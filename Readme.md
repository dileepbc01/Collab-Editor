# Server Startup Instructions

**Note:** This project is currently under development.

## Tech Stack

The project utilizes the following technologies:

* **FastAPI:** A modern, fast (high-performance) web framework for building APIs with Python.
* **Next.js:** A React framework for building full-stack web applications, known for server-side rendering and static site generation.
* **SQLModel:** A library for interacting with SQL databases from Python, designed to be easy to use and combining features of Pydantic and SQLAlchemy.
* **Alembic:** A lightweight database migration tool for use with SQLAlchemy.
* **PostgreSQL:** A powerful, open-source object-relational database system.
* **Redis:** An in-memory data structure store, used as a database, cache, and message broker.
* **Shadcn/ui:** A collection of re-usable UI components that you can copy and paste into your apps, built with Radix UI and Tailwind CSS.

## Backend Server

To start the backend server:

1.  Navigate to the `./backend` directory.
    ```bash
    cd ./backend
    ```
2.  Run Docker Compose.
    ```bash
    docker compose up
    ```

## Frontend Server

To start the frontend server:

1.  Navigate to the `./frontend` directory.
    ```bash
    cd ./frontend
    ```
2.  Install the necessary Node modules.
    ```bash
    npm install
    ```
3.  Start the development server.
    ```bash
    npm run dev
    ```