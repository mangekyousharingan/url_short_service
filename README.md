# URL Shortener Service

A robust URL shortening service built with FastAPI, following the Ports & Adapters (Hexagonal) architecture pattern. This service allows users to create, manage, and track short URLs with detailed statistics.

## Features

- Create short URLs from long URLs
- Retrieve original URLs using short codes
- Update existing short URLs
- Delete short URLs
- Track URL access statistics
- RESTful API with proper HTTP status codes
- Async database operations with PostgreSQL
- Clean architecture implementation

## Architecture

The project follows the Ports & Adapters (Hexagonal) architecture pattern, which promotes separation of concerns and maintainability. The architecture consists of:

### Core Domain
- **Entities**: Domain models with business logic
- **Ports**: Interfaces defining the contract for external interactions
- **Services**: Business logic implementation

### Adapters
- **API**: FastAPI controllers and request/response models
- **Database**: SQLAlchemy implementation of repositories

## Project Structure

```
src/
├── core/
│   ├── entities/       # Domain models
│   ├── ports/          # Interface definitions
│   ├── services/       # Business logic
│   └── config.py       # Application configuration
├── adapters/
│   ├── api/            # FastAPI controllers
│   └── database/       # Database implementations
└── main.py             # Application entry point
```

## API Endpoints

### Create Short URL
```http
POST /shorten
Content-Type: application/json

{
  "url": "https://www.example.com/some/long/url"
}
```

### Get URL by Short Code
```http
GET /shorten/{short_code}
```

### Update URL
```http
PUT /shorten/{short_code}
Content-Type: application/json

{
  "url": "https://www.example.com/some/updated/url"
}
```

### Delete URL
```http
DELETE /shorten/{short_code}
```

### Get URL Statistics
```http
GET /shorten/{short_code}/stats
```

## Prerequisites

- Python 3.9+
- Poetry (Python package manager)
- Docker and Docker Compose
- PostgreSQL

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/url-shortener-service.git
cd url-shortener-service
```

2. Install dependencies:
```bash
poetry install
```

> **Note**: This project uses Poetry for dependency management only. Package mode is disabled in `pyproject.toml` (`package-mode = false`). This means Poetry will only manage dependencies and virtual environments, not package building and publishing.

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Start the services using Docker Compose:
```bash
docker-compose up -d
```

5. Run the application:
```bash
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000` with Swagger documentation at `http://localhost:8000/docs`.

## Development

### Pre-commit Hooks
This project uses pre-commit hooks to ensure code quality. The following checks are automatically run before each commit:

- Code formatting with Black
- Import sorting with isort
- Type checking with mypy
- Linting with ruff
- Security checks with bandit
- Code style with flake8
- Python version compatibility with pyupgrade

To set up pre-commit hooks:
```bash
pre-commit install
```

The hooks will run automatically on each commit. You can also run them manually:
```bash
pre-commit run --all-files
```

### Running Tests
```bash
poetry run pytest
```

### Code Formatting
```bash
poetry run black .
poetry run isort .
```

### Type Checking
```bash
poetry run mypy .
```

### Linting
```bash
poetry run ruff check .
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- FastAPI for the web framework
- SQLAlchemy for database operations
- Poetry for dependency management
- Docker for containerization

## Database Migrations

This project uses Alembic for database migrations. Migrations are automatically applied when the application starts in development mode.

### Creating a New Migration

1. Make changes to your SQLAlchemy models in `src/adapters/database/models.py`
2. Generate a new migration:
```bash
alembic revision --autogenerate -m "description_of_changes"
```

3. Review the generated migration file in `migrations/versions/`
4. Apply the migration:
```bash
alembic upgrade head
```

### Migration Workflow

1. **Development Environment**:
   - Migrations are automatically applied when the application starts
   - You can manually run migrations using `alembic upgrade head`

2. **Production Environment**:
   - Migrations should be reviewed and tested in development first
   - Apply migrations manually or through your deployment pipeline
   - Always backup your database before applying migrations

### Common Migration Commands

```bash
# Create a new migration
alembic revision --autogenerate -m "description"

# Apply all pending migrations
alembic upgrade head

# Rollback the last migration
alembic downgrade -1

# Show migration history
alembic history

# Show current migration version
alembic current
```
