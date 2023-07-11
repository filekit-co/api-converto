import io
import zipfile
from typing import List


async def zip_files(files: List[bytes], file_names: List[str]) -> bytes:
    # Create a zip file in memory
    with io.BytesIO() as zip_buffer:
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for i, f in enumerate(files):
                # Add each file to the zip
                zip_file.writestr(f'{file_names[i]}.pdf', f)

        # Prepare the response with zip file data
        return zip_buffer.getvalue()
