Distributing your package
-------------------------

There are many ways of install a python packaging. The simplest maybe just
copying the repository, `cd`-ing into the directory, and then just running

.. code-block:: bash

    pip install -e .

provided a ``setup.py`` file. This approach, however, would make it extremely
hard and uncontrollable to integrate your package into other projects. In
this chapter, a few approaches are shown on how to make your packages easily
accessible to others through the PyPi package manager.

Installing your package using the source code
+++++++++++++++++++++++++++++++++++++++++++++

Just like in the first paragraph the simplest way of installing your package
without going through the hassle of distribution is

.. code-block:: bash

    git clone https://github.com/lsawade/how_to_make_a_python_package
    cd how_to_make_a_python_package
    pip install -e .

This approach is simple and useful as long as you are the only one using the
code. As soon as other people are starting to use it, this approach maybe too
simple.


Distributing you code using PyPi
++++++++++++++++++++++++++++++++

When you want more people to use your packages it becomes crucial to
distribute them using a package manager. The most popular is PyPi which you
have probably come across already when you installed a package using ``pip
install <some_package>``. I don't want to get too crazy with the instructions
here because you can find most of the necessary details
`here <https://packaging.python.org/tutorials/packaging-projects/>`_.

I will however go through the basics as for example a step-wise breakdown.

Steps involved
==============

1. Create a ``setup.py``
2. Create a README
3. Create a LICENSE file and name it in ``setup.py``.
   Check out classifiers `here <https://pypi.org/classifiers/>`_.
4.

Before the steps your package should have this structure:

.. code-block::

    how_to_make_a_python_package/
      |__ tests/
      |__ matpy/
      |    |__ __init__.py
      |    |__ matrixmultiplication.py
      |__ tests/
      |    |____test_matmul_and_dot.py
      |__ setup.py
      |__ LICENSE
      |__ README.md

and after following the steps 2 additional directories should appear:

.. code-block::

    how_to_make_a_python_package/
      |__ build/
      |    |__bdist.macosx-10.9-x86_64
      |    |__lib
      |__ dist/
      |    |__ how_to_make_a_python_package-0.0.2.tar.gz
      |    |__ how_to_make_a_python_package-0.0.2-py3-none-any.whl
      |__ tests/
      |__ matpy/
      |    |__ __init__.py
      |    |__ matrixmultiplication.py
      |__ tests/
      |    |____test_matmul_and_dot.py
      |__ setup.py
      |__ LICENSE
      |__ README.md

The build and dist are created to make it possible for other users to
download the package onto their system.

``setup.py``
____________

The ``setup.py`` (:ref:`setup-py`) makes sure that all the necessary info to
install and distribute your package is known. Important features to note are

- If you choose to load the long description from a text file that is not an
  ``.rst`` file, you need to specify the file type using the keyword argument

  .. code-block:: python

      long_description_content_type="text/markdown"

  if the file type is MarkDown for example.

- Specify all the requirements for the installation in the keyword argument

  .. code-block:: python

      install_requires=["numpy", "<other_package>"]

  in form of a list. If you don't and the package is installed into an
  environment that does not have the requirements installed, the module will
  error, of course. Hence, it is convenient to mention
  requirements here.

- The classifiers have to have a certain format. If they aren't, the upload
  will fail. Check out classifiers `here <https://pypi.org/classifiers/>`_.

The rest is probably self-explaining.

LICENSE
_______

The license is important since PyPi won't be allowed to share your package if
it doesn't have a license. A good practice if you want your project to be
completely open is to just distribute it under an open GNU license. This let's
anyone use, change and then redistribute the code, but recognizes you as the
original author.


``README.md``
_____________

The ``README`` is essential for your project on GitHub either way, os I'm not
going to elaborate the need for it here.



