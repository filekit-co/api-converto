import fitz

valid_formats = {"png": 1, "pnm": 2, "pgm": 2, "ppm": 2, "pbm": 2, "pam": 3, "psd": 5, "ps": 6, "jpg": 7, "jpeg": 7}


def convert_img_type(file_bytes: bytes, out_type: str):
    idx = valid_formats.get(out_type.lower(), None) 
    
    pix = fitz.Pixmap(file_bytes)
    if pix.alpha and idx in (2,6,7):
        pix = fitz.Pixmap(pix,0)
    
    return pix.tobytes(out_type)
    