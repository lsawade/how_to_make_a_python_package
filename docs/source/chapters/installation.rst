Installation
------------

There are two things necessary for a good Python package installation. One,
the ``setup.py`` file which controls the installation of the package itself.
and then the ``environment.yml`` which is used to set up the environment for
the installation.


``setup.py``
++++++++++++

In the ``setup.py`` file used for this project, there are two small things that
make your life easier, but first of all let's look at it.

.. include:: ../../../setup.py
    :code: python

First, there is a function to read the ``README.md`` which will then be
printed into the long_description of the package.
The second thing which is a great addition for testing is the ``PyTest``
testcommand. After package installation, when you in the repository, a simple

.. code-block:: bash

    $ pytest

will test all test in all subdirectories. It is amazing for debugging your code.
Other than that, you can look at the simple keywords in the ``setup( )`` and
change them to match you liking. The line ``packages=find_packages()`` will
find all directories below the main directory that contain a ``__init__``.



``environment.yml``
+++++++++++++++++++

This one is mainly to set up an environment and install dependencies there,
so that you main Python installation stays untouched and cannot be broken.
The general structure looks as follows:


.. include:: ../../../environment.yml
    :code: yaml

``name`` specifies the name of the environment to be created, ``channels``
the online locations from where to grab the dependencies when they are
installed with conda, and ``pip`` defines extra packages that possibly aren't
available from the conda package manager. The file is pretty straightforward,
so I'm gonna stop talking now.

Actual installation
+++++++++++++++++++

Having all these corner stones in place, we simply need to install it. This
is simply done by the following few lines of code.

.. code-block:: bash

    # Create the conda environment and install dependencies
    conda env create -f environment.yml

    # Activate the conda environment
    conda activate htmapp

    # Install your package
    pip install -e .


The ``-e`` simply let's you modify the package without having to reinstall it
all the time.
