import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG = {
    "AUTHORIZED_FACES_DIR": os.path.join(BASE_DIR, "data/authorized_face"),
    "LOG_DIR": os.path.join(BASE_DIR, "data/logs"),
    "TEMP_IMAGE": os.path.join(BASE_DIR, "data/temp_image.jpg"),
    "MATCH_THRESHOLD": 0.6
}
