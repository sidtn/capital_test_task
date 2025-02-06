from pydantic import BaseModel


class StringSchema(BaseModel):
    value: str | int
