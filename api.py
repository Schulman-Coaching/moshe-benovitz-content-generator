"""
Rabbi Moshe Benovitz Content Generator API

FastAPI REST API for generating content in Rabbi Moshe Benovitz's voice.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os

from benovitz_content_generator import (
    ContentFormat,
    BenovitzVoiceProfile,
    generate_content_with_claude,
    generate_content_prompt_only,
    get_system_prompt,
    get_format_instructions
)

app = FastAPI(
    title="Rabbi Moshe Benovitz Content Generator API",
    description="Generate content in the distinctive voice of Rabbi Moshe Benovitz, NCSY International Managing Director",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GenerateRequest(BaseModel):
    topic: str
    format: str = "article"
    additional_context: Optional[str] = ""
    prompt_only: bool = False


class GenerateResponse(BaseModel):
    content: str
    format: str
    topic: str


class FormatInfo(BaseModel):
    name: str
    value: str
    description: str


@app.get("/")
async def root():
    """API root - returns basic info."""
    return {
        "name": "Rabbi Moshe Benovitz Content Generator API",
        "version": "1.0.0",
        "description": "Generate content in the voice of Rabbi Moshe Benovitz",
        "endpoints": {
            "/generate": "POST - Generate content",
            "/formats": "GET - List available formats",
            "/voice-profile": "GET - Get voice profile details",
            "/system-prompt": "GET - Get the full system prompt",
            "/health": "GET - Health check"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "benovitz-content-api"}


@app.get("/formats")
async def list_formats():
    """List all available content formats."""
    formats = [
        FormatInfo(
            name="Article/Essay",
            value="article",
            description="Long-form content (800-1200 words) with opening hook, Torah perspective, and practical application"
        ),
        FormatInfo(
            name="Social Media",
            value="social_media",
            description="Short-form posts for NCSY audience with hashtags"
        ),
        FormatInfo(
            name="Shiur Outline",
            value="shiur_outline",
            description="NCSY Kollel-style lecture outline with discussion questions"
        ),
        FormatInfo(
            name="Short Reflection",
            value="short_reflection",
            description="Brief daily wisdom (75-150 words)"
        ),
        FormatInfo(
            name="Advisor Training",
            value="advisor_training",
            description="Training content for NCSY advisors and Jewish educators"
        )
    ]
    return {"formats": formats}


@app.get("/voice-profile")
async def get_voice_profile():
    """Get the full voice profile for Rabbi Moshe Benovitz."""
    voice = BenovitzVoiceProfile()
    return {
        "name": voice.name,
        "tone": voice.tone.strip(),
        "style_patterns": voice.style_patterns.strip(),
        "themes": voice.themes.strip(),
        "influences": voice.influences.strip(),
        "hebrew_vocabulary": voice.hebrew_vocabulary.strip(),
        "transitions": voice.transitions.strip()
    }


@app.get("/system-prompt")
async def get_full_system_prompt():
    """Get the complete system prompt used for content generation."""
    voice = BenovitzVoiceProfile()
    return {
        "system_prompt": get_system_prompt(voice)
    }


@app.post("/generate", response_model=GenerateResponse)
async def generate_content(request: GenerateRequest):
    """Generate content in Rabbi Moshe Benovitz's voice."""

    # Validate format
    try:
        format_type = ContentFormat(request.format)
    except ValueError:
        valid_formats = [f.value for f in ContentFormat]
        raise HTTPException(
            status_code=400,
            detail=f"Invalid format '{request.format}'. Valid formats: {valid_formats}"
        )

    # Check for API key if not prompt_only
    if request.prompt_only:
        content = generate_content_prompt_only(
            topic=request.topic,
            format_type=format_type,
            additional_context=request.additional_context or ""
        )
    else:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise HTTPException(
                status_code=500,
                detail="ANTHROPIC_API_KEY not configured on server"
            )

        content = generate_content_with_claude(
            topic=request.topic,
            format_type=format_type,
            api_key=api_key,
            additional_context=request.additional_context or ""
        )

        if content.startswith("Error:"):
            raise HTTPException(status_code=500, detail=content)

    return GenerateResponse(
        content=content,
        format=request.format,
        topic=request.topic
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
