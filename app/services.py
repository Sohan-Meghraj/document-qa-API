from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Document, Question, QuestionStatus
import asyncio
import PyPDF2
from io import BytesIO

async def create_document(db: AsyncSession, document_data):
    document = Document(**document_data.dict())
    db.add(document)
    await db.commit()
    await db.refresh(document)
    return document

async def get_document(db: AsyncSession, document_id: int):
    return await db.get(Document, document_id)

async def create_question(db: AsyncSession, document_id: int, question_data):
    question = Question(
        document_id=document_id,
        question=question_data.question,
    )
    db.add(question)
    await db.commit()
    await db.refresh(question)
    
    # Simulate async processing
    asyncio.create_task(generate_answer(db, question.id))
    
    return question

async def generate_answer(db: AsyncSession, question_id: int):
    await asyncio.sleep(5)  # Simulate LLM processing
    
    async with db.begin():
        question = await db.get(Question, question_id)
        if question:
            question.answer = f"This is a generated answer to your question: {question.question}"
            question.status = QuestionStatus.ANSWERED
            await db.commit()

async def get_question(db: AsyncSession, question_id: int):
    return await db.get(Question, question_id)