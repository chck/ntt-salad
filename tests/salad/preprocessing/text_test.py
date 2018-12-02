# -*- coding: utf-8 -*-
import pytest

from salad.preprocessing.text import Tokenizer


def test_tokenize():
    noisy_text = '''
    100年勤めたNTTを退職しました。http://bit.ly/abcde
    以上が転職した経緯です。
    '''
    expected = '100年 勤め た NTT を 退職 し まし た 。 以上 が 転職 し た 経緯 です 。'
    tokenizer = Tokenizer()
    actual = tokenizer.parse(noisy_text)
    assert expected == actual


if __name__ == '__main__':
    pytest.main([__file__])