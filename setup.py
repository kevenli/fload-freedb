from setuptools import setup, find_packages


def read_file(filename):
    with open(filename) as fp:
        return fp.read().strip()


setup(
    name='fload-freedb',
    version='0.0.1',
    description='A fload plugin work together with freedb', 
    packages=find_packages(),
    entry_points={
        'fload_modules': [
            '_ = fload_freedb.stream'
        ]
    },
    author='Keven Li',
    author_email='pbleester@gmail.com',
    url='http://github.com/kevenli/fload-freedb',
    install_requires=read_file('requirements.txt'),
)
