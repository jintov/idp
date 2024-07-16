from fastapi import FastAPI

app = FastAPI()

@app.get("/info")
def info():
    return {"name": "${{values.name}}", "version": "1.0.0"}