
# Day 14 — Docker Fundamentals

## Project Overview

This project demonstrates Docker fundamentals by containerizing a simple Python HTTP application.

The application returns JSON responses and supports health checking.

## Technologies Used

- Python 3.11
- Docker
- Dockerfile
- Docker Compose
- Git and GitHub

## Project Files

| File | Description |
|---|---|
| `app.py` | Python HTTP application |
| `Dockerfile` | Instructions for building the Docker image |
| `requirements.txt` | Dependency information |
| `.dockerignore` | Excludes unnecessary files from the Docker build context |
| `compose.yaml` | Docker Compose configuration |
| `README.md` | Project documentation |

## Application Endpoints

| Endpoint | Description | Expected Status |
|---|---|---|
| `/` | Returns a success message | 200 |
| `/health` | Returns the health status | 200 |
| Any unknown path | Returns an error message | 404 |

## Prerequisites

- Docker Desktop installed and running
- Git installed (for version control)

## Build the Docker Image

Run these commands from the project directory:

```powershell
docker build -t docker-python-app .
```

## Run the Container

```powershell
docker run -d --name python-docker-container -p 8000:8000 docker-python-app
```

## Test the Application

Open these URLs in your browser:

- http://localhost:8000/
- http://localhost:8000/health

## Useful Docker Commands

```powershell
docker images
docker ps
docker ps -a
docker logs python-docker-container
docker exec -it python-docker-container sh
docker stop python-docker-container
docker start python-docker-container
docker rm python-docker-container
```

## Run with Docker Compose

Make sure port 8000 is available, then run:

```powershell
docker compose up --build -d
docker compose ps
docker compose logs
```

Open the application at `http://localhost:8000/`.

To stop the Compose application:

```powershell
docker compose down
```

## Environment Variables

The application reads its listening port from the `PORT` environment variable. The default is `8000`.

Example:

```powershell
docker run -d --name python-env-practice -p 8001:8001 -e PORT=8001 docker-python-app
```

Test it at `http://localhost:8001/health`.

## Learning Outcomes

- Understood Docker images and containers
- Practised common Docker commands
- Created a Dockerfile
- Built and ran a custom Python Docker image
- Practised port mapping and environment variables
- Prepared a Docker Compose configuration
- Documented the project for GitHub

## Verification Note

Run and verify all documented commands before marking the practical complete. Some advanced practicals, including Docker Compose, should be tested separately.
