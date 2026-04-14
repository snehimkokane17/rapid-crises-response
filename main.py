from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, Resource, Alert
from groq import Groq

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

client = Groq(api_key="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")

@app.get("/resources")
def get_resources():
    db = SessionLocal()
    resources = db.query(Resource).all()
    db.close()
    return resources

@app.get("/alerts")
def get_alerts():
    db = SessionLocal()
    alerts = db.query(Alert).all()
    db.close()
    return alerts

@app.post("/reports")
def submit_report(title: str, description: str, location: str):
    return {"message": "Report received!", "title": title}

@app.post("/chat")
def chat(message: str):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a crisis response assistant helping people during emergencies. Answer helpfully and calmly."},
                {"role": "user", "content": message}
            ]
        )
        return {"reply": response.choices[0].message.content}
    except Exception as e:
        return {"reply": f"Error: {str(e)}"}