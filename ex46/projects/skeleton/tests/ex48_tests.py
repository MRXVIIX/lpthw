from nose.tools import *
from ex48 import lexiconcopy


def test_directions():
    assert_equal(lexiconcopy.scan("north"), [('direction', 'north')])
    result = lexiconcopy.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])

def test_verbs():
    assert_equal(lexiconcopy.scan("go"), [('verb', 'go')])
    result = lexiconcopy.scan("go kill eat")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat')])


def test_stops():
    assert_equal(lexiconcopy.scan("the"), [('stop', 'the')])
    result = lexiconcopy.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of')])


def test_nouns():
    assert_equal(lexiconcopy.scan("bear"), [('noun', 'bear')])
    result = lexiconcopy.scan("bear princess")
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'princess')])

def test_numbers():
    assert_equal(lexiconcopy.scan("1234"), [('number', 1234)])
    result = lexiconcopy.scan("3 91234")
    assert_equal(result, [('number', 3),
                          ('number', 91234)])


def test_nouns():
    assert_equal(lexiconcopy.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    result = lexiconcopy.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'IAS'),
                          ('noun', 'princess')])
