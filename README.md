# Movie Watchlist API

> A robust RESTful API for managing a personal movie watchlist, built with Python, FastAPI, and PostgreSQL. This project follows Clean Architecture principles and is fully containerized with Docker.

This API provides a complete backend solution for a movie tracking application, featuring user authentication, watchlist management, movie rating, and more. It is designed to be scalable, maintainable, and secure.

## ✨ Features

- **User Authentication:** Secure user registration and login using JSON Web Tokens (JWT).
- **Watchlist Management:** Add movies to a personal watchlist and categorize them.
- **Movie Tracking:** Mark movies as "watched" or "want to watch".
- **Rating System:** Rate watched movies on a scale of 1 to 5.
- **Review System:** Write and manage personal reviews for movies.
- **Fully Asynchronous:** Built with FastAPI and `asyncpg` for high performance.
- **Interactive Documentation:** Automatic, interactive API documentation powered by Swagger UI and ReDoc.

## 🛠️ Tech Stack

- **Backend:** Python 3.11, FastAPI
- **Database:** PostgreSQL
- **Containerization:** Docker, Docker Compose
- **Dependency Management:** Poetry
- **Web Server:** Uvicorn
- **Authentication:** `passlib` for hashing, JWT for sessions

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine for development and testing purposes.

### Prerequisites

You must have the following software installed on your system:

- [Docker](https://www.docker.com/products/docker-desktop/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation & Running

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/Sir-Moulodi/movie-watchlist-api--by-Moulodi.git](https://github.com/Sir-Moulodi/movie-watchlist-api--by-Moulodi.git)
    cd movie-watchlist-api--by-Moulodi
    ```

2.  **Create an Environment File:**
    This project uses a `.env` file to manage environment variables. Copy the example file to create your own local configuration:
    ```sh
    cp .env.example .env
    ```
    You can modify the variables inside `.env` if needed, but the default values are configured to work with Docker Compose out of thebox.

    *(Make sure to create a `.env.example` file with the content shown in the next section).*

3.  **Build and Run the Application:**
    Use Docker Compose to build the images and run the containers in detached mode (`-d`):
    ```sh
    docker-compose up --build -d
    ```

The API will now be running and available at `http://localhost:8000`.

## 📖 API Documentation

Once the application is running, you can access the interactive API documentation in your browser. FastAPI automatically generates this documentation from your code.

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

These interfaces allow you to explore all API endpoints, view their models, and test them live.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---