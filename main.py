from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Bienvenue sur SemaPulse"})

# Exemple d'endpoint pour les recommandations
@app.post("/recommandation", response_class=HTMLResponse)
async def recommandations(request: Request, concept: str = Form(...)):
    # Ici, vous pouvez générer de vraies recommandations
    data = ["Idée 1", "Idée 2", "Idée 3"]
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "message": f"Recommandations pour '{concept}'", "recommandations": data}
    )

from fastapi import FastAPI

app = FastAPI(
    title="SemaPulse API",
    version="0.1.0",
    description="Semantic Innovation Engine - Explore SemaPulse capabilities across disciplines."
)

@app.get("/")
def read_root():
    return {"message": "Hello from SemaPulse 🚀"}

@app.get("/domains")
def get_domains():
    domains = [
        "Artificial Intelligence",
        "Medicine",
        "Biology",
        "Geopolitics",
        "Business Strategy",
        "Education",
        "Climate Science",
        "Law and Ethics",
        "Energy and Sustainability",
        "Social Sciences",
        "Neuroscience",
        "Robotics",
        "Agriculture",
        "Economics",
        "Psychology",
        "Engineering",
        "Nanotechnology",
        "Philosophy",
        "Astronomy",
        "Cognitive Science"
    ]
    return {"domains": domains}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}, welcome to SemaPulse 🌍"}
