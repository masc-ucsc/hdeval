from setuptools import setup, find_packages

setup(
    name='hdeval',
    version='0.1.0',
    packages=find_packages(),
    description='Hardware Description Evaluation Interface',
    long_description=open('README.md').read(),
    install_requires=[],
    author='MASC group',
    author_email='frabieik@ucsc.edu',
    url='https://github.com/masc-ucsc/hdeval'
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    package_data={'hdeval': ['hdeval-comb/*.hdeval']},
    scripts=['src/crypt', 'src/decrypt'],
    install_requires=[
        # List your dependencies here
    ],
    classifiers=[
        # Your classifiers
    ],
    python_requires='>=3.6',
)

