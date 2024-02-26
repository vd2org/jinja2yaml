# Copyright (C) 2017-2024 by Vd.
# This file is part of jinja2yaml package.
# jinja2yaml is released under the MIT License (see LICENSE).
from tempfile import TemporaryDirectory

import pytest
from jinja2 import Environment, TemplateNotFound

from jinja2yaml import YamlLoader

CONTENT = """
home:
  welcome: |
    Welcome, {{username}}!
  goodbye: |
    Goodbye, {{username}}!
"""


def test_yamlloader_render():
    with TemporaryDirectory() as tmpdir:
        template_file = f'{tmpdir}/templates.yaml'
        with open(f'{tmpdir}/templates.yaml', 'w') as f:
            f.write(CONTENT)

        jinja = Environment(loader=YamlLoader(template_file))

        username = 'John Doe'
        template1 = jinja.get_template('home/welcome')
        rendered1 = template1.render(username=username)
        assert rendered1 == "Welcome, John Doe!"

        template2 = jinja.get_template('home/goodbye')
        rendered2 = template2.render(username=username)
        assert rendered2 == "Goodbye, John Doe!"


def test_yamlloader_not_found():
    with TemporaryDirectory() as tmpdir:
        template_file = f'{tmpdir}/templates.yaml'
        with open(f'{tmpdir}/templates.yaml', 'w') as f:
            f.write(CONTENT)

        jinja = Environment(loader=YamlLoader(template_file))

        with pytest.raises(TemplateNotFound):
            jinja.get_template('home/not_found')


def test_yamlloader_file_not_found():
    with TemporaryDirectory() as tmpdir:
        template_file = f'{tmpdir}/templates.yaml'

        jinja = Environment(loader=YamlLoader(template_file))

        with pytest.raises(FileNotFoundError):
            jinja.get_template('home/not_found')
