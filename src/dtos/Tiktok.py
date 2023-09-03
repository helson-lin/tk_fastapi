from pydantic import BaseModel


class TikTikDto(BaseModel):
    url: str
