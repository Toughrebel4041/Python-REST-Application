from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import httpx
import sqlite3

app = FastAPI()

# Base URL of the ReqRes.in API
BASE_URL = "https://reqres.in/api"

# SQLite database connection
conn = sqlite3.connect('users.db')
conn.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, job TEXT)''')

# Pydantic model for user data
class User(BaseModel):
    name: str
    job: str

# Endpoint to create a new user
@app.post("/api/users", response_model=User)
async def create_user(user: User):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/users", json=jsonable_encoder(user))
        if response.status_code == 201:
            user_data = response.json()
            # Store the user in SQLite database
            conn.execute('INSERT INTO users (name, job) VALUES (?, ?)', (user_data["name"], user_data["job"]))
            conn.commit()
            return user_data
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)

# Endpoint to get a user by ID
@app.get("/api/user/{user_id}", response_model=User)
async def get_user(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/users/{user_id}")
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)

# Endpoint to delete a user by ID
@app.delete("/api/user/{user_id}")
async def delete_user(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL}/users/{user_id}")
        if response.status_code == 204:
            # Delete the user from SQLite database
            conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
            conn.commit()
            return JSONResponse(status_code=204)
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
