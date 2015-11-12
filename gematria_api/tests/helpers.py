# -*- coding: utf-8 -*-
# Gematria-API (c) Raphael Enochian

from flask.ext.testing import TestCase
from flask import current_app


class GeneralTestCase(TestCase):
    def create_app(self):
        """
        Create a Flask app for testing.
        """

        from gematria_api import create_app
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        return self.app

    def setUp(self):
        """
        Prepare for a test case.
        """
        pass

    def tearDown(self):
        """
        Clean up after a test case.
        """
        pass
