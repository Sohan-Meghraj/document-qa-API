from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum , Boolean
from sqlalchemy.sql import func
from app.database import Base
import enum

class QuestionStatus(str, enum.Enum):
    PENDING = "pending"
    ANSWERED = "answered"

class Document(Base):
    __tablename__ = "documents"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    is_pdf = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Question(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"))
    question = Column(Text)
    answer = Column(Text, nullable=True)
    status = Column(Enum(QuestionStatus), default=QuestionStatus.PENDING)
    created_at = Column(DateTime(timezone=True), server_default=func.now())