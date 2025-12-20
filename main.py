from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Status": "Secure & Live"}

import os

# SECURE: We pull the secret from the system environment, not the code
SECRET_KEY = os.getenv("APP_SECRET_KEY", "default_safe_value")

password = 'incorrect'
