# -*- coding: utf-8 -*-
# Gematria-API (c) Raphael Enochian


class BaseCodex(object):
    """
    Represents a base codex object.
    """
    pass


class EnglishCodex(BaseCodex):
    """
    Represents Base6 English Gematria Codex
    """
    def __init__(self):
        self.table = {'a': 6, 'b': 12, 'c': 18, 'd': 24, 'e': 30, 'f': 36, 'g': 42, 'h': 48, 'i': 54, 'j': 60, 'k': 66, 'l': 72, 'm': 78, 'n': 84, 'o': 90, 'p': 96, 'q': 102, 'r': 108, 's': 114, 't': 120, 'u': 126, 'v': 132, 'w': 138, 'x': 144, 'y': 150, 'z': 156}

    def decode(self, phrase):
        '''
        Takes an English phrase (word, noun, or phase) and returns the numerical Gematria representation of it.

        :param phrase:
        :type phrase: str
        '''
        pass
