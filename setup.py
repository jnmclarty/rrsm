from setuptools import setup, find_packages

with open('README.rst') as file:
    long_description = file.read(
    
setup(
    name = "",
    version = "0.1",
    packages = find_packages(),

    # metadata for upload to PyPI
    author = "Jeffrey McLarty",
    author_email = "jeffrey.mclarty@gmail.com",
    description = "This is an Example Package",
    license = "PSF",
    keywords = "readable runtime run-time finite state machine"
)