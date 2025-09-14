from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="SemaPulse API",
    version="0.1.0",
    description="Semantic Innovation Engine - Explore SemaPulse capabilities across disciplines."
)

templates = Jinja2Templates(directory="templates")

# Route pour l'interface HTML
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Bienvenue sur SemaPulse"})

# Endpoint pour générer recommandations
@app.post("/recommandation", response_class=HTMLResponse)
async def recommandations(request: Request, concept: str = Form(...)):
    data = ["Idée 1", "Idée 2", "Idée 3"]  # Exemple, à remplacer par votre logique
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "message": f"Recommandations pour '{concept}'", "recommandations": data}
    )

# Endpoint API pour les domaines
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

# Endpoint API exemple
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}, welcome to SemaPulse 🌍"}
