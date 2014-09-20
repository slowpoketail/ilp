#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ilp - a tag based file indexer
#
# Author: slowpoke <mail+git@slowpoke.io>
#
# This program is Free Software under the non-terms
# of the Anti-License. Do whatever the fuck you want.

from .. import funcmap

KEY1 = "foo"
KEY2 = "spam"

VAL1 = "bar"
VAL2 = "baz"


def test_init():
    m = funcmap({KEY1: VAL1})
    # the key and value must be in the new object
    assert KEY1 in m.keys()
    assert VAL1 in m.values()
    assert m.get(KEY1) == VAL1
    # it must only contain one object
    assert len(m) == 1


def test_set():
    m = funcmap({KEY1: VAL1})
    n = m.set(KEY1, VAL2)
    # a new object must have been created
    assert m is not n
    # the old object must not have mutated
    assert m.get(KEY1) == VAL1
    # the new object must have the updated value
    assert n.get(KEY1) == VAL2


def test_remove():
    m = funcmap({KEY1: VAL1})
    n = m.remove(KEY1)
    # a new object must have been created
    assert m is not n
    # the old object must still have the old key/value
    assert m.get(KEY1) == VAL1
    # the new object must not have the key/value
    assert n.get(KEY1) is None
    # it must also be empty
    assert len(n) == 0


def test_compare():
    m = funcmap({KEY1: VAL1})
    n = funcmap({KEY1: VAL1})
    # check if two identical maps are not the same object, but compare equal
    assert m is not n
    assert m == n
    # check if another object with different content compares unequal
    o = funcmap({KEY2: VAL2})
    assert m is not o
    assert m != o
