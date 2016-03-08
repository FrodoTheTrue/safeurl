SafeUrl: link analyzer on Python
================================
Simple and clever analyzer, decoder, encoder ... urls on python, using requests

.. image:: https://badge.fury.io/py/safeurl.svg
    :target: https://badge.fury.io/py/safeurl

Installation
------------
.. code-block:: bash

    $ pip install safeurl

Usage
------------
.. code-block:: python

    from safeurl.core import decodeURL
    decodeURL("http://bit.ly/1gaiW96")
    # https://www.yandex.ru/