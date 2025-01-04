# Project Info Backend

This repository contains the backend service for the **Project Info** application. It connects to a MySQL database and provides APIs to fetch data for the React frontend.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Endpoints](#endpoints)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)

---

## Overview
The **Project Info Backend** is built using Python and Flask. It connects to a MySQL database to fetch and serve data related to project information.

### Features
- Connects to a MySQL database
- Provides a RESTful API for the React frontend
- Lightweight and easy to extend

---

## Prerequisites
- **Python 3.8+**: Ensure Python is installed on your machine.
    - Check version: `python3 --version`
- **pip**: The package installer for Python.
    - Check version: `pip3 --version`
- **MySQL Database**: A running MySQL server instance.
    - MySQL Workbench 8.0.31: [Install Guide](https://dev.mysql.com/doc/workbench/en/wb-installing-mac.html)
    - MySQL Server 8.0.31: [Install Guide](https://dev.mysql.com/doc/refman/8.0/en/macos-installation-pkg.html)

---

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/project_info_backend.git
    cd project_info_backend
    ```

2. Install dependencies:
    ```bash
    pip3 install flask flask-cors mysql-connector-python
    ```

---

## Running the Application
1. Save the backend script as `app.py`.

2. Run the backend server:
    ```bash
    python3 app.py
    ```

3. Access the backend API:
    - Base URL: `http://localhost:5000`
    - Example Endpoint: `http://localhost:5000/api/projects`

---

## Endpoints
| Endpoint                | Method | Description                      |
|-------------------------|--------|----------------------------------|
| `/api/projects`         | GET    | Fetches all projects information |

---

## Folder Structure
```
project_info_backend/
├── app.py                # Main application file
├── requirements.txt      # Python dependencies (optional)
├── README.md             # Project documentation
└── ...
```

---

## Contributing
1. Fork the repository.
2. Create a feature branch:
    ```bash
    git checkout -b feature-name
    ```
3. Commit changes:
    ```bash
    git commit -m "Add a feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Create a pull request.



