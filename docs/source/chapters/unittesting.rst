Unit Testing
------------

Since Github offerd a builtin unittesting/CI (continuous integration) service it
is relatively easy make your code pull-request-safe. But first a little bit
about testing itself.



Setting up your tests
+++++++++++++++++++++

The first thing you need to do is to set up some tests. As you may have seen in
:ref:`module-label`, ``matpy`` contains a subdirectory, which contains a
testing file, specifically the test file ``test_matmul_and_dot.py``:

.. literalinclude:: ../../../tests/test_matmul_and_dot.py
    :linenos:
    :language: python

When inspecting the file you will, see
three different unittest classes -- for each function and one for the class.
These are not perfect tests, but they do illustrate the basic usage of the
:class:`unittest.TestCase`, which is very useful especially if you want to
set up a test environment. Note that in the last test we are not testing the
output of the class' run since it is already tested with the previous two tests.
This is the great thing about unit testing.


Setting up a ``.travis.yml``
++++++++++++++++++++++++++++

After having at least one file that contains unit tests, we can start setting
up the continuous integration. And as you might suspect, it's also not as
hard as it sounds. You simply need to open an account on
`travis-ci.com <http://travis-ci.com/>`_ preferably using your github account (
or linking the both works, too I presume) and then add the
``.travis.yml`` to your repository. After adding the ``.travis.yml``,
`travis-ci.com <http://travis-ci.com/>`_ will automatically detect the file
and start running a test. This will start after every commit pull request etc.

So now, let's look at one of these ``.travis.yml`` files
(the one from ``matpy``)

.. include:: ../../../.travis.yml
    :code: yaml

The first few things are just system settings. The ``install`` keyword
however introduces a sequence of bash commands that are executed.
Let's go through this thing line by line.

1. Gets the anaconda installation file from the server.
2. Starts installation
3. Add miniconda path to PATH
4. hash -r (idk)
5. In installation always say yes and turn off command line environment
   indicator
6. Add package channels
7. Update conda
8. conda info -a
9. Create environment from environment file
10. Activate environment
11. Install package

The ``script`` is the test script to be executed. If everything is executed
without errors, the continuous integration test will show up as passed.

That means you're all set for continuous integration! Wasn't all that hard
was it?
