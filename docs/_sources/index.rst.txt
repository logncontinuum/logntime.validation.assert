.. logn.validation.assertions documentation master file, created by
   sphinx-quickstart on Tue May 10 14:30:15 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Assertions documentation
========================

Custom messages
---------------

This is library with functions to exert fancy assertions in test cases.
It enables attaching a custom messages to the beginning of the text on the exception thrown when the assertion fails.

.. code:: python

    from logntime.validation.assertions.assert_equals import assert_equals

    custom_message = "Very important test failed."

    expected = (1, 2, 3)
    result = (1, 2, 3, 4)

    assert_equals(
        expected,
        result,
        custom_message=custom_message
    )

    # Very important test failed.
    # Subject is not equal to reference.
    #     Reference: (1, 2, 3)
    #     Subject: (1, 2, 3, 4)

It also lets you format the "expected" and "result" parameters.

.. code:: python

    from logntime.validation.assertions.assert_equals import assert_equals

    expected = (1, 2, 3)
    result = (5, 6, 7)

    def(data):
        ">".join(map(str, data))

    assert_equals(
        expected,
        result,
        format_data=to_json
    )

    # Subject is not equal to reference.
    #    Reference: 1>2>3
    #    Subject: 5>6>7

Assert similarities
-------------------

It allows to assert equality for dictionaries and prints a report of the difference in case of failure.


.. code::

    assert_similarities



Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. toctree::
   :maxdepth: 2
   :caption: Contents:




