# dsert

[![Build Status](https://travis-ci.org/paxos-bankchain/dsert.svg?branch=master)](https://travis-ci.org/paxos-bankchain/dsert)

Library to explicitly test *all* the fields of a python dictionary, even when you don't know all of their values.

## Install

From [PyPi](https://pypi.python.org/pypi/dsert/):
```bash
$ pip install dsert
```

From [GitHub](https://github.com/paxos-bankchain/dsert/):
```bash
$ pip install git+https://github.com/paxos-bankchain/dsert.git
```

## Examples

```python
>>> from dsert import assert_valid_dict
>>> my_dict = {'balance': 123.45, 'status': 'homeowner', 'good_credit': True}
```

Check all the fields (will return `None`):
```python
>>> assert_valid_dict(my_dict, known_contents={'balance': 123.45}, known_types={'status': str, 'good_credit': bool})
>>>
```

Check some of the fields (will raise an `Exception` with helpful debug instructions):
```python
>>> assert_valid_dict(my_dict, known_contents={'balance': 123.45})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "dsert/__init__.py", line 35, in assert_valid_dict
    raise KeyError(err_msg)
KeyError: "Keys for {'good_credit': True, 'status': 'homeowner'} not in known_contents keys (['balance']), known_types keys ([]), nor excluded_fields ([])."
```

## Why

Most tests are opt-in, where we test certain keys/values only:
```python
>>> self.assertEqual(some_dict['a'], 1)
```

This can work well, but it can also cause situations where the tests pass and yet a bug has slipped in!

From [The Zen of Python](https://www.python.org/dev/peps/pep-0020/)
> Explicit is better than implicit.

## Coming Soon

More complex validators. Don't just test that a dictionary value is of type `int`, test that it's a positive/even/prime `int`.

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
(this requires having [nose](http://nose.readthedocs.io/en/latest/) installed)

Make your changes and confirm that tests still pass:
```
$ nosetests .
```

## Updating PyPi

You must have the credentials in order to push updates to [PyPi](https://pypi.python.org/pypi).

Create a `.pypirc` file in your home directory:
```
$ cat ~/.pypirc
[distutils]
index-servers=
    pypi

[pypi]
repository = https://pypi.python.org/pypi
username = paxos
password = <password goes here>
```

Install twine:
```
$ pip install twine
```

Create a distribution:
```
$ python setup.py sdist bdist_wheel
```

Push your distribution to PyPi:
```
$ twine upload dist/* -r pypi
```

To test this process, you can use [PyPi's test server](https://testpypi.python.org/). Add an entry to `.pypirc` that looks like this with whatever creds you create for testpypi:
```
[testpypi]
repository = https://testpypi.python.org/pypi
username = <your user name goes here>
password = <your password goes here>
```

Then use the following command to push your distrobution to test PyPi:
```
$ twine upload dist/* -r testpypi
```
