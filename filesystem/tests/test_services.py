from filesystem.services import convert_size_to_mb_decimal, get_mime_type


def test_convert_size_to_mb_decimal():
    """Test conversion from bytes to Megabytes"""
    size_in_bytes: int = 1000000
    size_in_megabytes: float = 1.0
    assert size_in_megabytes == convert_size_to_mb_decimal(size_in_bytes)


def test_get_mime_from_filename():
    """Test retrieving mime from get_mime_type"""
    filename: str = "Hound of the Baskervilles.pdf"
    expected_mime: str = "application/pdf"
    assert expected_mime == get_mime_type(filename)
