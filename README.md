# kubi-cicd-integration

This repository contains the integration for **Kubi CI/CD**. It is built using **FastAPI** with dependencies managed by **Poetry**.

## Table of Contents

- [Installation](#installation)
- [Running the Application](#running-the-application)
  - [Using Poetry](#using-poetry)
  - [Using Docker Compose](#using-docker-compose)
- [Testing](#testing)
- [Linting](#linting)

---

## Prerequisites
Before running the application, ensure that the following tools are installed on your system:

### Docker

```bash
docker --version
```

### Python 3.13
```bash
python --version
```

### Poetry

```bash
pip install poetry
poetry --version
````

## Installation

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/jtarang/kubi-cicd-integration
cd kubi-cicd-integration
```

## Running the Application
### Using Poetry 
```bash
 poetry install
 ```

### Using Docker Compose
```bash
docker compose up --build
```

## Testing
```bash 
poetry run pytest
```

## Linting
```bash
poetry run pylint
```
