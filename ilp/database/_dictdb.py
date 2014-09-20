#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Kirschwasser - a tag based file indexer
#
# Author: slowpoke <mail+git@slowpoke.io>
#
# This program is Free Software under the non-terms
# of the Anti-License. Do whatever the fuck you want.

from . import API


class DictDB(API):

    """A volatile database that uses a dict as a backend.

    This is meant mostly for testing purposes. Shouldn't be used in production.

    """

    def __init__(self):
        self._storage = dict()

    def _put(self, key, value):
        self._storage[key] = value

    def _get(self, key):
        return self._storage[key]

    def _del(self, key):
        del self._storage[key]

    def __contains__(self, key):
        return key in self._storage
