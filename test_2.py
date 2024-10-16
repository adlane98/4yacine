import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from python_code import find_plant_info
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory = "static"), name = "static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request : Request):
    return templates.TemplateResponse("code.html", {"request" : request, "message" : None})

@app.post("/record")
async def record(request : Request, texte: str = Form(...)): 
    print(texte)
    response_message = find_plant_info(texte)
    print (response_message)
    return templates.TemplateResponse("code.html", {"request": request, "message" : response_message})
   

    


if __name__ == "__main__":
    uvicorn.run (app, host="127.0.0.1", port=8000)