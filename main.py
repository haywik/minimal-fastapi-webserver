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

parent_directory = Path(__file__).parent #Stores the aboslute directory the parent folder is, realtive to it self.
public_directory = parent_directory / "public" # Tells fastapi to only read HMTL files from the absolute directory they should be in.
#static_files = parent_directory / "public"

templates = Jinja2Templates(directory="public/html") #Defind to Jinja2 where the HTML files are stored
app.mount("/css", StaticFiles(directory="public/css"), name="css") 
app.mount("/js", StaticFiles(directory="public/js"), name="js")
app.mount("/img", StaticFiles(directory="public/img"), name="img")

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
#    if not re.fullmatch(r'[a-zA-Z0-9_\-/]+', path) or ".." in path: #If the requested path contains non letter,number or /, it will void a request.
#        return Response(status_code=status.HTTP_404_NOT_FOUND)
#
#    if not (html_files/path).is_file() or not path.resolve().is_relative_to(html_files.resolve()):
#        return Response(status_code=status.HTTP_404_NOT_FOUND)

    path=path.replace(".html","")+".html"
    print("Template ",f"{public_directory}/{path}"," Was requested.")


    if (public_directory/ "html" / path).is_file():
        return templates.TemplateResponse(request, path)
    else:
        return templates.TemplateResponse(request, "codes/404.html", status_code=404)
