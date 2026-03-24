from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Interview Assistant is running!"}

@app.get("/question")
def get_question():
    return {"question": "What is the difference between list and tuple in Python?"}