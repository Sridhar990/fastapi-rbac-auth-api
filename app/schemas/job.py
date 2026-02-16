from pydantic import BaseModel, HttpUrl
from datetime import date, datetime


class JobCreate(BaseModel):
    company_name: str
    role: str
    application_end_date: date
    job_link: HttpUrl


class JobResponse(BaseModel):
    id: int
    company_name: str
    role: str
    application_end_date: date
    job_link: HttpUrl
    created_at: datetime

    class Config:
        fro_attributes = True

