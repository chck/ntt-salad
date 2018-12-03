# -*- coding: utf-8 -*-
import pytest

from salad.utils.string_utils import (
    clean,
    remove_br,
    remove_url,
)


def test_clean():
    noisy_text = '''
    改行とURLつきテキストです。http://bit.ly/abcde
    改行とURLつきテキストです。
    '''
    expected = '改行とURLつきテキストです。 改行とURLつきテキストです。'
    actual = clean(noisy_text)
    assert expected == actual


def test_remove_br():
    text_with_break = '''
    改行つきテキストです。
    改行つきテキストです。
    改行つきテキストです。
    '''
    actual = remove_br(text_with_break)
    assert '\n' not in actual


def test_remove_url():
    text_with_url = 'URLつきテキストです。http://bit.ly/abcde'
    expected = 'URLつきテキストです。'
    actual = remove_url(text_with_url)
    assert expected == actual


if __name__ == '__main__':
    pytest.main([__file__])
