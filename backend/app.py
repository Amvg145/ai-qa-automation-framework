from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check():
    return {
        "status": "success",
        "message": "AI QA backend running"
    }

@app.post("/chat")
def chat():
    return {
        "response": "I can help you with refund related issues"
    }