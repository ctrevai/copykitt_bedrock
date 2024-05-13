from fastapi import FastAPI
from copykitt import generate_branding_snippet, generate_keywords
from fastapi import HTTPException
from mangum import Mangum
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
handler = Mangum(app)

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
            detail=f"Input too long. Must be under {
                MAX_KEYWORD_LENGTH} charactors"
        )
    return True

# show openapi.json in lambda


@app.get("/docs", include_in_schema=False)
async def get_documentation():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="CopyKitt API")


@app.get("/openapi.json", include_in_schema=False)
async def access_openapi():
    return get_openapi(title=app.title, version=app.version, routes=app.routes)
    # openapi = get_openapi(
    #     title=app.title,
    #     version=app.version,
    #     description=app.description,
    #     routes=app.routes,
    #     tags=app.openapi_tags,
    # )
    # openapi["servers"] = [{"url": app.root_path}]
    # return openapi
# uvicorn copykitt_api:app --reload
