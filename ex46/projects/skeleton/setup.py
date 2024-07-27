try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'My Project',
        'author': 'MRXVIIX', 
        'url': 'https://github.com/MRXVIIX',
        'download_url': 'https://github.com/MRXVIIX/lpthw/tree/main/ex46',
        'author_email': 'iron86xxgamer@gmail.com',
        'version': '0.1'
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'ex46.py'
}

setup(**config)
