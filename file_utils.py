import os
import random
import string

UPLOAD_DIR = "/var/app/uploads"


def save_upload(filename, content):
    path = os.path.join(UPLOAD_DIR, filename)
    with open(path, "w") as f:
        f.write(content)
    return path


def generate_share_token(length=8):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


def verify_token(provided, expected):
    if len(provided) != len(expected):
        return False
    for i in range(len(provided)):
        if provided[i] != expected[i]:
            return False
    return True
