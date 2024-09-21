from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.products.router import router as product_router
from app.news.router import router as news_router
from app.users.router import router_auth as auth_user_router
from app.recall.router import router as recall_router
from app.progress.router import router as progress_router
from app.email.order_call.router import router as ordercall_router
from app.email.send_request.router import router as sendrequest_router
from sqladmin import Admin
from app.database import engine
from app.admin.auth import authentication_backend
from app.admin.views import OrderCallAdmin, ProgressAdmin, RecallAdmin, SendRequestAdmin, UsersAdmin, CategoriesAdmin, NewsAdmin, ProductsAdmin
from app.config import settings
from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

openapi_url=None
redoc_url=None

if settings.MODE in ["DEV","TEST"]:
    openapi_url="/openapi.json"
    redoc_url="/redoc"

app = FastAPI(
    title="Сайт ASK-BP",
    root_path="/api",
    openapi_url=openapi_url, 
    redoc_url=redoc_url
    )

app.include_router(product_router)
app.include_router(news_router)
app.include_router(recall_router)
app.include_router(progress_router)
app.include_router(ordercall_router)
app.include_router(sendrequest_router)
app.include_router(auth_user_router)

origins = [
    "http://localhost:3000",
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
