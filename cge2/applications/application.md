Application class test
=================


###Testing of Application error ###
```python3
>>> from command import ApplicationError
>>> err = ApplicationError(1, "helloworld", "", "Some error text")
>>> err.returncode, err.cmd, err.stdout, err.stderr
(1, 'helloworld', '', 'Some error text')
>>> print(err)
Non-zero return code 1 from 'helloworld', message 'Some error text'
>>> noterr = ApplicationError(1, "helloworld", "Some success text", "")
>>> noterr.returncode, noterr.cmd, noterr.stdout, noterr.stderr
(1, 'helloworld', 'Some success text', '')
>>> print(noterr)
Non-zero return code 1 from 'helloworld'

```
###Testing of CommandLineBase####
```python3
>>> from KMA.kma_application import KMACommandline
>>> kmaline = KMACommandline(k_size=10, min_len=0.5, sparse=True)
>>> kmaline
KMACommandline(cmd='kma', k_size=10, min_len=0.5, sparse=True)

You can instead manipulate the parameters via their properties, e.g.
>>> kmaline.k_size
10
>>> kmaline.k_size = 20
>>> kmaline
KMACommandline(cmd='kma', k_size=20, min_len=0.5, sparse=True)

You can clear a parameter you have already added by 'deleting' the
corresponding property:
>>> del kmaline.k_size
>>> kmaline.k_size
'DB defined (default)'
>>> kmaline.output = "/out/"
>>> kmaline.template_db = "/template_db/"
>>> str(kmaline)
Traceback (most recent call last):
...
ValueError: Parameter input is not set. Neither alternative parameters as input_int, input_ipe.
>>> kmaline.input = "/home.txt"
>>> kmaline.input
'/home.txt'
>>> kmaline
KMACommandline(cmd='kma', input='/home.txt', output='/out/', template_db='/template_db/', min_len=0.5, sparse=True)
>>> str(kmaline)
'kma -i /home.txt -o /out/ -t_db /template_db/ -ml 0.5 -Sparse'
>>> kmaline.input_ipe = "/home2.txt"
>>> str(kmaline)
Traceback (most recent call last):
...
ValueError: Parameter input_ipe is set, but the incompatible parameter input has been also set.

>>> del kmaline.input
>>> kmaline.sup = 10
Traceback (most recent call last):
...
ValueError: Option name sup was not found.
>>> kmaline.custom_args = "-sup 10 --MEH -ipe error.txt"
>>> str(kmaline)

```
