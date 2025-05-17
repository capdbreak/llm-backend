# FinanceFlow LLM Backend

A FastAPI backend service for performing sentiment analysis and relevance scoring on financial news articles using large language models (LLMs) via LangChain.

---

## 🧠 Features

- 📰 Analyze news article content for:
  - Summary
  - Valence (1–5)
  - Arousal (1–5)
  - Importance (1–10)
- 📦 Built with [FastAPI](https://fastapi.tiangolo.com/) and [LangChain](https://www.langchain.com/)
- 🐳 Containerized with Docker
- 📜 Declarative dependency management using Poetry

---

## 🚀 Getting Started

### Requirements

- Python 3.13+
- [Poetry](https://python-poetry.org/)
- (Optional) Docker

---

### 🔧 Local Development

#### 1. Install Dependencies

```bash
poetry install
```

#### 2. Run the Server

```bash
poetry run uvicorn financeflow_llm_backend.server:app --reload
```

#### 3. Test Health Check

```bash
curl http://localhost:8000/health
```

---

### 🐳 Run with Docker

#### 1. Build the Image

```bash
docker build -t financeflow-llm-backend .
```

#### 2. Run the Container

```bash
docker run -p 8000:8000 financeflow-llm-backend
```

---

## 📡 API Usage

### `POST /analyze`

Analyze one or more articles under a specific subject.

#### Request Body

```json
{
  "subject": "S&P 500",
  "articles": [
    {
      "title": "Breaking News",
      "article": "Full text of the article..."
    }
  ]
}
```

#### Response

```json
{
  "results": [
    {
      "summary": "...",
      "valence": 3,
      "arousal": 2,
      "importance": 6
    }
  ]
}
```

---

## 📁 Project Structure

```
financeflow_llm_backend/
├── core.py           # Load LLM chain logic
├── server.py         # FastAPI application entry
pyproject.toml        # Poetry project config
Dockerfile            # Container configuration
README.md             # You're reading this
```

---

## ⚖ License

[MIT](./LICENSE)

---

## 🧑‍💻 Author

**amicus-veritatis**  
📧 otome@u.sogang.ac.kr

---

