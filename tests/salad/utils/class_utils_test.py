# -*- coding: utf-8 -*-
import pytest

from salad.utils.class_utils import Singleton


def test_singleton():
    class NonSingletonKlass:
        pass

    class SingletonKlass(metaclass=Singleton):
        pass

    assert NonSingletonKlass() != NonSingletonKlass()
    assert SingletonKlass() == SingletonKlass()


if __name__ == '__main__':
    pytest.main([__file__])
