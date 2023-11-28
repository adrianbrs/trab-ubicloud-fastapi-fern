from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.routing import APIRoute

# Define uma função que será utilizada para gerar o ID único
# de cada rota. Por padrão, o FastAPI utiliza o nome da função,
# o path e o método HTTP para gerar o ID único.
def custom_generate_unique_id(route: APIRoute):
  if len(route.tags) == 0:
    return f"{route.name}"
  return f"{route.tags[0]}-{route.name}"

app = FastAPI(generate_unique_id_function=custom_generate_unique_id)

class HelloResponse(BaseModel):
  message: str

# Define uma rota simples de exemplo
# O argumento response_model define o modelo de resposta
@app.get("/hello/{name}", response_model=HelloResponse)
def hello(name: str, query: str | None = None):
  return {
    "message": f"Hello, {name}! ({query})"
  }

# Utilizando tags, é possível agrupar as rotas dentro de
# um escopo separado na hora de gerar o SDK
@app.get("/ping", tags=["utils"])
def ping():
  return "pong"