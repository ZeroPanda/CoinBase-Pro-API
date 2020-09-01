# ----- Imports ---------------------------------------------------------------

from distutils.core import setup

# ----- Instructions ----------------------------------------------------------

REQUIREMENTS = [line.strip() for line in open(os.path.join(os.path.dirname(__file__),'requirements.txt')).readlines()]


setup(
    name = 'coinbasepro',
    version = '0.0.1',
    packages = ['coinbasepro'],
    url = 'https://github.com/ZeroPanda/CoinBase-Pro-API',
    license = 'MIT',
    install_requires=REQUIREMENTS,
    author = 'Shrey Shah',
    author_email = 'shreyshah31@gmail.com',
    description = 'Python Coinbase Pro API',
    classifiers = [
        'Development Status :: Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
