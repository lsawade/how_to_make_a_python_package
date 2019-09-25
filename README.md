# Sample package structure

This is a tiny, little package that shows how to easily setup a python 
package that includes

1. Modularized structure
2. A simple unittest setup using `.travis.yml`
3. An easy environment building option via `environment.yml`
4. Documentation of the code based on sphinx.

With this sample repository and a few instructions you should be good to go 
to create your own repositories that are simple to distribute and easily 
reproducible in the future.

## Where do you start?

The simplest way is to take a peak into the documentation which ich located 
here: <somelink>. There, I will explain and go through the few necessary 
steps starting with your modules.


## Installation of this package

A few simple steps:

```bash
# Create the conda environment and install dependencies
conda env create -f environment.yml

# Activate the conda environment
conda activate htmapp

# Install your package
pip install -e .
```

The `-e` simply let's you modify the package without having to reinstall it 
all the time.


