from nose.tools import *
from ex49.ex49 import *

def test_parse_sentence():
    sentence = parse_sentence([('noun', 'bear'), ('verb', 'eats'), ('noun', 'honey')])
    assert_equal(sentence.subject, 'bear')
    assert_equal(sentence.verb, 'eats')
    assert_equal(sentence.object, 'honey')

def test_parse_verb():
    word_list = [('stop', 'the'), ('verb', 'run')]
    result = parse_verb(word_list)
    assert_equal(result, ('verb', 'run'))

def test_parse_object():
    word_list = [('stop', 'the'), ('noun', 'door')]
    result = parse_object(word_list)
    assert_equal(result, ('noun', 'door'))

def test_parse_subject():
    word_list = [('verb', 'run'), ('noun', 'door')]
    subj = ('noun', 'player')
    sentence = parse_subject(word_list, subj)
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'run')
    assert_equal(sentence.object, 'door')

def test_peek():
    word_list = [('noun', 'princess'), ('verb', 'eats')]
    result = peek(word_list)
    assert_equal(result, ('noun'))

def test_no_match_found():
    word_list = []
    result = match(word_list, None)
    assert_equal(result, None)

def test_match_found():
    word_list = [('noun', 'princess'), ('stop', 'the')]
    result = match(word_list, ('noun'))
    assert_equal(result, ('noun', 'princess'))

def test_skip():
    word_list = [('stop', 'the'), ('stop', 'in'), ('noun', 'bear')]
    skip(word_list, 'stop')
    assert_equal(word_list, [('noun', 'bear')])


