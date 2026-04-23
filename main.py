from fastapi import FastAPI
app = FastAPI()
@app.get("/health")
def health():
   return {"status": "ok"}
@app.get("/info")
def info():
   return {"app": "devops-demo", "version": "1.0"}
