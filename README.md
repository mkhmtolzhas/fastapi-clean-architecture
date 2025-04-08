# FastAPI Boilerplate

This repository provides a boilerplate for building web applications using [FastAPI](https://fastapi.tiangolo.com/). It is designed to help you quickly set up a project with best practices and a clean architecture.

## Features

- **FastAPI**: High-performance web framework for building APIs.
- **Modular Structure**: Organized codebase for scalability and maintainability.
- **Database Integration**: Pre-configured with SQLAlchemy support.
- **Environment Configuration**: `.env` file support for managing environment variables.
- **Docker Support**: Dockerfile and docker-compose for containerized development.

## Project Structure

```bash
├── alembic.ini
├── app.log
├── docker-compose.yaml
├── dockerfile
├── migrations
├── poetry.lock
├── pyproject.toml
├── README.md
└── src
    ├── api
    │   ├── http
    │   │   ├── api_router.py
    │   │   ├── dependencies.py
    │   │   ├── __init__.py
    │   │   ├── v1
    │   │   │   ├── endpoints
    │   │   │   │   ├── domain_router.py
    │   │   │   │   ├── __init__.py
    │   │   │   ├── __init__.py
    │   │   │   └── router.py
    │   │   └── v2
    ├── core
    │   ├── app
    │   │   ├── app_creator.py
    │   │   ├── __init__.py
    │   │   ├── lifespan.py
    │   ├── connections
    │   │   ├── cache.py
    │   │   ├── connection.py
    │   │   ├── database.py
    │   │   ├── __init__.py
    │   ├── container.py
    │   ├── __init__.py
    │   ├── logger
    │   │   ├── __init__.py
    │   │   ├── logger.py
    │   ├── config.py
    ├── __init__.py
    ├── main.py
    ├── models
    │   ├── base_model.py
    │   ├── domain_model.py
    │   ├── __init__.py
    ├── repositories
    │   ├── base_repositiry.py
    │   ├── domain_repository.py
    │   ├── __init__.py
    ├── schemas
    │   ├── base_schema.py
    │   ├── domain_schema.py
    │   ├── __init__.py
    ├── usecases
    │   ├── base_usecase.py
    │   ├── domain_usecase.py
    └── utils
        ├── __init__.py
        ├── model_adapter.py
```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/mkhmtolzhas/fastapi-clean-architecture
    cd fastapi-clean-architecture
    ```

2. Install Poetry if not already installed:
    ```bash
    pip install poetry
    poetry shell
    ```

3. Install dependencies using Poetry:
    ```bash
    poetry install
    ```

4. Set up environment variables:
    Create a `.env` file in the root directory and configure your environment variables.

5. Run the application:
    ```bash
    uvicorn src.main:app --reload
    ```


## Usage

- Access the API documentation at `http://127.0.0.1:8000/docs` (Swagger UI) or `http://127.0.0.1:8000/redoc` (ReDoc).
- Customize the boilerplate by adding your own routes, models, and business logic.


## Docker

Build and run the application using Docker:
```bash
docker-compose up --build
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).