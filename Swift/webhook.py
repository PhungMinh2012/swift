from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"FastAPI":"Is running   "}

@app.post("/webhook")
async def hook(request: Request):
    data = await request.json()
    return {"Data": data, "Received": "got it"}