from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routes import auth, user, admin, job
import app.models

# create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="RBAC Auth System with Jobs",
    description="FastAPI project with OTP auth, JWT, RBAC, and job postings",
    version="1.0.0")


# ---- CORS CONFIG ----
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # React
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)




# include routers
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(admin.router)
app.include_router(job.router)

