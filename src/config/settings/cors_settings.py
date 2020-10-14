import json
from config.settings.config import PATTERNS_DIR
from urllib.parse import urlparse


def get_allowed_urls():
    with open(PATTERNS_DIR) as f:
        data = json.load(f)
    urls = []
    for item in data:
        url = urlparse(item['url_pattern'])
        url = '{uri.scheme}://{uri.netloc}'.format(uri=url)
        urls.append(url)
    return urls


