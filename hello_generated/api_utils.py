from server.resources.utils.service import AbstractUtilsService

class UtilsService(AbstractUtilsService):
  def ping(self):
    return "pong"