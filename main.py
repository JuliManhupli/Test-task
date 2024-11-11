from fastapi import FastAPI, HTTPException

from src.conf.config import settings
from src.routes import benchmarking_result

app = FastAPI()

if settings.DEBUG:
    app.include_router(benchmarking_result.router)
else:
    @app.get("/")
    def not_ready_yet():
        raise HTTPException(status_code=503, detail="Feature not ready for live yet")
