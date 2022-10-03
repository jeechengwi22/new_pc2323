import fastapi
from uvicorn import run

api = fastapi.FastAPI()

@api.get("/api/endpoint")
def endpoint():
    return {
            "msg": "Hello world!",
            "list of ports": [8000, 9000]
            }


run(api)
