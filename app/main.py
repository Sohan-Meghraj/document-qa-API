from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.models import Base
from app.database import engine, get_db
from app.schemas import DocumentCreate, DocumentResponse, QuestionCreate, QuestionResponse
from app.services import create_document, get_document, create_question, get_question
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/documents/", response_model=DocumentResponse)
async def upload_document(document: DocumentCreate, db: AsyncSession = Depends(get_db)):
    return await create_document(db, document)

@app.get("/documents/{document_id}", response_model=DocumentResponse)
async def get_document_by_id(document_id: int, db: AsyncSession = Depends(get_db)):
    document = await get_document(db, document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document

@app.post("/documents/{document_id}/question", response_model=QuestionResponse)
async def ask_question(
    document_id: int, 
    question: QuestionCreate, 
    db: AsyncSession = Depends(get_db)
):
    document = await get_document(db, document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    
    return await create_question(db, document_id, question)

@app.get("/questions/{question_id}", response_model=QuestionResponse)
async def get_question_by_id(question_id: int, db: AsyncSession = Depends(get_db)):
    question = await get_question(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@app.get("/health")
async def health_check():
    return {"status": "healthy"}