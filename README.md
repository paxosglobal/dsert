# dsert

[![Build Status](https://travis-ci.org/paxos-bankchain/dsert.svg?branch=master)](https://travis-ci.org/paxos-bankchain/dsert)

Library to explicitly test *all* the fields of a python dictionary, even when you don't know all of their values.

## Install

```bash
$ pip install git+https://github.com/paxos-bankchain/dsert.git
```
TODO: pypi support

## Examples

```python
>>> from dsert import assert_valid_dict
>>> my_dict = {'balance': 123.45, 'property': 'homeowner', 'good_credit': True}
```

Check all the fields (will return `None`):
```python
>>> assert_valid_dict(my_dict, known_contents={'balance': 123.45}, unknown_contents={'property': str}, excluded_fields=['good_credit'])
>>>
```

Check some of the fields (will raise an `Exception` with helpful debug instructions):
```python
>>> assert_valid_dict(my_dict, known_contents={'balance': 123.45})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "dsert/__init__.py", line 35, in assert_valid_dict
    raise KeyError(err_msg)
KeyError: "Keys for {'good_credit': True, 'property': 'homeowner'} not in known_contents keys (['balance']), unknown_contents keys ([]), nor excluded_fields ([])."
```

## Contributing

Check out repo:
```bash
$ git checkout git+https://github.com/paxos-bankchain/dsert.git && cd dsert
```

Install locally
```bash
$ pip install --editable .
```

Confirm tests pass:
```
$ nosetests .
```
(this requires having [nose](http://nose.readthedocs.io/en/latest/]) installed)

Make your changes and confirm that tests still pass:
```
$ nosetests .
```

## Coming Soon

More complex validators. Don't just test that a dictionary value is of type `int`, test that it's a positive/even/prime `int`.
