from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
import httpx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/uv")
async def get_uv(lat: float = Query(...), lng: float = Query(...)):
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lng}"
        f"&daily=uv_index_max&timezone=auto&forecast_days=1"
    )
    async with httpx.AsyncClient() as client:
        res = await client.get(url)
        data = res.json()

    uv = data["daily"]["uv_index_max"][0]
    return {"uv": uv, "lat": lat, "lng": lng}

@app.get("/health")
def health():
    return {"status": "ok"}

handler = Mangum(app, lifespan="off")
