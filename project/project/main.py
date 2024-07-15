from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
import cohere
import os
from dotenv import load_dotenv
from pydantic import BaseModel


load_dotenv()

co = cohere.Client(api_key=os.getenv("API_KEY"))

app = FastAPI()

message = """
    "## Instructions\n"
    "1. Error Detection: Identify any errors or bugs in the code. These could be syntax errors, runtime errors, or logical errors that could cause the code to malfunction or produce incorrect results."
    "2. Bug Identification: Highlight specific bugs and provide detailed explanations of what causes them and how they can be fixed. Include examples if possible."
    "3. Code Improvement: Suggest better ways to write the code. This could involve refactoring for readability, performance optimization, adherence to best practices, or using more efficient algorithms and data structures."
    "4. Reasoning: Provide clear reasoning behind each suggestion. Explain why a particular approach is better, how it improves the code, and any potential trade-offs or implications."

    ## Input Text
    {message}
"""

class InputText(BaseModel):
    message: str

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/review/")
async def review_code(input_text:InputText):
    try:
        response = co.chat(
            message=input_text.message,
            model="command-r-plus",
            temperature=0.3
        )
        return JSONResponse(response.text)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)