#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ilp - a tag based file indexer
#
# Author: slowpoke <mail+git@slowpoke.io>
#
# This program is Free Software under the non-terms
# of the Anti-License. Do whatever the fuck you want.

import pytest

from .. import funcset

ITEM1 = "foo"
ITEM2 = "bar"


def test_init():
    s = funcset((ITEM1, ITEM2))
    assert ITEM1 in s
    assert ITEM2 in s
    assert len(s) == 2


def test_add():
    s = funcset((ITEM1,))
    t = s.add(ITEM2)
    # a new object must have been created
    assert s is not t
    # the old object must not have been mutated
    assert ITEM1 in s
    assert ITEM2 not in s
    assert len(s) == 1
    # the new object must hold the old value...
    assert ITEM1 in t
    # ...as well as the new one
    assert ITEM2 in t
    assert len(t) == 2


def test_discard():
    s = funcset((ITEM1,))
    t = s.remove(ITEM1)
    # a new object must have been created
    assert s is not t
    # the old object must not have mutated
    assert ITEM1 in s
    assert len(s) == 1
    # the new object must be empty and not hold the removed key
    assert ITEM1 not in t
    assert len(t) == 0


def test_remove():
    # check that a non-existent key won't silently fail everything else is
    # already tested in test_discard()
    with pytest.raises(KeyError):
        funcset().remove(ITEM1)


def test_compare():
    s = funcset((ITEM1,))
    t = funcset((ITEM1,))
    assert s is not t
    assert s == t
    u = funcset((ITEM2,))
    assert s is not u
    assert s != u
