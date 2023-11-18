import os.path
import sys
from urllib.parse import urlparse

import validators


class Validator:
    def __init__(self, data):
        self.data = data

    def validate(self):
        self.validate_link()
        self.validate_directory()

    def validate_link(self):
        validation = validators.url(self.data["link"])
        if validation:
            domain = urlparse(self.data["link"]).netloc
            if domain == "music.youtube.com" or domain == "www.youtube.com":
                pass
            else:
                print("Link is not valid")
                print('Enter playlist link from "YouTube Music" or "YouTube"')
                sys.exit(0)
        else:
            print("Link is not valid")
            sys.exit(0)

    def validate_directory(self):
        is_exists = os.path.exists(self.data["directory"])
        if not is_exists:
            print("Directory is not exists, creating...")
            os.makedirs(self.data["directory"])
            print("New directory created")