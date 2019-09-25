.. _doc-label: doc.rst

Documentation
-------------

Everyone should want their code documented. The simple reason for that is
that nobody will be able to use your code of there is no documentation. So,
let's get started.

Pre-Setup-Rambling
++++++++++++++++++

First of all, all documentation in for Python code is written in
ReStructuredText, short: ``RST``. It is extremely similar to Markdown, but it
has a few advantages when it comes to writing longer documentation. For example,
if you want to write so much documentation that the it's easier to split
things up into chapter, you can simply include chapter files into a main file
(much like in LateX), which is not possible using Markdown. But this is just
one of the perks. When you start working with sphinx you will start noticing
the subtle and the obvious differences between ``RST`` and ``Markdown``.


Setting up Sphinx
+++++++++++++++++

Let's say you have created your ``conda environment`` using the
``environment.yml`` that was provided with the sample package. In your own
package directory create a docs subdirectory just as in the ``htmapp``
repository and ``cd`` into it

.. code-block:: bash

    # Provided you are in your package repo
    $ mkdir docs && cd docs

Then,

.. code-block:: bash

    $ sphinx-quickstart

will guide you through the initialization process of creating sphinx structure.


As you may have noticed a bunch of files were generated in the docs directory.
The most important ones are: ``conf.py`` & ``index.rst``. The latter can be
thought of as ``main.tex`` for LateX documents. The former is a configuration
file that defines any modifications for the way the documents are created.

``conf.py``
===========

To be able to actually document the code and make the final html look nice, a
few lines in ``conf.py`` have to changed. The lines that are changed are
shown below:

.. code-block:: python

    ...

    extensions = ['sphinx.ext.autodoc',
                  'sphinx.ext.viewcode',
                  'm2r'
    ...
    autoclass_content = 'both'
    ...

    html_theme = 'sphinx_rtd_theme'

    ...

The extensions enable the possibility on auto documenting your code, meaning
the docstrings of your functions and classes are gonna be read and added when
the ``.. auto-module`` directive is called. ``autoclass_content = 'both'``
makes sure that when a class is documented in your code the ``__init__`` part
will be documented as well. Finally, the ``sphinx_rtd_theme`` is simply nice
to look at. There are other themes out there. But I just like this one.


``index.rst``
=============

The ``index.rst`` is used to control the content in your documentation.
Usually this is done by the so-called ``toctree`` directive (table of
contents tree), which allows us to include files so that not the complete
documentation has to be written in one file. A standard file (the one of this
documentation) looks as follows:

.. include:: ../index.rst
    :code: rst

This way, we can write a very user-friendly structured documentation.



API
===

There's one step involved in making the documentation "automatic". We need
some file to actually call in the "docstrings" from the package files. The
usual way of doing this is to have a function library at the end of your
documentation. Here, it is also the last section: :ref:`api-label`. The
source file is very simple:

.. include:: API.rst
    :code: rst

As you can see, we have exactly one ``.. automodule::`` per python module
(file). The cool thing about this is that we don't have to
change the actual reference to the function or even write manual
documentation on the side. When the functions in the package are updated, so
will the documentation.


Offline Docs
============

To create either the ``pdf`` or the ``html`` files, simply cd into the
``docs`` directory and

.. code-block:: bash

    # For PDF
    make pdf

    # For HTML
    make html

The built files can then be found in ``docs/build/pdf`` or ``docs/build/html``.
The pdf, I assume, you can find yourself, but if you want to open the ``html``
it's the ``index.html`` file you want to open. It brings you directly to
offline webpage when opened.


ReadTheDocs
===========

What's nice about Python, Sphinx, and ReStructuredText that with a few simple
tricks your documentation is online. The key ingredient to make that happen
is the ``.readthedocs.yml`` file. This file tells the server what is
necessary to build your documentation and how to build it. Let's take a look.

.. include:: ../../../.readthedocs.yml
    :code: yaml

There are a few important steps here. The first entry in this file that needs
to be manually set is the ``sphinx` keyword. The location of the conf.py
needs to be set in relation to the repository.The second one is the ``formats``
keyword, which if you want ``html``, ``PDF`` and ``EPub`` built and
donwloadable from the page, is simply 'all'. Otherwise specify.
Much like for the installation and the unit testing we also need to specify the
``environment.yml`` with the keywords ``conda`` and ``environment``. Last but
not least, we have to define Python version and method of installation. In
this case, we'll let ``pip`` do the job.

Having this things set, head over to `ReadTheDocs <https://readthedocs.org/>`_
and log in. If you do not have an account there, I would suggest logging in
using your Github account. Then import the github repository. That should be
it since the ``.readthedocs.yml`` does all the configuring. Usually it takes
a bit until the build is done, but eventually you can click on the ``View
Docs`` button and your good to go.

