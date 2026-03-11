from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
import os

from backend.database import get_all_skin_mortality_data

app = FastAPI(title="Sun Safety Dashboard")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── API 1: Skin mortality data from RDS ───────────────────────────────────────
@app.get("/api/get_all_skin_mortality_data")
def melanoma_data():
    return get_all_skin_mortality_data()

# ── Health check ──────────────────────────────────────────────────────────────
@app.get("/health")
def health():
    return {"status": "ok"}

# ── Mangum adapter ────────────────────────────────────────────────────────────
handler = Mangum(app, lifespan="off")
