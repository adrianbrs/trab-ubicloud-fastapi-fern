from fastapi import FastAPI
app = FastAPI()

@app.get("/hello/{name}")
def hello(name: str, query: str | None = None):
  return {
    "message": f"Hello, {name}! Query: {query}"
  }