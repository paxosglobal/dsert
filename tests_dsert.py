from dsert import assert_valid_dict
from unittest import TestCase


class BasicTestCase(TestCase):

    def setUp(self):
        self.basic_dict = {'foo': 'bar'}


class TestKnownContents(BasicTestCase):

    def test_correct_values_should_not_raise_an_error(self):
        assert_valid_dict(to_validate=self.basic_dict, known_contents=self.basic_dict)

    def test_missing_value_should_raise_an_error(self):
        with self.assertRaises(KeyError):
            assert_valid_dict(to_validate=self.basic_dict, known_contents={})

    def test_incorrect_key_should_raise_an_error(self):
        with self.assertRaises(KeyError):
            assert_valid_dict(to_validate=self.basic_dict, known_contents={'snap': 'crackle'})

    def test_incorrect_value_should_raise_an_error(self):
        with self.assertRaises(ValueError):
            assert_valid_dict(to_validate=self.basic_dict, known_contents={'foo': 'baz'})

    def test_extra_value_should_raise_an_error(self):
        with self.assertRaises(KeyError):
            assert_valid_dict(
                to_validate=self.basic_dict,
                known_contents={'foo': 'bar', 'snap': 'crackle'},
            )


class TestUnknownContents(BasicTestCase):

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


class TestExcludedFields(BasicTestCase):

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


class TestAdvancedUsage(TestCase):

    def setUp(self):
        self.advanced_dict = {
            'temp': 98.6,
            'color': 'red',
            'healthy': True,
        }

    def test_exact_match_should_succeed(self):
        # there's no reason to do this, a simple equality test with == works
        assert_valid_dict(to_validate=self.advanced_dict, known_contents=self.advanced_dict)

    # Unknown:

    def test_partial_unknown_match_should_succeed(self):
        assert_valid_dict(
            to_validate=self.advanced_dict,
            known_contents={'temp': 98.6, 'color': 'red'},
            unknown_contents={'healthy': bool},
        )

    def test_mostly_unknown_match_should_succeed(self):
        assert_valid_dict(
            to_validate=self.advanced_dict,
            known_contents={'temp': 98.6},
            unknown_contents={'color': str, 'healthy': bool},
        )

    def test_entirely_unknown_match_should_succeed(self):
        assert_valid_dict(
            to_validate=self.advanced_dict,
            unknown_contents={'color': str, 'healthy': bool, 'temp': float},
        )

    # Exclude:

    def test_partial_excluded_match_should_succeed(self):
        assert_valid_dict(
            to_validate=self.advanced_dict,
            known_contents={'temp': 98.6, 'color': 'red'},
            excluded_fields=['healthy'],
        )

    def test_mostly_excluded_match_should_succeed(self):
        assert_valid_dict(
            to_validate=self.advanced_dict,
            known_contents={'temp': 98.6},
            excluded_fields=['color', 'healthy'],
        )

    def test_entirely_excluded_match_should_succeed(self):
        assert_valid_dict(
            to_validate=self.advanced_dict,
            excluded_fields=['temp', 'color', 'healthy'],
        )

    # Errors

    def test_exact_match_plus_extra_unknowns_should_raise_an_error(self):
        with self.assertRaises(TypeError):
            assert_valid_dict(
                to_validate=self.advanced_dict,
                known_contents=self.advanced_dict,
                unknown_contents={'foo': 'bar'},
            )

    def test_exact_match_plus_extra_excludes_should_raise_an_error(self):
        with self.assertRaises(KeyError):
            assert_valid_dict(
                to_validate=self.advanced_dict,
                known_contents=self.advanced_dict,
                excluded_fields=['foo'],
            )

    def test_missing_key_should_raise_an_error(self):
        with self.assertRaises(KeyError):
            assert_valid_dict(
                to_validate=self.advanced_dict,
                known_contents={'temp': 98.6},
            )

    def test_incorrect_value_should_raise_an_error(self):
        with self.assertRaises(ValueError):
            assert_valid_dict(
                to_validate=self.advanced_dict,
                known_contents={'temp': 98.7},
                excluded_fields=['color', 'healthy'],
            )
