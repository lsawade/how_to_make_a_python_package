Introduction
------------

This tutorial/repository was created due to a lack of helpful resources that
bring you from writing your two cool functions to actual making them
available to people. So, in the following few pages, you can follow some
instructions, tips, and tricks on how to create your own package that others
can easily install on their machine.

**Disclaimer**: This package is meant to be a you can find everything here,
but don't necessarily need everything packages. It is supposed to be an example.
E.g. the logging part. It is convenient, but most people will never use it in
their lives because it is unnecessary. But for the ones that want to use it
this is going to be a place to look up on how to customize the logger.

.. _module-label:

The module
++++++++++

Before we begin with the stuff you want to learn about, I will briefly
introduce the example module.

``matpy`` is simply a two function, one class package with one module.

.. code-block:: bash

        matpy
          |____matrixmultiplication.py
          |______init__.py

``matpy`` contains one module called ``matrixmultiplication.py``. In the module
there are two functions and one class.
:func:`matpy.matrixmultiplication.matmul`
is just a wrapper around :func:`numpy.matmul`, and
:func:`matpy.matrixmultiplication.dotprod`
is just a wrapper around :func:`numpy.dot`. The third component is the
:class:`matpy.MatrixMultiplication`, which uses the two functions as methods.

To test the function a separate folder is created containing all the tests.

.. code-block:: bash

        tests
          |______init__.py
          |____test_matmul_and_dot.py

``test_matmul_and_dot.py`` is located inside this folder which is the where
the unittests are located. This folder can be used for developement purposes.
The reason for not including the tests inside the module is to lighten the
download of the package.

Goal
++++

The goal of this documentation is to make the package reproducible, create a
fully automated testing environment for the package, as well as good-looking
documentation.

