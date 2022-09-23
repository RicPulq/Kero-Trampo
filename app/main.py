import logging
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from app import api
from typing import List
from app import core, util, db

if core.settings.DEBUG:
    app = FastAPI(title=core.settings.PROJECT_NAME, swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})
else:
    app = FastAPI(docs_url=None, redocs_url=None, openapi_url=None)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api.routers, prefix=core.settings.API_URL_PREFIX)
