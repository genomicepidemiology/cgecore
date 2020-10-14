# Result class test

```python

>>> from result import Result, ResultParser
>>> from exceptions import CGECoreOutTypeError, CGECoreOutInputError

```

## Usage

### Initialize Result class

A Result object can be initialized using a dict containing many key-value pairs.
The "type" key is always mandatory, but other key-values depend on the given
template.
```python

>>> res = Result(type="software_result", **{"key1": "val1", "key2": "val2"})
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
>>> res = Result(parsers=custom_parser, **{"type": "software_result"})

```

### Initialize ResultParser class

An instance of the Result class loads the json template(s) provided and stores
them in a dict. Each template class is a dict within the dict, and the key is
the class "type".

For each template class an instance of ResultParser is created.

A ResultParser instance is created to hold the definition of a single template
class. The test below uses a previously loaded Result object and provides a dict
from within a dict as argument to ResultParser.

ResultParser is a dict that holds all the definitions from the template class.
Furthermore it detects which values are dictionaries and which values are lists.
It removes the "dict" or "array" part and stores only the rest of the value. But
keeps two dictionaries named "dicts" and "arrays" with the key-value pairs in
order to determine if the value of the key is expected to be a list or a
dictionary.
Values that are not dictionaries or list are not stored in specific
dictionaries, but just in the "root" dictionary.

```python

>>> res_parser1 = ResultParser(result_def=res.defs["software_result"])
>>> res_parser1["type"]
'software_result'
>>> res_parser1["databases"]
'database:class'
>>> res_parser1.dicts["databases"]
'database:class'
>>> "databases" in res_parser1.dicts
True
>>> "databases" in res_parser1.arrays
False
>>> res_parser2 = ResultParser(result_def=res.defs["gene"])
>>> res_parser2["type"]
'gene'
>>> res_parser2.arrays["phenotypes"]
'phenotype.key'

```

### Methods
```python

>>> res.add(**{"key1": "val1", "key2": "val2", "key3": None})
>>> res["key1"]
'val1'
>>> res["key3"]
Traceback (most recent call last):
KeyError: 'key3'

```

Exceptions
----------

Result must be initialized with a "type". Otherwise an exception is thrown.
```python

>>> res = Result()
... #doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
TypeError: __init__() missing 1 required positional argument: 'type'

```

The "type" given must be defined in the json template provided. These are found
in the "templates_json" folder. If not an exception is thrown and the possible
types of the given json is listed. In the test the exact types has been left out
and replaced with "...".
```python

>>> res = Result(type="some_type")
... #doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
Traceback (most recent call last):
exceptions.CGECoreOutTypeError:
    Unknown result type given. Type given: some_type. Type must be one of: [...]

```