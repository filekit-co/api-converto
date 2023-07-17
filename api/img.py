# https://github.com/pymupdf/PyMuPDF/wiki/How-to-Convert-Images
# https://github.com/pymupdf/PyMuPDF-Utilities/tree/master/examples/convert-pixmap


# Input Formats	Output Formats	Description
# JPEG	-	Joint Photographic Experts Group
# BMP	-	Windows Bitmap
# JXR	-	JPEG Extended Range
# JPX	-	JPEG 2000
# GIF	-	Graphics Interchange Format
# TIFF	-	Tagged Image File Format
# PNG	PNG	Portable Network Graphics
# PNM	PNM	Portable Anymap
# PGM	PGM	Portable Graymap
# PBM	PBM	Portable Bitmap
# PPM	PPM	Portable Pixmap
# PAM	PAM	Portable Arbitrary Map
# -	PSD	Adobe Photoshop Document
# -	PS	Adobe Postscript

from typing import Annotated

from fastapi import APIRouter, File, Form, Response, UploadFile, status
from fastapi.responses import StreamingResponse

from consts import get_extension, get_mimetype
from infra.img import convert_img_type
from utils import content_disposition, generate_chunks, out_filename

router = APIRouter(prefix='/images', tags=["images"])


@router.post(
        path="/convert",
        summary="Convert images to png format",
        description="Valid input and out_types are ['png', 'pnm', 'pgm', 'ppm', 'pbm', 'pam', 'ps', 'jpg', 'jpeg']",
        status_code=status.HTTP_200_OK,
        )
async def convert(
        file: Annotated[UploadFile, File(...)],
        out_type: Annotated[str, Form()],
    ):

    with_leading_dot = '.' + out_type
    input_type = get_extension(file.content_type, exclude_leading_dot=False)
    filename = out_filename(file.filename, input_type, with_leading_dot)
    
    file_bytes = await file.read()
    out_bytes = convert_img_type(file_bytes, out_type)
    
    return StreamingResponse(
        content=generate_chunks(out_bytes),
        headers={
            'Content-Disposition': content_disposition(filename)
            },
        media_type=get_mimetype('.pdf'),
    )



#  TODO: https://pymupdf.readthedocs.io/en/latest/recipes-images.html
#  TODO: to webp
