import os

from datetime import datetime


def get_upload_path(instance, filename):
    return os.path.join('investor/images/', datetime.now().date().strftime("%Y/%m/%d"), filename)
