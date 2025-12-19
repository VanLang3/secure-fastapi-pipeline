from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Status": "Secure & Live"}

# THIS IS A SECURITY VULNERABILITY (Hardcoded password)
password = "admin123_very_secret"
