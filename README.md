# Student Information Management System

## Introduction

This project provides a full solution for managing student information by combining a React Native front-end application with a Flask-powered RESTful API backend and a PostgreSQL database. It enables the submission, retrieval, updating, and deletion of student records, ensuring a consistent user experience across all mobile devices.

## Project Structure

The system is divided into three main components:

1. React Native Application: A cross-platform mobile application for data input and display.
2. Flask API: Serves as the middleman between the front-end application and the database, handling HTTP requests.
3. PostgreSQL Database: Stores student information securely and efficiently.

## Getting Started

### Prerequisites

1. Node.js and npm (for React Native app)
2. Python 3.x (for Flask API)
3. PostgreSQL (for the database)

### Setup Instructions

Frontend (React Native App)

1. Install dependencies: npm install
2. Start the application: npm start

Backend (Flask API)

1. Create a virtual environment and activate it:

python3 -m venv venv
source venv/bin/activate # Use `venv\Scripts\activate` on Windows

2. Install required Python packages: pip install flask flask-restful flask-cors psycopg2-binary

3. Initialize the database with infoDetail.sql script.

4. Run the Flask server: python server.py

Database

Set up a PostgreSQL database and apply the schema from infoDetail.sql.

## API Reference

1. POST /infoitem: Submit new student information.
2. GET /infoitem: Retrieve all student records.
3. PUT /infoitem/<id>: Update a specific student record.
4. DELETE /infoitem/<id>: Delete a specific student record.

## Features

Submit and validate student information through a user-friendly mobile interface.
View all student records stored in the database.
Update or delete existing student information.

## Future Work

Enhance the security of the application by implementing authentication and authorization mechanisms.
Introduce more interactive elements in the UI for a better user experience.
Expand the database schema to include more details about students.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your improvements.

## Screenshots

<img src="images/S1.png" alt="RIT APP" width="200" height="400">
<img src="images/S2.png" alt="RIT APP" width="200" height="400">
