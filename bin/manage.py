#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import traceback
sys.path.insert(0, '.')

from flask.ext.script import Manager, Shell, Server
from gematria_api import create_app
from gematria_api import codices

app = create_app()


def _make_context():
    return dict(app=app)

manager = Manager(app)
manager.add_command("shell", Shell(make_context=_make_context))
manager.add_command("runserver", Server(port=app.config['PORT']))


@manager.command
def english_codex_simple(phrase):
    """
    Invokes the simple English codex on phrase.

    :param phrase: Str
    """
    codex = codices.BaseCodex()
    print(codex.decode(phrase))


@manager.command
def english_codex(phrase):
    """
    Invokes the simple English codex on phrase.

    :param phrase: Str
    """
    codex = codices.EnglishCodex()
    print(codex.decode(phrase))


if __name__ == "__main__":
    # try:
    manager.run()
    # except Exception as e:
    #     ex_type, ex, tb = sys.exc_info()
    #     traceback.print_tb(tb)
    #     print("Error: %s" % e)
    #     print("Line: %d" % sys.exc_traceback.tb_lineno)
