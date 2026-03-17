import os
from urllib.parse import urlparse


def get_extension_from_url(url: str, default: str = ".jpg") -> str:
    path = urlparse(url).path
    ext = os.path.splitext(path)[1].lower()
    return ext if ext else default
