from pydantic import BaseModel

class File(BaseModel):
    parent_dir: str
    filename: str
    full_path: str

class LanguageSummary(BaseModel):
    lines: int
    blank: int