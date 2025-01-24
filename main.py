from fastapi import FastAPI
from routes.order_router import router
import logging


app = FastAPI()
logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
        ],
    )


@app.get("/health")
def health_check():
    """
    Healthy check to see if the application is working in a basic way
    """
    return {"status": "healthy"}


app.include_router(router)
