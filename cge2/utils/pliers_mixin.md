# Pliers test

```python

>>> from cge2.utils.pliers_mixin import PliersMixin

>>> version, commit = PliersMixin.get_version_commit(gitdir=".")
>>> len(commit)
40

>>> version, commit = PliersMixin.get_version_commit(gitdir="./cge2")
>>> commit
'unknown'

```
