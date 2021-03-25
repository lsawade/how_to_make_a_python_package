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
`https://packaging.python.org/tutorials/packaging-projects/`_.

I will however go through the basics as for example a step-wise breakdown.

Steps involved
==============

1. Create a ``setup.cfg`` and/or a ``setup.py``
2. Create a README
3. Create a LICENSE file and name it in ``setup.cfg``.
   Check out classifiers `here <https://pypi.org/classifiers/>`_.
4. Create a pyproject.toml (see the tutorial linked above).
4. Generating the distribution files
5. Create normal ``PyPi`` account and a test account.
6. Upload project using the PyPi
7. Check if you can install it using pip.

Before the steps your package should have this structure:

.. code-block:: bash

    how_to_make_a_python_package/
      |__ tests/
      |__ src/
      |    |__ matpy/
      |         |__ __init__.py
      |         |__ matrixmultiplication.py
      |__ tests/
      |    |____test_matmul_and_dot.py
      |__ setup.py
      |__ setup.cfg
      |__ LICENSE
      |__ README.md

and after following the steps 2 additional directories should appear:

.. code-block:: bash

    how_to_make_a_python_package/
      |__ build/
      |    |__bdist.macosx-10.9-x86_64
      |    |__lib
      |__ dist/
      |    |__ how_to_make_a_python_package-0.0.2.tar.gz
      |    |__ how_to_make_a_python_package-0.0.2-py3-none-any.whl
      |__ tests/
      |__ src/
      |    |__ matpy/
      |         |__ __init__.py
      |         |__ matrixmultiplication.py
      |__ tests/
      |    |____test_matmul_and_dot.py
      |__ setup.py
      |__ LICENSE
      |__ README.md

The build and dist are created to make it possible for other users to
download the package onto their system.

``setup.cfg``
____________

The ``setup.cfg`` (:ref:`setup-cfg`) makes sure that all the necessary info to
install and distribute your package is known. Important features to note are

- Specify all the requirements for the installation in the keyword argument

  .. code-block:: bash
    [options]
    install_requires = numpy; other_package

  in form illustrated above. If you don't and the package is installed into an
  environment that does not have the requirements installed, the module will
  error, of course. Hence, it is convenient to mention
  requirements here. Note that those packages will only be available in the
  installation process, not afterwards.

- You can also specify requirements for your python package that will be installed
  together with your package (i.e., the modules you import in your source code
  as for instance ``SciPy`` or ``NumPy``) by adding the following

  .. code-block:: bash
    [metdata]
    requires = numpy; scipy; my_odd_requirement
  
  In this case, the ``environment.yml`` becomes obsolete and we will only
  rely on Pypi.

- The classifiers have to have a certain format. If they aren't, the upload
  will fail. Check out classifiers `here <https://pypi.org/classifiers/>`_.

The rest is probably self-explaining.

Here, a setup file with all the bare necessities (Copied from
`https://packaging.python.org/tutorials/packaging-projects/`_):

.. code-block:: bash
    :linenos:

    [metadata]
    # replace with your username:
    name = example-pkg-YOUR-USERNAME-HERE
    version = 0.0.1
    author = Example Author
    author_email = author@example.com
    description = A small example package
    long_description = file: README.md
    long_description_content_type = text/markdown
    url = https://github.com/pypa/sampleproject
    project_urls =
        Bug Tracker = https://github.com/pypa/sampleproject/issues
    classifiers =
        Programming Language :: Python :: 3
        License :: OSI Approved :: MIT License
        Operating System :: OS Independent

    [options]
    package_dir =
        = src
    packages = find:
    python_requires = >=3.6

    [options.packages.find]
    where = src

The projects own ``setup.cfg`` is a bit longer and has more features. In addition,
we added a ``setup.py`` to support some more advanced functions.


LICENSE
_______

The license is important since PyPi won't be allowed to share your package if
it doesn't have a license. A good practice if you want your project to be
completely open is to just distribute it under an open GNU license. This let's
anyone use, change and then redistribute the code, but recognizes you as the
original author.


``README.md``
_____________

The ``README`` is essential for your project on GitHub either way, so I'm not
going to elaborate the need for it here.


Generating the files to upload
______________________________

Since we have all the files in place, it's time to distribution files. These
file are going to be upload to PyPi for anyone to download. To do that you'll
need a couple of things. First, let's update the ``setuptools`` and
``wheel``, which are used to create the ``build`` and ``dist`` files.

.. code-block:: bash

    python3 -m pip install --user --upgrade setuptools wheel


After updating the packages, we are ready to create the ``dist`` and the
``wheel``, which are needed for other people to install your package from
``PyPi`` via ``pip``.

.. code-block:: bash

    python3 setup.py sdist bdist_wheel

This results in two new directories ``build`` and ``dist``, which you'll need
both.

Uploading the distribution archives [TEST]
__________________________________________

The last step is to actually upload your package to ``PyPi``. For that you'll
need an account on `https://test.pypi.org/account/register/
<https://test.pypi.org/account/register/>`_. This is the package registry for
testing your upload etc. This is not meant for actual distribution.
Follow the steps to create the API token and add it to the ``~/.pypirc`` in
your home folder.

.. code-block:: bash

    [pypi]
        username = __token__
        password = pypi-<s0me_v3ry_l0ng_l3773r_and_numb3r_c0mb1nat10n>

If the file doesn't exist, create it. It allows you to safely upload data to
``PyPi``. Before uploading your package, it's good to have a upload test space.
I'll show in the next step what to do/change to actually distribute your
package. Let's first do the test round.

The next thing you'll need, is the package ``twine``.

.. code-block:: bash

    python3 -m pip install --user --upgrade twine

``twine`` is the package that helps uploading your package ``dist`` and
``build``. After updating, the ``twine`` package, you can upload your package
using

.. code-block:: bash

    python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

You will be asked for username and password in the process.

Installing the package
______________________

Now that it is uploaded you can try to install it using the command line and
pip:

.. code-block:: bash

    pip install -i https://test.pypi.org/simple/ <your_package_name>

Note that this line of code you can find on your project page on
`test.pypi.org <test.pypi.org>`_.

Final Upload!
_____________

When you are ready to distribute your package to ``PyPi``, make sure you
create an account on the actual ``PyPi``. Here I'm just reiterating the
points made on
`https://packaging.python.org/tutorials/packaging-projects/ <https://packaging.python.org/tutorials/packaging-projects/>`_:

    When you are ready to upload a real package to the Python Package Index
    you can do much the same as you did in this tutorial, but with these
    important differences:

    - Choose a memorable and unique name for your package.
      You don’t have to append your username as you did in the tutorial.
    - Register an account on https://pypi.org - note that these are two
      separate servers and the login details from the test server are not
      shared with the main server.
    - Use twine upload dist/* to upload your package and enter your
      credentials for the account you registered on the real PyPI. Now that
      you’re uploading the package in production, you don’t need to specify
      --repository-url; the package will upload to https://pypi.org/ by default.
    - Install your package from the real PyPI using pip install [your-package].

    At this point if you want to read more on packaging Python libraries
    here are some things you can do:

    - Read more about using setuptools to package libraries in Packaging and
      distributing projects.
    - Read about Packaging binary extensions.
    - Consider alternatives to setuptools such as flit, hatch, and poetry.
