from model_main_dir.prediction import prediction_pipeline
from fastapi import FastAPI
import uvicorn

app = FastAPI()
@app.get('/')
def read():
    return {"prediction_model_name": "cfar_10_categorical_image_classification"}

@app.post("/openapi.json HTTP/")
async def image_read_pred():
    Prediction_pipeline = prediction_pipeline()
    return Prediction_pipeline

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)

