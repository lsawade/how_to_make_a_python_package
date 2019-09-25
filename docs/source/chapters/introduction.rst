Introduction
------------

This tutorial/repository was created due to a lack of helpful resources that
bring you from writing your two cool functions to actual making them
available to people. So, in the following few pages, you can follow some
instructions, tips, and tricks on how to create your own package that others
can easily install on their machine.

The module
++++++++++

Before we begin with the stuff you want to learn about, I will briefly
introduce the example module.

``matpy`` is simply a two function, one class package with one module.

.. code-block::

    matpy
      |____matrixmultiplication.py
      |______init__.py
      |____test
            |______init__.py
            |____test_matmul_and_dot.py

``matpy`` contains one module called ``matrixmultiplication.py`` and then
``test_matmul_and_dot.py`` which is the where the unittests are located.

In the module there are two functions and one class. :func:`matpy.matmul`
is just a wrapper around :func:`numpy.matmul`, and :func:`matpy.dotprod`
is just a wrapper around :func:`numpy.dot`. The third component is the
:class:`matpy.MatrixMultiplication`, which uses the two functions as methods.
S

Goal
++++

The goal of this documentation is to make the package reproducible, create a
fully automated testing environment for the package, as well as good-looking
documentation.

