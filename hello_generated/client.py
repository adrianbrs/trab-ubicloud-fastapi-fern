# Importa o client do SDK gerado
from sdk import client

# Inicializa o client informando a URL em que a API está rodando
api = client.HelloWorldApi(base_url="http://localhost:8081")

# Chama o endpoint /hello/{name} através do método gerado a partir da
# especificação OpenAPI criada pelo FastAPI
res = api.hello("World", query="My query")

res_ping = api.utils.ping()

# Exibe a mensagem da resposta do servidor
print(f"Message: {res.message}")
print(f"Ping: {res_ping}")