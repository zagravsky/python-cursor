from setuptools import find_packages, setup

setup(
    name='some_name',
    version='1.0.0',
    packages=find_packages(),
    include_packege_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
