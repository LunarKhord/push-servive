from contextlib import asynccontextmanager
from fastapi import FastAPI
import aio_pika.abc
from aio_pika import connect_robust, Message
import logging
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Attempt to connect to RabitMQ")
    try:
        connection: aio_pika.abc.AbstractRobustConnection = await connect_robust("amqp://guest:guest@rabbitmq/")
    except Exception as RabbitMQExp:
        logger.error(f"Could not connect to rabbitmq: {RabbitMQExp}")

    yield

    
app = FastAPI(title="Push Service", lifespan=lifespan)