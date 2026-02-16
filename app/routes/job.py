from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.job import Job
from app.schemas.job import JobResponse
from app.core.deps import get_current_user
from typing import List

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.get("/", response_model=List[JobResponse])
def list_jobs(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    jobs = db.query(Job).order_by(Job.application_end_date.asc()).all()
    return jobs
