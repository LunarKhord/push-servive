# main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
import aio_pika.abc
from aio_pika import connect_robust, Message
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connection logic for RabbitMQ
    logger.info("Initializing RabbitMQ Connection...")
    connection: aio_pika.abc.AbstractRobustConnection = await connect_robust("amqp://guest:guest@rabbitmq/")
    yield

# Create the app instance and pass the lifespan function directly
app = FastAPI(title="Push Service", lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Operational"}