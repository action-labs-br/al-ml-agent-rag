from fastapi import FastAPI

from app.models import ChatRequest, ChatResponse, PredictRequest, PredictResponse

app = FastAPI(title="SpellForge API")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
async def predict(request: PredictRequest):
    # TODO: initialize CardPopularityPredictor and call predict()
    # Hint: train the model at startup (e.g. using FastAPI lifespan)
    # and store it in app.state
    raise NotImplementedError("Wire up the predictor")


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    # TODO: initialize SpellForgeAgent and call process_message()
    # Hint: initialize the agent at startup with the trained predictor
    raise NotImplementedError("Wire up the agent")
