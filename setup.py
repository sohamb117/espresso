from setuptools import setup

setup(
    name='espresso',
    packages=['espresso'],
    include_package_data=True,
    install_requires=[
        'flask',
		'shortuuid',
		'blake3'
    ],
)