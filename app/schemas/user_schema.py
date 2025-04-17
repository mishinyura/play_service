from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    message: str

    class Config:
        from_attributes = True


class UserRequestSchema(BaseModel):
    message: str
