from setuptools import find_packages, setup

setup(
    name='Car_a_small_site',
    version='1.0.0',
    description='First step in Flask - Car site',
    author='Dmytro Melnyk',
    author_email='ekut2104@gmail.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'flask',
    ],
)