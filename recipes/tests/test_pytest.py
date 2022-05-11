from unittest import skip

from django.test import TestCase

# Create your tests here.


class Pyteste(TestCase):
    def test_the_pytest_is_ok(self):
        assert 1 == 1, '1 é igual a 1'

    @skip('Teste para testar skip, para pular o teste')
    def test_example_skip(self):
        assert 1 == 1

    def test_raised(self):
        if 1 == 2:
            raise
        else:
            pass
