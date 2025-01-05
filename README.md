# Kubi CI/CD Integration

This repository contains a integration demo for **Kubiya**. It is built using **FastAPI** with dependencies managed by **Poetry**.

---

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Clone the Repository](#clone-the-repository)
- [Running the Application](#running-the-application)
  - [Using Poetry](#using-poetry)
  - [Using Docker Compose](#using-docker-compose)
- [Testing](#testing)
- [Linting](#linting)
- [Notes](#notes)

---

## Introduction

This project integrates the CI/CD workflows with **Kubiya** teammates.

---

## Prerequisites

Ensure the following tools are installed on your system before proceeding:

### Docker
Docker is required for containerized deployment.

```bash
docker --version
```

### Python 3.13
Python is needed for running the application locally.

```bash
python --version
```

### Poetry
Poetry is used for dependency management and virtual environments.

```bash
pip install poetry
poetry --version
```

---

## Installation

### Clone the Repository

Follow these steps to get a local copy of the project:

1. Clone the repository:

   ```bash
   git clone https://github.com/jtarang/kubi-cicd-integration
   ```

2. Navigate to the project directory:

   ```bash
   cd kubi-cicd-integration
   ```

---

## Running the Application

Choose one of the following methods to run the application:

### Using Poetry

1. Install the project dependencies:

   ```bash
   poetry install
   ```

2. Run the application:

   ```bash
   poetry run uvicorn main:app --reload
   ```

### Using Docker Compose

1. Build and start the application using Docker Compose:

   ```bash
   docker compose up --build
   ```

2. Access the application by navigating to `http://localhost:8000` in your web browser.

---

## Testing

Run tests to ensure the application is working correctly:

```bash
poetry run pytest
```

---

## Linting

Check the code for style and quality issues:

```bash
poetry run pylint
```

---

## Notes

- If using Poetry for the first time, ensure it is properly configured in your environment. You can find documentation [here](https://python-poetry.org/docs/).
- Docker Compose is recommended for a streamlined deployment process.
- For additional configuration options, refer to the `docker-compose.yml` repository.
