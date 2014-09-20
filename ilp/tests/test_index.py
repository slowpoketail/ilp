#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ilp - a tag based file indexer
#
# Author: slowpoke <mail+git@slowpoke.io>
#
# This program is Free Software under the non-terms
# of the Anti-License. Do whatever the fuck you want.

import sys

from .. import Index

from hashlib import sha1

SAMPLE_HASH = sha1(b"Heliocentrism!").digest()
SAMPLE_PATH = "books/systema_cosmicum.epub"
SAMPLE_TAG = "heresy"

def test_add_file():
    i = Index()
    j = i.add_file(SAMPLE_PATH, SAMPLE_HASH)
    assert i is not j
    assert i != j
    assert SAMPLE_PATH not in i.files
    assert SAMPLE_PATH in j.files

def test_remove_file():
    i = Index().add_file(SAMPLE_PATH, SAMPLE_HASH)
    j = i.remove_file(SAMPLE_PATH)
    assert i is not j
    assert i != j
    assert SAMPLE_PATH in i.files
    assert SAMPLE_PATH not in j.files

def test_add_tag():
    i = Index()
    j = i.add_tag(SAMPLE_TAG)
    assert i is not j
    assert i != j
    assert SAMPLE_TAG not in i.tags
    assert SAMPLE_TAG in j.tags

def test_remove_tag():
    i = Index().add_tag(SAMPLE_TAG)
    j = i.remove_tag(SAMPLE_TAG)
    assert i is not j
    assert i != j
    assert SAMPLE_TAG in i.tags
    assert SAMPLE_TAG not in j.tags

def test_tag_file():
    i = Index().add_file(SAMPLE_PATH, SAMPLE_HASH).add_tag(SAMPLE_TAG)
    j = i.tag_file(SAMPLE_PATH, SAMPLE_TAG)
    assert i is not j
    assert i != j
    assert not i.file_has_tag(SAMPLE_PATH, SAMPLE_TAG)
    assert j.file_has_tag(SAMPLE_PATH, SAMPLE_TAG)

def test_untag_file():
    i = Index().add_file(
        SAMPLE_PATH, SAMPLE_HASH).add_tag(
            SAMPLE_TAG).tag_file(SAMPLE_PATH, SAMPLE_TAG)
    j = i.untag_file(SAMPLE_PATH, SAMPLE_TAG)
    assert i is not j
    assert i != j
    assert i.file_has_tag(SAMPLE_PATH, SAMPLE_TAG)
    assert not j.file_has_tag(SAMPLE_PATH, SAMPLE_TAG)

def test_tags_of_file():
    i = Index().add_file(
        SAMPLE_PATH, SAMPLE_HASH).add_tag(
            SAMPLE_TAG).tag_file(SAMPLE_PATH, SAMPLE_TAG)
    assert i.tags_of_file(SAMPLE_PATH) == {SAMPLE_TAG, }
