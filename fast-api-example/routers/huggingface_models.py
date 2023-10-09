

from pydantic import BaseModel, Field


class TextClassificationRequest(BaseModel):
    text: str = Field(default=None, max_length=1000, min_length=3)