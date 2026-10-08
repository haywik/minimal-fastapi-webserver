from fastapi import FastAPI, Request, HTTPException, status, Response
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import re
import os
from datetime import datetime

start_time = datetime.now()

app = FastAPI()

base = Path(__file__).parent
TEMPLATES_DIR = base / "templates"

tpl = Jinja2Templates(directory=str(TEMPLATES_DIR))
app.mount("/static", StaticFiles(directory=str(base / "static")), name="static")


@app.get("/")
async def index(request: Request):
    return RedirectResponse(url="/home")

@app.get("/status-b")
async def status_b(request: Request):
    uptime = str(datetime.now() - start_time)
    uptime = uptime[:uptime.index(".")]
    return {"name":"central.haywik.com","alive":True,"uptime":uptime}

@app.get("/{path:path}")
async def serve_page(request: Request, path: str):
    if not re.fullmatch(r'[a-zA-Z0-9_\-/]+', path) or ".." in path:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    template_path = path + ".html"
    full_path = TEMPLATES_DIR / template_path

    if not full_path.is_file() or not full_path.resolve().is_relative_to(TEMPLATES_DIR.resolve()):
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    return tpl.TemplateResponse(request, template_path)
