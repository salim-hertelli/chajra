from setuptools import setup, find_packages

setup(
    name='chajra',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        "pydantic"
    ],
    entry_points={
        'console_scripts': [
            'chajra=chajra.main:main',
        ],
    },
    author='Salim Hertelli',
    # author_email='your.email@example.com',
    description='A simple CLI tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/salim-hertelli/chajra',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)