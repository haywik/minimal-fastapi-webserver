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
parent_name=(str(parent_directory)[::-1])[0:(str(parent_directory)[::-1]).index("/")][::-1] #Looks scary but, gets the parent directory, flips it, find the first "/", removes everything after it, the re flips it, giving the parent name
public_directory = parent_directory / "public" # Tells fastapi to only read HMTL files from the absolute directory they should be in.


templates = Jinja2Templates(directory="public/html") #Defind to Jinja2 where the HTML files are stored
app.mount("/css", StaticFiles(directory="public/css"), name="css") # Sets up a mounts, so any requests that begin with "css" will be safely served 
app.mount("/js", StaticFiles(directory="public/js"), name="js")  #
app.mount("/img", StaticFiles(directory="public/img"), name="img") #

@app.get("/")
async def index(request: Request): #If someone goes to the / (root) of the web page they are redirect to /home,
    return RedirectResponse(url="/home") # | this not not needed, if not make sure to have the server redirect any / to home.html (or index.html your choice)

@app.get("/status") #A simple status page path
async def status(request: Request):
    uptime = str(datetime.now() - start_time)
    uptime = uptime[:uptime.index(".")]
    return {"name":f"{__file__.parent}","uptime":uptime}  #returns the, parent name, which is assumed to be the name of the domain, and the uptime since script start.

@app.get("/{path:path}") # path:path allows for traversal path serving
async def traversalPageServe(request: Request, path: str): 
    path=path.replace(".html","")+".html"     #you may put example.com/home or /home.html so we assume there is a html and remove it anyway and readd it.
    if (public_directory/ "html" / path).is_file():  #Uses the absolute directory location eg /home/haywik/example.com/public/html/home.html,
        return templates.TemplateResponse(request, path) #| if the file does exist, it will return said file
    return templates.TemplateResponse(request, "codes/404.html", status_code=404) # If anything else happend, it will throw a 404 (file not found error)
