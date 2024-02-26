# Copyright (C) 2017-2024 by Vd.
# This file is part of jinja2yaml package.
# jinja2yaml is released under the MIT License (see LICENSE).


from os.path import exists, getmtime

from jinja2 import BaseLoader, TemplateNotFound
from yaml import safe_load


class YamlLoader(BaseLoader):
    def __init__(self, path: str, separator: str = '/'):
        """\
        YamlLoader loads jinja2 templates from fields of yaml-file.
        This allows to keep all templates in one file. Useful when
        you have a large number of small templates. For example,
        strings for Telegram bots, etc.

        Supports autoreload in debug mode.

        :param path: path to yaml-file
        :param separator: fields separator

        :raises FileNotFoundError: if file not found
        :raises TemplateNotFound: if template not found
        """

        self.__path = path
        self.__separator = separator
        self.__data = dict()
        self.__mtime = None

    @property
    def separator(self) -> str:
        """

        :return: Using separator
        """
        return self.__separator

    @property
    def path(self) -> str:
        """

        :return: Using file path
        """
        return self.__path

    def get_source(self, environment, template):
        mtime = getmtime(self.path)
        if self.__mtime != mtime:
            self.__mtime = mtime
            if not exists(self.path):
                raise TemplateNotFound(template)
            with open(self.path, 'r') as f:
                self.__data = safe_load(f)

        source = self.__data
        for i in template.split(self.separator):
            if type(source) is not dict:
                raise TemplateNotFound(template)
            source = source.get(i)

        if type(source) is not str:
            raise TemplateNotFound(template)

        p = f"{self.path}:{template}"
        return source, p, lambda: mtime == getmtime(self.path)
