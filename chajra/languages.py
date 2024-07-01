from pydantic import BaseModel, ConfigDict, ValidationError
from typing import List
from chajra.extensions import extensions_db
import logging

class Language(BaseModel):
    model_config = ConfigDict(strict=True)

    name: str
    type: str
    extensions: List[str] = []

try:
    ALL = list(map(Language.model_validate, extensions_db))
except ValidationError as ve:
    logging.critical("Internal Error: Invalid extensions list.")
    exit(1)

_supported_languages = [l.name for l in ALL]

_supported_extensions = []
for l in ALL:
    _supported_extensions += l.extensions
    
_supported_extensions_set = set(_supported_extensions)

def is_supported(ext):
    return ext in _supported_extensions_set

_reverse_languages_dict = dict()
for l in ALL:
    for ext in l.extensions:
        _reverse_languages_dict[ext] = l.name

def get_language_name(ext: str) -> str:
    return _reverse_languages_dict.get(ext)
