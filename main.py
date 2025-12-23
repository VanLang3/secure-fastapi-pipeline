import os
import datetime
from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# --- CONFIGURATION ---
# We get the connection string from the docker-compose environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Set up the Database Engine (The Connection Manager)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- THE MODEL (The Table Schema) ---
class SecurityLog(Base):
    __tablename__ = "security_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    message = Column(String)

# Create the tables in the database (Automatic Migration)
Base.metadata.create_all(bind=engine)

# --- APP SETUP ---
app = FastAPI()

# Dependency: Get a database session for each request, then close it
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- THE ENDPOINT ---
@app.get("/")
def read_root(db: Session = Depends(get_db)):
    # 1. Create a new log entry
    new_log = SecurityLog(message="API accessed - Security Scan has Passed")
    
    # 2. Add it to the "Staging Area"
    db.add(new_log)
    
    # 3. Commit it to the database (Save permanently)
    db.commit()
    
    return {
        "Status": "Secure & Live", 
        "Database": "Connected & Logging",
        "Log_ID": new_log.id
    }