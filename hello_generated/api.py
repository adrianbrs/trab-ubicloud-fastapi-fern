from fastapi import FastAPI
from server.register import register
import api_root
import api_utils

app = FastAPI()

register(app, root=api_root.RootService(), utils=api_utils.UtilsService())