from setuptools import setup, find_packages

setup(
    name='hdeval',
    version='0.1.0',
    description='Hardware Description Evaluation Interface',
    long_description=open('README.md').read(),
    author='MASC group',
    author_email='frabieik@ucsc.edu',
    url='https://github.com/masc-ucsc/hdeval',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    package_data={'hdeval': ['hdeval-comb/*.hdeval']},
    scripts=[
        'src/decrypt',  # Ensure this is a script and has execute permissions
    ],
    install_requires=[
        'pyyaml>=6.0.2',  # Add your dependencies here
    ],
    classifiers=[
        # Add your classifiers here
    ],
    python_requires='>=3.6',
)

