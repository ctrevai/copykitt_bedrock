from fastapi import FastAPI
from copykitt import generate_branding_snippet, generate_keywords
from fastapi import HTTPException

app = FastAPI()

MAX_KEYWORD_LENGTH = 32

@app.get("/")
async def root():
    return {"message": "Hello CopyKitt"}

@app.get("/generate-snippet")
async def generate_snippet_api(prompt: str):
    validate_input_lenght(prompt)
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet, "keywords": []}

@app.get("/generate-keywords")
async def generate_keywords_api(prompt: str):
    validate_input_lenght(prompt)
    keywords = generate_keywords(prompt)
    return {"snippet": None, "keywords": keywords}

@app.get("/generate-snippet-and-keywords")
async def generate_snippet_and_keywords_api(prompt: str):
    validate_input_lenght(prompt)
    snippet = generate_branding_snippet(prompt)
    keywords = generate_keywords(prompt)
    return {"snippet": snippet, "keywords": keywords}


def validate_input_lenght(prompt: str):
    if len(prompt) > MAX_KEYWORD_LENGTH:
        raise HTTPException(
            status_code=400, 
            detail=f"Input too long. Must be under {MAX_KEYWORD_LENGTH} charactors"
            )
    return True

#uvicorn copykitt_api:app --reload