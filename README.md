# Python-REST-Application
The Python REST application is a simple API built using the FastAPI framework, which enables communication with the ReqRes.in API. The application follows the RESTful architecture, allowing users to perform CRUD (Create, Read, Update, Delete) operations on user data.

Features of the Python REST Application:

Endpoints:

POST /api/users: This endpoint allows users to create a new user. It accepts user data in JSON format, such as the user's name and job. The data is sent to the ReqRes.in API to create the user and is also stored in an SQLite database.
GET /api/user/{userId}: This endpoint retrieves user data by user ID. It makes a request to the ReqRes.in API to fetch the user's information and returns it in JSON representation.
DELETE /api/user/{userId}: This endpoint allows users to delete a user by user ID. It sends a request to the ReqRes.in API to delete the user and also removes the user's data from the SQLite database.
FastAPI Framework:

The application is built using the FastAPI framework, which provides a robust and efficient platform for building web APIs in Python.
FastAPI offers automatic data validation, serialization, and documentation generation, making it easy to define API endpoints and handle requests and responses.
ReqRes.in Integration:

The application communicates with the ReqRes.in API (https://reqres.in/api) to create, fetch, and delete user data.
For creating and deleting users, the application makes requests to the ReqRes.in API endpoints for user creation and deletion.
For fetching user data, the application retrieves information from the ReqRes.in API based on the provided user ID.
SQLite Database:

The application uses an SQLite database to store the user data locally.
When a user is created or deleted, the data is stored or removed from the SQLite database as well as sent to or removed from the ReqRes.in API.
Docker and Docker Compose:

The application is containerized using Docker and can be deployed using Docker Compose.
Docker allows for consistent and isolated environments for running the application, making it easier to manage dependencies and ensure portability.
The Python REST application provides a simple but functional API that integrates with an external API (ReqRes.in) and stores data locally in an SQLite database. It showcases the use of the FastAPI framework for building a modern and efficient web API and demonstrates how Docker can be used to package and deploy the application in a containerized environment.
