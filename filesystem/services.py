import mimetypes


def convert_size_to_mb_decimal(file_size: int):
    """Returns the size of the file in megabytes in base 10"""
    return round(float(file_size) / (1000.0 * 1000.0), 2)


def get_mime_type(file_name: str) -> str:
    """Returns the mime type of the file"""
    return mimetypes.guess_type(file_name)[0]
