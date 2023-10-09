from pydantic import BaseModel, field_validator, Field

class CreateUser(BaseModel):
    firstname: str = Field(default=None, max_length=50, min_length=3)
    lastname: str = Field(default=None, max_length=50, min_length=3)

    @field_validator('firstname')
    @classmethod
    def check_for_whitespace(cls, firstname: str) -> str:
        if ' ' in firstname:
            raise ValueError("Can't contain space")
        return firstname.title()