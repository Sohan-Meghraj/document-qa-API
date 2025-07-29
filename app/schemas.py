from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DocumentCreate(BaseModel):
    title: str
    content: str

class DocumentResponse(BaseModel):
    id: int
    title: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class QuestionCreate(BaseModel):
    question: str

class QuestionResponse(BaseModel):
    id: int
    document_id: int
    question: str
    answer: Optional[str] = None
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True