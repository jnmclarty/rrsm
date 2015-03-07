import os

from setuptools import setup

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()
        
v = '0.1.0'
print "Setting up rrsm" 
  
setup(name = "rrsm",
      version = v,
      packages = ['rrsm'],
      description = 'Readable run-time state machine',
      long_description=(read('README.rst')),    
      author = "Jeffrey McLarty",
      author_email = "jeffrey.mclarty@gmail.com",
      url = 'https://github.com/jnmclarty/rrsm',
      download_url = 'https://github.com/jnmclarty/rrsm/tarball/' + v,    
      keywords = "readable runtime run-time finite state machine".split(" "),
      classifiers = ['Development Status :: 1 - Planning',
                     'License :: OSI Approved :: MIT License',
                     'Intended Audience :: Developers',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python :: 2.7'])