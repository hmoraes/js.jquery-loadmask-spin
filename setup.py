from setuptools import setup, find_packages
import os

version = '1.2.0'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'jquery_loadmask_spin', 'test.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.jquery_loadmask_spin',
    version=version,
    description="fanstatic jQuery Loadmask Spin.",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Heberte Fernandes de Moraes',
    author_email='brebete@gmail.com',
    url='https://github.com/hmoraes/js.jquery-loadmask-spin',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'fanstatic[cssmin]',
        'fanstatic[jsmin]',
        'setuptools',
        'js.jquery>=1.9.0',
    ],
    entry_points={
        'fanstatic.libraries': [
            'jquery_loadmask_spin = js.jquery_loadmask_spin:library',
        ],
    },
)
