from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from . import models, database
from pydantic import BaseModel
import datetime

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

class WebhookPayload(BaseModel):
    user_id: str
    message: str
    timestamp: int

@app.get("/")
def read_root():
    return {"status": "ok", "service": "AI Consultant Backend"}

@app.post("/webhook")
async def receive_webhook(payload: WebhookPayload, db: Session = Depends(get_db)):
    """
    Receives a webhook from L-Message (simulated).
    Expected payload: {"user_id": "U123...", "message": "こんにちは", "timestamp": 123456789}
    """
    print(f"Received message from {payload.user_id}: {payload.message}")
    
    # 1. Generate AI Response (Simulated)
    ai_response = generate_ai_response(payload.message)
    
    # 2. Save to DB
    db_conversation = models.Conversation(
        user_id=payload.user_id,
        user_message=payload.message,
        ai_response=ai_response,
        timestamp=datetime.datetime.now()
    )
    db.add(db_conversation)
    db.commit()
    db.refresh(db_conversation)
    
    # 3. Return response to L-Message (or trigger L-Message API to send reply)
    # In a real scenario, we would call requests.post("https://api.line.me/...", ...)
    
    return {"reply": ai_response}

def generate_ai_response(message: str) -> str:
    """
    Simple rule-based + simulated AI logic
    """
    message = message.lower()
    if "悩み" in message or "集客" in message:
        return "集客に関するお悩みですね。現在、どのような媒体（Instagram, YouTubeなど）を使われていますか？"
    elif "いくら" in message or "費用" in message:
        return "費用についてはプランにより異なりますが、月額3万円からご用意しております。詳細な資料をお送りしましょうか？"
    elif "興味" in message:
        return "ありがとうございます！まずは無料診断からスタートできますが、ご希望されますか？"
    else:
        return "メッセージありがとうございます。担当者が確認次第、詳しくご返信いたします。（AI自動応答）"

# Endpoint to view logs (for Dashboard)
@app.get("/logs")
def get_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    logs = db.query(models.Conversation).order_by(models.Conversation.timestamp.desc()).offset(skip).limit(limit).all()
    return logs
