from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
import pytest_asyncio
from app.config import settings
from httpx import ASGITransport, AsyncClient
from app.main import app as fastapi_app
from app.utils.mock import mock_script

@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_db():
    assert settings.MODE == "TEST"
    await mock_script()
    
    
@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_redis():
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="cache")   
    
@pytest_asyncio.fixture(scope="function")
async def ac():
    async with AsyncClient(transport=ASGITransport(fastapi_app), base_url="http://test") as ac:
        yield ac
    