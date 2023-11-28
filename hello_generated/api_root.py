from server.types.hello_response import HelloResponse
from server.service import AbstractRootService

class RootService(AbstractRootService):
  def hello(self, *, name: str, query: str | None = None) -> HelloResponse:
    return HelloResponse(message=f"Hello, {name}! ({query})")