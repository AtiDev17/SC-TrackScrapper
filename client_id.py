import re

import requests

BUNDLE_URL = "https://a-v2.sndcdn.com/assets/55-f1b8682b.js"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    ),
}


def create_session():
    session = requests.Session()
    session.headers.update(HEADERS)
    return session


def get_client_id():
    response = requests.get(BUNDLE_URL, headers=HEADERS, timeout=30)
    response.raise_for_status()
    return re.search(r'client_id:"([0-9a-zA-Z]{32})"', response.text).group(1)
