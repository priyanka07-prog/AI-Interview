from fastapi import FastAPI
from backend.AI_services import generate_question

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Interview Assistant is running!"}

@app.get("/question")
def get_question():
    question = generate_question()
    return {"question": question}
    