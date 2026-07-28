from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import router

app = FastAPI(
    title="North Star Support Bot API",
    description="Backend API for the North Star Support chatbot.",
    version="1.0.0",
)

# Allow frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # We'll tighten this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "Welcome to North Star Support Bot API",
        "docs": "/docs",
        "health": "/api/v1/health"
    }

app.include_router(router)