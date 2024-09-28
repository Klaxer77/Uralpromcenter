from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from app.products.router import router as product_router
from app.news.router import router as news_router
from app.users.router import router_auth as auth_user_router
from app.recall.router import router as recall_router
from app.progress.router import router as progress_router
from app.email.order_call.router import router as ordercall_router
from app.email.send_request.router import router as sendrequest_router
from app.products.categories.router import router as categories_router
from sqladmin import Admin
from app.database import engine
from app.admin.auth import authentication_backend
from app.admin.views import OrderCallAdmin, ProgressAdmin, RecallAdmin, SendRequestAdmin, UsersAdmin, CategoriesAdmin, NewsAdmin, ProductsAdmin
from app.config import settings
from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from app.utils.limiter import limiter
import sentry_sdk
from fastapi_pagination import add_pagination

openapi_url=None
redoc_url=None

if settings.MODE in ["DEV","TEST"]:
    openapi_url="/openapi.json"
    redoc_url="/redoc"

if settings.MODE == "PROD":
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        traces_sample_rate=1.0,
        profiles_sample_rate=1.0,
    )


app = FastAPI(
    title="Сайт ASK-BP",
    openapi_url=openapi_url, 
    redoc_url=redoc_url
    )
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
add_pagination(app)

app.include_router(product_router)
app.include_router(categories_router)
app.include_router(news_router)
app.include_router(recall_router)
app.include_router(progress_router)
app.include_router(ordercall_router)
app.include_router(sendrequest_router)
app.include_router(auth_user_router)

origins = [
    "http://localhost:3001",
    "http://localhost:3000",
    "ws://localhost:3001",
    "ws://localhost:3000",
]

#Подключение CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", 
                   "Access-Control-Allow-Origin",
                   "Authorization"],
)

if settings.MODE == "TEST":
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="cache")

@app.on_event("startup")
def startup():
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="cache")
    
# Подключение Прометеуса
instrumentator = Instrumentator(
    should_group_status_codes=False,
    excluded_handlers=[".*admin.*", "/metrics"],
)
instrumentator.instrument(app).expose(app)

# Подключение админки
admin = Admin(app, engine, authentication_backend=authentication_backend)
admin.add_view(UsersAdmin)
admin.add_view(ProductsAdmin)
admin.add_view(CategoriesAdmin)
admin.add_view(NewsAdmin)
admin.add_view(RecallAdmin)
admin.add_view(ProgressAdmin)
admin.add_view(SendRequestAdmin)
admin.add_view(OrderCallAdmin)
