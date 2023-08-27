# Text api server

FileKit API Server is a versatile tool designed to handle various file conversion and manipulation tasks. Built on top of the FastAPI framework, it offers a range of endpoints to cater to different file processing needs, from image background removal to PDF manipulations.

- Webpage: https://filekit.co/en/menu
- Front sourcecode: https://github.com/filekit-co/converto
- Swagger: https://api-file-xgnu4lf2ea-de.a.run.app/docs
- Image server: https://github.com/filekit-co/api-bg-remove/tree/main
- Vide server: https://github.com/filekit-co/api-video/tree/main

<div align='center'>
<table width="100%" border="0">
  <tr>
    <td><img width="1725" alt="Screen Shot 2023-08-27 at 11 58 14 AM" src="https://github.com/filekit-co/api-text/assets/37536298/02da3c07-811e-433b-ab93-087ed3d44cdd">
</td>
    <td><img width="861" alt="Screen Shot 2023-08-27 at 11 59 37 AM" src="https://github.com/filekit-co/api-text/assets/37536298/39de46c4-5755-4382-aec5-7fd84add6aad">
</td>
  </tr>
</table>
</div>

## Stack
- Pdf Process: [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)
- API Server: `fastapi`
- Cloud: `Google cloud run` / `Docker`

## Deploy

```bash
# develop
make dev 
# local docker
make up
```
# Features
## Image Processing:

### Background Removal:
- `POST /bg/remove`: Remove the background from an image sent within the request.
- `GET /bg/remove`: Remove the background from an image using a provided URL.
- `POST /images/convert`: Convert images to PNG format.

## File Conversion:

### Document Conversion:
Convert between various formats like EPUB, PDF, DOC, DOCX, and XPS. Specific routes include:
- `/epub-to-doc`
- `/pdf-to-doc`
- `/xps-to-doc`
- `/epub-to-docx`
- `/pdf-to-docx`
- `/xps-to-docx`

### PDF Conversion:
Convert different formats to PDF, including EPUB, XPS, OXPS, CBZ, and FB2. Specific routes include:
- `/xps-to-pdf`
- `/epub-to-pdf`
- `/oxps-to-pdf`
- `/cbz-to-pdf`
- `/fb2-to-pdf`

## Media Downloads:
- `POST /info`: Download target URL info.
- `POST /download/audio`: Download to audio format.
- `POST /download/video`: Download to video format.

## PDF Utilities:

### Encryption & Decryption:
- `POST /pdf/encrypt`: Encrypt a PDF file.
- `POST /pdf/decrypt`: Decrypt a PDF file.

### Watermark & Logo Addition:
- `POST /pdf/add-watermark`: Add a watermark to a PDF file.
- `POST /pdf/add-logo`: Add a logo to a PDF file.

### PDF Manipulation:
- `POST /pdf/merge`: Merge multiple PDFs into one.
- `POST /pdf/split`: Split a PDF into multiple files.
- `POST /pdf/compress`: Compress a PDF file.
