# -*- coding: utf-8 -*-
import pytest

from salad.preprocessing.text import Tokenizer


def test_tokenize():
    noisy_text = '''
    長年勤めたNTTを退職しました。http://bit.ly/abcde
    以上が転職した経緯です。
    '''
    expected = '長年 勤め た NTT を 退職 し まし た 。 以上 が 転職 し た 経緯 です 。'
    actual = Tokenizer().parse(noisy_text)
    assert expected == actual


if __name__ == '__main__':
    pytest.main([__file__])
