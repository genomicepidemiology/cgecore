Result class test
=================

```python

>>> from result import Result, ResultParser
>>> from exceptions import CGECoreOutTypeError, CGECoreOutInputError

```

Usage
-----

A Result object can be initialized using a dict containing many key-value pairs.
The "type" key is always mandatory, but other key-values depend on the given
template.
```python

>>> res = Result(**{"type": "software_result"})
>>> res.val_parsers["char64"]("54d762f5aacbd706457d109d520e3c550feb8df"
...                           "edc4f0d8ccae1ad203e3388c0")

```

When the Result instance is created, the class used to test the format of the
values is also chosen. Per default it is the ValueParsers class.
**Important:** It is the class that is given as argument, not an instance of the
class.
```python

>>> from valueparsers import ValueParsers
>>> custom_parser = ValueParsers
>>> res2 = Result(parsers=custom_parser, **{"type": "software_result"})

```

Exceptions
----------

Result must be initialized with a "type". Otherwise an exception is thrown.
```python

>>> res = Result()
... #doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
exceptions.CGECoreOutTypeError:
    The class format requires a 'type' attribute. The given dictionary contained
    the following attributes: dict_keys([])

```

The "type" can be provided as an argument named "result_type" and/or "type". If
both are provided, they must match, or an exception is thrown.
```python

>>> res = Result(result_type="some_type", **{"type": "another_type"})
... #doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
exceptions.CGECoreOutTypeError:
    Type was given as argument to method call and as an attribute in the given
    dictionary, but they did not match. some_type (method) != another_type
    (dict)

```

The "type" given must be defined in the json template provided. These are found
in the "templates_json" folder. If not an exception is thrown and the possible
types of the given json is listed. In the test the exact types has been left out
and replaced with "...".
```python

>>> res = Result(result_type="some_type")
... #doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
Traceback (most recent call last):
exceptions.CGECoreOutTypeError:
    Unknown result type given. Type given: some_type. Type must be one of: [...]

```
