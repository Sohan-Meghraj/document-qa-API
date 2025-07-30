markdown
# Document Q&A API with PDF Support

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python)

A FastAPI microservice for document processing and question answering, featuring PDF text extraction and async LLM response simulation.

## 🌟 Features

- **PDF Upload & Parsing**
- **Document Storage** (PostgreSQL)
- **Question Answering** (Async Mock LLM)
- **RESTful API Endpoints**
- **Async Background Processing**

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- PostgreSQL 15+
- [Poetry](https://python-poetry.org/) (recommended)

### Installation
```bash
# Clone repository
git clone https://github.com/Sohan-Meghraj/document-qa-API.git
cd document-qa-API

# Install dependencies (using Poetry)
poetry install

# Or with pip
pip install -r requirements.txt
Configuration
Create .env file:

bash
cp .env.example .env
Update with your credentials:

ini
DATABASE_URL="postgresql+asyncpg://user:password@localhost:5432/dbname"
Running the API
bash
uvicorn app.main:app --reload
Access docs at: http://localhost:8000/docs

📚 API Documentation
Endpoints
Method	Endpoint	Description
POST	/documents/	Upload text document
POST	/pdfs/	Upload PDF file
POST	/documents/{id}/question	Ask question about document
GET	/questions/{id}	Get question status/answer
Example Requests
Upload PDF:

bash
curl -X POST "http://localhost:8000/pdfs/" \
  -F "file=@document.pdf" \
  -F "pdf_data='{\"title\":\"Sample\",\"description\":\"Test PDF\"}'"
Ask Question:

bash
curl -X POST "http://localhost:8000/documents/1/question" \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the main topic?"}'
🛠️ Development
Database Setup
Create PostgreSQL database

Run migrations:

bash
alembic upgrade head
Testing
bash
pytest tests/ -v
📦 Project Structure
text
document-qa-API/
├── app/
│   ├── __init__.py
│   ├── main.py         # FastAPI app
│   ├── models.py       # DB models
│   ├── schemas.py      # Pydantic models
│   ├── services.py     # Business logic
│   └── database.py     # DB connection
├── tests/              # Test cases
├── alembic/            # Database migrations
├── .env.example        # Environment template
├── requirements.txt    # Dependencies
└── README.md           # This file
🤝 Contributing
Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit changes (git commit -m 'Add amazing feature')

Push to branch (git push origin feature/AmazingFeature)

Open Pull Request

📄 License
Distributed under the MIT License.

Note: Replace placeholder credentials with your actual database configuration before deployment.

text

### Key Additions to Your Project:
1. Create these files if missing:
   - `.env.example` (as shown in the config section)
   - `requirements.txt` (run `pip freeze > requirements.txt`)

2. Add badges by copying the image URLs from:
   - [Shields.io](https://shields.io/) for custom badges
   - Replace `Sohan-Meghraj/document-qa-API` with your actual repo path

3. For the **alembic setup**, ensure you have:
   ```ini
   # alembic.ini
   [alembic]
   script_location = alembic
   sqlalchemy.url = postgresql+asyncpg://user:pass@localhost/dbname
