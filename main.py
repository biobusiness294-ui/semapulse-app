
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
