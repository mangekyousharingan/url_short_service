#!/bin/bash

set -e

# Run database migrations if needed
if [ "${ENVIRONMENT}" = "development" ]; then
    echo "Running database migrations..."
    alembic upgrade head
fi

# Start the application
echo "Starting application on ${APP_HOST}:${APP_PORT}..."
exec uvicorn src.main:app --host ${APP_HOST} --port ${APP_PORT} --reload
