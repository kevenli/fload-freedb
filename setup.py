from setuptools import setup, find_packages


def read_file(filename):
    with open(filename) as fp:
        return fp.read().strip()


setup(
    name='fload-freedb',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'fload_modules': [
            '_ = fload_freedb.stream'
        ]
    },
    install_requires=read_file('requirements.txt'),
)
