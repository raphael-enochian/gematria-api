# -*- coding: utf-8 -*-
# Gematria-API (c) Raphael Enochian
from functools import reduce
from string import ascii_lowercase


class BaseCodex(object):
    """
    Represents a base codex object.
    """
    def __init__(self):
        self.table = {k: v for k, v in zip(ascii_lowercase, range(1, 27))}

    def decode(self, phrase):
        '''
        Decodes phrase into given codex using table

        :param phrase: A phrase to translate into Gematra
        :type phrase: str
        '''
        phrase = phrase.lower()
        gematria_map = (lambda table=self.table, phrase=phrase: [table.get(i) for i in phrase if table.get(i) is not None])()
        return reduce(lambda x, y: x+y, gematria_map)


class EnglishCodex(BaseCodex):
    """
    Represents Base6 English Gematria Codex
    """
    def __init__(self):
        self.table = {k: v for k, v in zip(ascii_lowercase, range(6, 157, 6))}
