Installation
------------

There are two things necessary for a good Python package installation. First,
the ``setup.cfg`` and/or ``setup.py`` files which control the installation of the package itself.
This is needed, if you want to create your package and use it like a pip
installed package. The other thing is the ``environment.yml`` which is used to
set up the environment for the installation. For this small project, the
``environment.yml`` is using a sledgehammer to crack a nut. We will still want to
keep it here for completeness.


Actual installation
+++++++++++++++++++

Having all these corner stones in place, we simply need to install it. This
is simply done by the following line of code.

.. code-block:: bash

    # Install your package
    pip install -e .

The ``-e`` simply let's you modify the package without having to reinstall it
all the time. So, testing of the package can be done with every change of the
source files even though there is no re-installation. Note that this is only
necessary for packages that you install from the source code and plan on
modifying!

.. _setup-cfg:

``setup.cfg``
+++++++++++++

In newer installations, the ``setup.cfg`` replaces parts of the ``setup.py``
or, in many cases, even the whole file. Here, we define all the options that
we want ``setuptools.setup()`` to use when executing:

.. code-block:: python

    pip install -e .

First, let's have a look at the file in our project:

.. literalinclude:: ../../../setup.cfg
    :language: bash
    :linenos:

Most of the defined options are quite self-explanatory.

.. code-block:: bash

    [options.packages.find]
    where = src

defines where the package is located. Typically, we have a ``src`` folder that
contains the whole package. This line changes the import structure so that we
can later run ``import matpy`` instead of ``import src.matpy``. For a list of
all available parameters and their correct syntax check out the
`setuptools documentation <https://setuptools.readthedocs.io/en/latest/userguide/declarative_config.html>`_.

Scripts argument
================

The scripts argument lets you create executables that are installed upon
running the installation. For example, in the directory ``bins`` (binaries,
which are not technically binaries in this case, but used in the same way as
traditional binary files), there is the executable sample-bin:

.. literalinclude:: ../../../src/matpy/bins/sample_bin.py
    :language: python
    :linenos:

It is normal Python code, but after installation

.. code-block:: bash

    pip install -e .

you can simply run

.. code-block:: bash

    sample-bin

from anywhere on your computer, which will run the python command ``sample_bin()``. Do make sure that this filenames do not
conflict with your traditional command line tools such as ``ls``, ``cd``, etc.
Otherwise you won't be able to use your created executables.

.. _setup-py:

``setup.py``
++++++++++++

In some cases, you might still want to include a ``setup.py`` which used
to be the old standard way. One of those cases is if you would like to be
able to use the ``-e`` (editable) ``pip install`` command. Then, you would
just include a minimal ``setup.py`` containing the following:

.. code-block:: python

    from setuptools import setup

    # configuration is done in setup.cfg
    setup()

A second use-case of the ``setup.py`` is illustrated in our sample file:

.. literalinclude:: ../../../setup.py
    :language: python
    :linenos:

Here, we add the ``cmdclass`` keyword, which is not supported by the
``setup.cfg`` (at least, at the time of writing). After package installation,
when you in the repository, a simple

.. code-block:: bash

    pytest

will check all subdirectories for tests and run them subsequently. It is
amazing for debugging your code.
A third case is for more advanced dynamic installs, in which we wish to
compile our module differenly depending upon which machine it is installed
on (e.g., different OS or architecture).


``environment.yml``
+++++++++++++++++++

This one is mainly to set up an environment and install dependencies there,
so that you main Python installation stays untouched and cannot be broken.
The general structure looks as follows:


.. literalinclude:: ../../../environment.yml
    :language: yaml
    :linenos:

``name`` specifies the name of the environment to be created, and ``pip``
defines extra packages that possibly aren't available from the conda package
manager. And additional setting that is often used, but we are skipping here are
``channels``, which are online locations from where to grab the dependencies
when they are installed with conda (a typical example is conda-forge).
The file is pretty straightforward, so I'm gonna stop talking about it now.

To create an environment from the ``environment.yml`` file simply execute the following:

.. code-block:: bash

    conda env create -f environment.yml