from setuptools import setup, find_packages

_locals = {}
execfile('tessera/api/_version.py', _locals)
version = _locals['__version__']

setup(
    name='tessera-client',
    version=version,
    description='Data model and API client for tessera',
    license='Apache',

    author='Urban Airship',
    url='https://github.com/urbanairship/tessera-client',

    packages=find_packages(),
    install_requires=[
        x.strip()
        for x in open('requirements.txt').readlines()
        if x and not x.startswith('#')
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: No Input/Output (Daemon)',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Systems Administration',
    ],
)
