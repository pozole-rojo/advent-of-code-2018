Advent_of_code_2018 |Version| |Build| |Coverage| |Health|
===================================================================

|Compatibility| |Implementations| |Format| |Downloads|

Track coding challenges from advent of code for 2018

.. code:: python

    # TODO: add super short usage


Installation:

.. code:: console

    $ pip install advent_of_code_2018

.. TODO: longer description


Example
-------

.. code:: python

    # TODO: add example

## Local Tests

Docker, Compose, and [Tox](https://tox.readthedocs.org/en/latest/) are used to approximate the environment that Travis CI, Code Climate, and Coveralls all run when you push. This will allow you to test your code against multiple versions of Python (2.6, 2.7, 3.3, 3.4, 3.5, 3.6, PyPy, and PyPy3) locally before pushing it or even committing it.

To run everything (this will take a while the first time you run it, but subsequent runs will be quick):

```
$ docker-compose build && docker-compose up
```

To run against a single environment (e.g., Python 3.4):

```
$ docker-compose build && docker-compose run tox tox -e py34
```

Changelog
---------

**0.0.0**

- Initial release.


.. |Build| image:: https://travis-ci.org/pozole-rojo/advent-of-code-2018.svg?branch=master
   :target: https://travis-ci.org/pozole-rojo/advent-of-code-2018
.. |Coverage| image:: https://img.shields.io/coveralls/pozole-rojo/advent-of-code-2018.svg
   :target: https://coveralls.io/r/pozole-rojo/advent-of-code-2018
.. |Health| image:: https://codeclimate.com/github/pozole-rojo/advent-of-code-2018/badges/gpa.svg
   :target: https://codeclimate.com/github/pozole-rojo/advent-of-code-2018
.. |Version| image:: https://img.shields.io/pypi/v/advent_of_code_2018.svg
   :target: https://pypi.python.org/pypi/advent_of_code_2018
.. |Downloads| image:: https://img.shields.io/pypi/dm/advent_of_code_2018.svg
   :target: https://pypi.python.org/pypi/advent_of_code_2018
.. |Compatibility| image:: https://img.shields.io/pypi/pyversions/advent_of_code_2018.svg
   :target: https://pypi.python.org/pypi/advent_of_code_2018
.. |Implementations| image:: https://img.shields.io/pypi/implementation/advent_of_code_2018.svg
   :target: https://pypi.python.org/pypi/advent_of_code_2018
.. |Format| image:: https://img.shields.io/pypi/format/advent_of_code_2018.svg
   :target: https://pypi.python.org/pypi/advent_of_code_2018
