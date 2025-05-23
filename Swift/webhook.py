from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"FastAPI":"Is running   "}  

@app.get("/webhook")
def get_webhook():
    return {
        "Message": "Webhook is running"
    }

@app.post("/webhook")
async def hook(request: Request):
    data = await request.json()
    print(data)
    return {"Data": data}