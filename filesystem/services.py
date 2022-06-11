import mimetypes


def get_mimetype(filename:str) -> str:
    """Returns mimetype from filename"""
    mime = mimetypes.guess_type(filename)[0]
    if mime is None:
        return ''
    return mime
