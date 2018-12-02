# -*- coding: utf-8 -*-
import re
from typing import Optional


def clean(_text: str) -> Optional[str]:
    _text = remove_br(_text.expandtabs(1))
    _text = remove_url(_text).strip()
    _text = re.sub(r'\s+', ' ', _text, flags=re.MULTILINE)
    return _text if _text != '' else None


def remove_br(_text: str) -> str:
    return re.sub(r'\n+', ' ', _text, flags=re.MULTILINE)


def remove_url(_text: str) -> str:
    """Reference:
    http://www.noah.org/wiki/RegEx_Python#URL_regex_pattern
    """
    _text = re.sub(r'http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', _text,
                   flags=re.MULTILINE)
    _text = re.sub(r'\s+$', '', _text, flags=re.MULTILINE)
    return _text
