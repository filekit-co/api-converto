import mimetypes
from functools import lru_cache

mimetypes.init()

@lru_cache
def get_mimetype(ext: str):
    """ext example .doc .docx"""
    return mimetypes.types_map.get(ext)

@lru_cache
def get_extension(mime_type: str, exclude_leading_dot=True):
    result = mimetypes.guess_extension(mime_type)
    
    if exclude_leading_dot:
        return result[1:]
    return result