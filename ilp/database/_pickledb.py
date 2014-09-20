#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Kirschwasser - a tag based file indexer
#
# Author: slowpoke <mail+git@slowpoke.io>
#
# This program is Free Software under the non-terms
# of the Anti-License. Do whatever the fuck you want.

import pickle
from . import DictDB


class PickleDB(DictDB):

    """A very basic database that uses a pickled dict as backend.

    Note that this is horribly inefficent and should never be used seriously
    anywhere ever - this is purely meant for testing purposes.

    """

    def __init__(self, path):
        super().__init__()
        self._path = path
        self._load()

    def _put(self, key, value):
        super()._put(key, value)
        self._write()

    def _del(self, key):
        super()._del(key)
        self._write()

    def _write(self):
        with open(self._path, "wb") as f:
            pickle.dump(self._storage, f)

    def _load(self):
        with open(self._path, "rb") as f:
            self._storage = pickle.load(f)
