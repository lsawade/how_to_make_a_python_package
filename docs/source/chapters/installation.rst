Installation
------------

There are two things necessary for a good Python package installation. One,
the ``setup.py`` file which controls the installation of the package itself.
This is needed, if you want to create your package and use it like a pip
installed package. The other thing is the ``environment.yml`` which is used to
set up the environment for the installation. For this small project, the
``environment.yml`` is using a sledgehammer to crack a nut. I still want to
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


.. _setup-py:

``setup.py``
++++++++++++

Everything important that is needed to install your package is located in the
``setup.py`` file.
The ``setup.py`` file used for this project contains two small things that
make your life easier, but first of all let's look at the whole thing.

.. literalinclude:: ../../../setup.py
    :language: python
    :linenos:

First, there is a function to read the ``README.md`` which will then be
printed into the long_description of the package. It simply reads it as a
string that is used in the actual setup.
The second thing which is a great addition for testing is the ``PyTest``
testcommand. After package installation, when you in the repository, a simple

.. code-block:: bash

    pytest

will check all subdirectories for tests and run them subsequently. It is
amazing for debugging your code.
Other than that, you can look at the simple keywords in the ``setup( )`` and
change them to match you liking. The line ``packages=find_packages()`` will
find all directories below the main directory that contain a ``__init__`` and
them to your in

Scripts argument
================

The scripts argument lets you create executables that are installed upon
running the installation. For example, in the directory ``bins`` (binaries,
which are not technically binaries in this case, but used in the same way as
traditional binary files), there is the executable sample-bin:

.. literalinclude:: ../../../bins/sample_bin
    :language: python
    :linenos:

It is normal Python code, but after installation

.. code-block:: python

    pip install -e .

you can simply run

.. code-block:: python

    sample_bin

from anywhere on your computer. Do make sure that this filenames do not
conflict with your traditional command line tools such as ``ls``, ``cd``, etc.
Otherwise you won't be able to use your created executables.


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
when they are installed with conda.
The file is pretty straightforward, so I'm gonna stop talking about it now.

To create an environment from the ``environment.yml`` file simply