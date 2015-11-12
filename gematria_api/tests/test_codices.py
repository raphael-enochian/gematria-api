# -*- coding: utf-8 -*-
# Gematria-API (c) Raphael Enochian
from . import fixtures
from .helpers import GeneralTestCase
from gematria_api import codices
from nose.plugins.attrib import attr


class BaseCodexTestCase(GeneralTestCase):

    def setUp(self):
        super().setUp()
        self.base_codex = codices.BaseCodex()

    @attr('single')
    def test_decode(self):
        '''
        Testing gematria_api.codices.EnglishCodex
        '''
        gematria = self.base_codex.decode(fixtures.typical_english_codex_phrase())
        self.assertEqual(gematria, 187, "Calculation performed correctly")
