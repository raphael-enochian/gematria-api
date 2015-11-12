# -*- coding: utf-8 -*-
# Gematria-API (c) Raphael Enochian
from . import fixtures
from .helpers import GeneralTestCase
from gematria_api import codices
from nose.plugins.attrib import attr


class BaseCodexTestCase(GeneralTestCase):

    def setUp(self):
        super().setUp()
        self.codex = codices.BaseCodex()

    # @attr('single')
    def test_decode(self):
        '''
        Testing gematria_api.codices.BaseCodex.decode
        '''
        gematria = self.codex.decode(fixtures.typical_english_codex_phrase())
        self.assertEqual(gematria, 187, "Calculation performed correctly")


class EnglishCodexTestCase(GeneralTestCase):

    def setUp(self):
        super().setUp()
        self.codex = codices.EnglishCodex()

    # @attr('single')
    def test_decode(self):
        '''
        Testing gematria_api.codices.EnglishCodex.decode
        '''
        gematria = self.codex.decode(fixtures.typical_english_codex_phrase())
        self.assertEqual(gematria, 1122, "Calculation performed correctly")
