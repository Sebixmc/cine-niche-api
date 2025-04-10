from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:3000",
    "https://proud-meadow-034f6310f.6.azurestaticapps.net"
    ]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load recommendation data
with open("collab_recommendations.json") as f:
    user_recs = json.load(f)

with open("content_recommendations.json") as f:
    item_recs = json.load(f)

@app.get("/")
def root():
    return {"message": "CineNiche Recommendation API is up 🚀"}

@app.get("/recommend/user/{user_id}")
def recommend_user(user_id: str):
    if user_id in user_recs:
        return {"user_id": user_id, "recommendations": user_recs[user_id]}
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.get("/recommend/item/{show_id}")
def recommend_item(show_id: str):
    if show_id in item_recs:
        return {"show_id": show_id, "recommendations": item_recs[show_id]}
    else:
        raise HTTPException(status_code=404, detail="Show not found")
