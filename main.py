from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base, NameEntry
from schemas import HelloResponse, NameCreate

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Render Hello API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/hello", response_model=HelloResponse)
def create_name(payload: NameCreate, db: Session = Depends(get_db)):
    cleaned_name = payload.name.strip()
    if not cleaned_name:
        raise HTTPException(status_code=400, detail="Name cannot be empty")

    entry = NameEntry(name=cleaned_name)
    db.add(entry)
    db.commit()
    db.refresh(entry)

    return HelloResponse(id=entry.id, message=f"Hello {cleaned_name}")
