# -*- coding: utf-8 -*-
import os
from typing import List, Union

import MeCab

from salad.utils.class_utils import Singleton
from salad.utils.string_utils import clean


class Tokenizer(metaclass=Singleton):
    def __init__(self):
        dic_path = os.environ.get('MECAB_DICDIR')
        self.tagger = MeCab.Tagger(f'-d {dic_path}') if dic_path else MeCab.Tagger()

    def parse(self, text: str, joined=True, lowered=False) -> Union[str, List[str]]:
        cleaned_text = clean(text)
        words = []
        if cleaned_text:
            for chunk in self.tagger.parse(cleaned_text).splitlines()[:-1]:
                if chunk != '':
                    (surface, feature) = chunk.split('\t')
                    if lowered:
                        surface = surface.lower()
                    words.append(surface)
        if joined:
            return ' '.join(words)
        else:
            return words
