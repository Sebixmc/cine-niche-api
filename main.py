from fastapi import FastAPI, HTTPException
import json
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

# ✅ CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://cine-niche.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load recommendation data
with open("collab_recommendations.json") as f:
    user_recs = json.load(f)

with open("content_recommendations.json") as f:
    item_recs = json.load(f)

with open("hybrid_recommendations.json") as f:
    hybrid_recs = json.load(f)

with open("enriched_user_recommendations.json") as f:
    enriched_user_recs = json.load(f)



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

@app.get("/recommend/hybrid/{show_id}")
def recommend_hybrid(show_id: str):
    if show_id in hybrid_recs:
        return {"show_id": show_id, "recommendations": hybrid_recs[show_id]}
    else:
        raise HTTPException(status_code=404, detail="Show not found in hybrid recommendations")
    
@app.get("/recommend/enriched/{user_id}")
def recommend_enriched(user_id: str):
    if user_id in enriched_user_recs:
        return {"user_id": user_id, "recommendations": enriched_user_recs[user_id]}
    else:
        raise HTTPException(status_code=404, detail="User not found in enriched recommendations")

