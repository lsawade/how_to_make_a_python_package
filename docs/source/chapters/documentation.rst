.. _doc-label: doc.rst

Documentation
-------------

Everyone should want their code documented. The simple reason for that is
that nobody will be able to use your code if there is no documentation. So,
let's get started.

Pre-Setup-Rambling
++++++++++++++++++

First of all, all documentation for Python code is written in
ReStructuredText, short: ``RST``. It is extremely similar to Markdown, but it
has a few advantages when it comes to writing longer documentation. For example,
if you want to write so much documentation that it's easier to split
things up into chapters, you can simply include chapter files into a main file
(much like in LateX), which is not possible using Markdown. But this is just
one of the perks. When you start working with sphinx, you will start noticing
the subtle and obvious differences between ``RST`` and ``Markdown``.


Setting up Sphinx
+++++++++++++++++

Let's say you have created your ``conda environment`` using the
``environment.yml`` that was provided with the sample package. 
If you are working on your own package, make sure that you have
both `sphinx` installed and the `sphinx-rtd-theme`. If not,

.. code-block:: bash

    $ pip install sphinx sphinx-rtd-theme

Now you're all set to start compiling some documentation!
First, let's create a directory for the docs and all things related

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
    ...
    autoclass_content = 'both'
    ...

    html_theme = 'sphinx_rtd_theme'

    ...

The extensions enable the possibility on auto documenting your code, meaning
the docstrings of your functions and classes are gonna be read and added when
the ``.. auto-module`` directive is called. ``autoclass_content = 'both'``
makes sure that when a class is documented in your code the ``__init__`` part
will be documented as well. If you are writing your docstrings in a language other
than `sphinx` (e.g. `Numpy`, which looks nicer (less dense) in your script)
adding ``sphinx.ext.napoleon`` to extensions, will auto-translate
those docstrings. Finally, the ``sphinx_rtd_theme`` is simply nice
to look at. There are other themes out there. But I just like this one.


``index.rst``
================

The ``contents.rst`` is used to control the content in your documentation.
Usually this is done by the so-called ``toctree`` directive (table of
contents tree), which allows us to include files so that not the complete
documentation has to be written in one file. A standard file (the one of this
documentation) looks as follows:

.. literalinclude:: ../index.rst
    :language: rst
    :linenos:

This way, we can write a very user-friendly structured documentation. 



API
===

There's one step involved in making the documentation "automatic". We need
some file to actually call in the "docstrings" from the package files. The
usual way of doing this is to have a function library at the end of your
documentation. Here, it is also the last section: :ref:`api-label`. The
source file is very simple:

.. literalinclude:: API.rst
    :language: rst
    :linenos:

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



Publishing your documentation online: 2 ways
++++++++++++++++++++++++++++++++++++++++++++

There are two ways you can publish your documentation online. You could either 
publish it through an external service such as `ReadTheDocs`, or, my now 
preferred way, through `github-pages`, directly from your github repo from a 
separate branch. 
The branch style setup is slightly more difficult, but I would definitely 
recommend it since you are not dependent on third-party services
(except `github`). 
Both ways are explained below and work equally well. 
Since I prefer the `github-pages`, let's start with that one.

`gh-pages`
==========

.. note::

    Before we get started, this option is only really possible if you choose
    to make your Github repo public. If it is not public, github refuses to host
    online documenation (which makes sense). You can follow these instructions
    either way. The disadvantage is that you won't be able to access the 
    online documenation (that is also the case for the `ReadTheDocs` documentation
    if you don't have a `pro` account). 
    The advantage is that once you have set this up and decide to make you 
    repository public, it takes seconds to host your
    up-to-date documentation (almost by yourself!).

After having set up the documentation locally, you can host it in a very 
simple, yet a bit tricky way on github pages if you setup your `Makefile`
correctly. Through in the `sphinx` setup already created a Makefile to create 
documentation. Now we create our own `Makefile` in the repodirectory that 
imitates the one generated by `sphinx`, so that you can run `make html/pdf` 
right from the main repo. For continuity however we keep the `sphinx` in
the docs folder, so that we have a way to go `back in time`.
To publish the webpage, create a `Makefile` that looks like the sphinx one in
the main repository directory with the difference that we change the actual
location of the source and destination to `docs/{src, build}`, respectively, 
and we add a new `target` to our `Makefile`, called `gh-pages`.

.. literalinclude:: ../../../Makefile
    :language: make
    :linenos:

.. note:: 

    Disregard the last `target` in the `Makefile` for now.

The very first time we need to create a branch called `gh-pages`.

.. code-block:: bash

    # Create branch
    git branch gh-pages

.. note :: 

    Do not switch to the branch! One user has reported that `git branch <branch>`
    showed unexpected behaviour by switching to the branch. 
    Check whether you are on the `master` branch using:

    `git branch`

    The branch with the star is the current branch. If it is not on the `master`
    `branch`, switch to the `master` `branch` using 

    `git checkout master`


This creates your documentation branch in your local git repo. Afterwards we can
call

.. code-block:: bash

    # Create extra branch and clear unnecessary files afterwards
    make gh-pages

To automatically checkout out all necessary files, compile the html data,
delete unnecessary data, and finally push the branch to the online `gh-pages`
branch.

To be clear what's happening, let's go through the `Makefile` `target`
`gh-pages` line by line.

Create branch
#############

.. code-block:: bash
    
    git checkout gh-pages

Delete previous build 
#####################

This step is redundant for building the first time, so it is skipped.

.. code-block:: bash
    
    rm -rf build _sources _static _modules chapters


Get necessary files from `master` `branch`
##########################################

.. code-block:: bash
    
    git checkout master $(GH_PAGES_SOURCES) .gitignore

This line gets all the necessary files listed in the `GH_PAGES_SOURCES`
variable declaration at the top of the file to create your documentaion;
i.e. the documentation folder, the package filed the test folder, and other
files which are presented in the documentation later on.

.. note:: 

    Note that the `.gitignore` is outside the `GH_PAGES_SOURCES`. We do not
    want to delete the `.gitignore` before we stage and commit our changes 
    later on, but all of `GH_PAGES_SOURCES` is deleted. Hence, we check it out
    separately.


Compile the documentation
#########################

Just like you did locally, compile the documenation with the following line

.. code-block:: bash

    make html


Move files into `html` from `build` folder to main repo
#######################################################

This step ensures that `github-pages` can read your files

.. code-block:: bash

    mv -fv docs/build/html/* ./

Remove files unnecessary fro the website
########################################

.. code-block:: bash

    rm -rf $(GH_PAGES_SOURCES) build

Stage the changes
#################

.. code-block:: bash
    
    git add -A


Commit & push branch to github repo 
###################################

This is a pretty long one-liner, but to split it up by the `&&`, it first
commits the changes with a message to the `gh-pages` `branch`. Second,
it pushes the changes to the online repo `gh-pages` branch. Finally,
we switch back to the master branch.

.. code-block:: bash

    git ci -m "Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`" && git push origin gh-pages ; git checkout master



ReadTheDocs
===========

What's nice about Python, Sphinx, and ReStructuredText that with a few simple
tricks your documentation is online. The key ingredient to make that happen
is the ``.readthedocs.yml`` file. This file tells the server what is
necessary to build your documentation and how to build it. Let's take a look.

.. literalinclude:: ../../../.readthedocs.yml
    :language: yaml
    :linenos:

There are a few important steps here. The first entry in this file that needs
to be manually set is the ``sphinx`` keyword. The location of the conf.py
needs to be set in relation to the repository. The second one is the ``formats``
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

