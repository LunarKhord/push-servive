# Generate a base image
FROM python:3.11-slim

# Create .env path for uv
ENV UV_PROJECT_ENVIRONMENT="app/.venv"

# Equip the base image with necessary dependencies: uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
libpq-dev \
gcc \
&& rm -rf /var/lib/apt/lists/*


COPY pyproject.toml uv.lock ./

# Install project dependencies
RUN uv sync --frozen --no-install-project --no-dev


COPY . .

RUN uv sync --frozen --no-dev

# Excecute the application
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--reload", "--port", "8000"]