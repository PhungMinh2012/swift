from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def hook(request: Request):
    data = await request.json()
    return {"Data": data, "Received": "got it"}