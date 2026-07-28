from fastapi import APIRouter, HTTPException

from app.chatbot import chatbot
from app.models import (
    ChatRequest,
    ChatResponse,
    ResetResponse,
)
from app.session import session_manager

router = APIRouter(prefix="/api/v1")


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.post("/reset", response_model=ResetResponse)
def reset():

    session_id = session_manager.create_session()

    return ResetResponse(session_id=session_id)


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    session = session_manager.get_session(request.session_id)

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Invalid session."
        )

    print("Before:", session)

    response = chatbot.process_message(
        session,
        request.message
    )

    print("After:", session)

    return response