# ---- Base image with Python 3.13 ----
FROM python:3.13-slim

# ---- Set environment variables ----
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.2

# ---- System deps ----
RUN apt-get update \
    && apt-get install -y curl build-essential libffi-dev \
    && apt-get clean

# ---- Install Poetry ----
RUN curl -sSL https://install.python-poetry.org | python3 -

# ---- Set Poetry to PATH ----
ENV PATH="/root/.local/bin:$PATH"

# ---- Set working directory ----
WORKDIR /app

# ---- Copy project files ----
COPY pyproject.toml poetry.lock ./
COPY financeflow_llm_backend ./financeflow_llm_backend

# ---- Install dependencies ----
RUN poetry install --no-root --only main

# ---- Expose port and run ----
EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "financeflow_llm_backend.server:app", "--host", "0.0.0.0", "--port", "8000"]

