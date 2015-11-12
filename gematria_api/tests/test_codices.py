# -*- coding: utf-8 -*-
# Gematria-API (c) Raphael Enochian
from . import fixtures
from .helpers import GeneralTestCase
from nose.plugins.attrib import attr
from gematria_api import codices


class EnglishCodexTestCase(GeneralTestCase):

    def setUp(self):
        super().setUp()
        self.english_codex = codices.EnglishCodex()

    @attr('single')
    def test_decode(self):
        '''
        Testing gematria_api.codices.EnglishCodex
        '''
        fixtures.typical_english_codex_phrase()
        pass
