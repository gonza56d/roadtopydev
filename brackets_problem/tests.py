from unittest import TestCase

from parameterized import parameterized

from .brackets import has_valid_brackets


class TestBracketsValidator(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.valid_value = """
        some_function {
            some_function (
                some_values {
                    blah {
                        value(value!!)
                    }
                }
            )
        }
        """
        self.invalid_value = """
        some_function {
            some_wrong_function (
                some_values {
                    blah {
                        value(value!!)
                    }
            )
        }
        """

    def get_value(self, is_valid: bool) -> str:
        return {
            True: self.valid_value,
            False: self.invalid_value
        }[is_valid]

    @parameterized.expand([(True,), (False,)])
    def test_validator_success(self, is_valid: bool) -> None:
        value = self.get_value(is_valid)

        result = has_valid_brackets(value)

        assert result is is_valid
