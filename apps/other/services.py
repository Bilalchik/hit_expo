import os
from datetime import datetime


def get_upload_path(instance, filename):
    return os.path.join('other/images/', datetime.now().date().strftime("%Y/%m/%d"), filename)
