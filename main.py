from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# Allow frontend requests (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection
client = MongoClient(os.getenv("MONGODB_URI"))
db = client["social_media"]
collection = db["fb_comments_sentiment"]

@app.get("/")
def root():
    return {"message": "Facebook Sentiment API running!"}

@app.get("/posts")
def get_posts():
    posts = list(collection.find({}, {"_id": 0}))
    return posts

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)