from setuptools import setup, find_packages

setup(
    name='fibre',
    version='1.0.0',
    description='Calculateur de pertes en fibre optique',
    author='By Eddy Okito   eddyokito@gmail.com 2025',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'fibre=fibre._main_:fibre'
        ]
    },
    python_requires='>=3.6',
)
