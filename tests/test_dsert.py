from dsert import assert_valid_dict
from unittest import TestCase


class BaseTestCase(TestCase):

    def setUp(self):
        self.basic_dict = {'foo': 'bar'}


class TestKnownContents(BaseTestCase):

    def test_correct_values_should_not_raise_an_error(self):
        assert_valid_dict(to_validate=self.basic_dict, known_contents=self.basic_dict)

    def test_missing_value_should_raise_an_error(self):
        with self.assertRaises(KeyError):
            assert_valid_dict(to_validate=self.basic_dict, known_contents={})

    def test_incorrect_value_should_raise_an_error(self):
        with self.assertRaises(KeyError):
            assert_valid_dict(to_validate=self.basic_dict, known_contents={'snap': 'crackle'})

    def test_extra_value_should_raise_an_error(self):
        with self.assertRaises(KeyError):
            assert_valid_dict(
                to_validate=self.basic_dict,
                known_contents={'foo': 'bar', 'snap': 'crackle'},
            )


class TestUnknownContents(BaseTestCase):

    def test_correct_types_should_not_raise_an_error(self):
        assert_valid_dict(to_validate=self.basic_dict, unknown_contents={'foo': str})

    def test_missing_type_should_raise_an_error(self):
        with self.assertRaises(KeyError):
            assert_valid_dict(to_validate=self.basic_dict, unknown_contents={})

    def test_incorrect_type_should_raise_an_error(self):
        with self.assertRaises(ValueError):
            assert_valid_dict(
                to_validate=self.basic_dict,
                unknown_contents={'foo': int},
            )

    def test_extra_type_should_raise_an_error(self):
        with self.assertRaises(KeyError):
            assert_valid_dict(
                to_validate=self.basic_dict,
                unknown_contents={'foo': str, 'snap': str}
            )


class TestExcludedFields(BaseTestCase):

    def test_correct_fields_should_not_raise_an_error(self):
        assert_valid_dict(to_validate=self.basic_dict, excluded_fields=['foo'])

    def test_missing_field_should_raise_an_error(self):
        with self.assertRaises(KeyError):
            assert_valid_dict(to_validate=self.basic_dict, excluded_fields=[])

    def test_incorrect_field_should_raise_an_error(self):
        with self.assertRaises(KeyError):
            assert_valid_dict(
                to_validate=self.basic_dict,
                excluded_fields=['snap'],
            )

    def test_extra_type_should_raise_an_error(self):
        with self.assertRaises(KeyError):
            assert_valid_dict(
                to_validate=self.basic_dict,
                excluded_fields=['foo', 'snap'],
            )
