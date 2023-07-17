import urllib.parse
from typing import AsyncIterator

_CHUNK_SIZE = 10 * 1024 * 1024 # 10MB

def out_filename(input_file_name:str, input_type:str, output_type:str)-> str:
    return f'{input_file_name[0:-len(input_type)]}{output_type}'

def content_disposition(filename):
    filename = urllib.parse.quote(filename)
    return f"attachment; filename*=UTF-8''{filename}"

# Chunk size 
async def generate_chunks(out_bytes, chunk_size=_CHUNK_SIZE)-> AsyncIterator[bytes]:
    index = 0
    while index < len(out_bytes):
        chunk = out_bytes[index : index + chunk_size]
        index += chunk_size
        yield chunk