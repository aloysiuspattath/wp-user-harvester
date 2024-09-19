from setuptools import setup

setup(
    name='wp_user_harvester',
    version='1.0',
    scripts=['wp_user_harvester.py'],
    install_requires=[
        'requests',
        'tqdm',
        'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
            'wp_user_harvester=wp_user_harvester:main',
        ],
    },
    description='A script to harvest user information from WordPress sites',
    author='Aloysius Pattath',
    url='https://github.com/aloysiuspattath',
)
