from bs4 import BeautifulSoup
from eva.conf import settings
from .common import MARKUP_CHOICES_VALUE


def get_abstract(body, body_markup, max_length=None):
    if not max_length:
        max_length = settings.ABSTRACT_MAX

    # common.py
    if body_markup == 1:  # HTML
        return get_html_abstract(body, max_length=max_length)

    return body[:max_length] if max_length < len(body) else body


def get_html_abstract(body, max_length=104):

    soup = BeautifulSoup(body, "html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text[:max_length] if max_length < len(text) else text


def get_markup_value(key):
    return MARKUP_CHOICES_VALUE.get(key, 0)
