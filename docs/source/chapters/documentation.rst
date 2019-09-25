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

    html_theme = 'sphinx_rtd_theme'

    ...

The extensions enable the possibility on auto documenting your code, meaning
the docstrings of your functions and classes are gonna be read and added when
the ``.. auto-module`` directive is called.




