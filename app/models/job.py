from sqlalchemy import Column,String,Integer,Date,DateTime
from sqlalchemy.sql import func
from app.database import Base


class Job(Base):
    __tablename__="jobs"

    id=Column(Integer,primary_key=True,autoincrement=True)
    company_name=Column(String(150),nullable=False)
    role=Column(String(150),nullable=False)
    job_link=Column(String(300),nullable=False)
    application_end_date=Column(Date,nullable=False)
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    