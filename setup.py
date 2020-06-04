from setuptools import setup

# requirementes from requirements.txt
requirements = open(file='requirements.txt', mode='r', encoding='utf-8')

setup(
    name = 'RexBot',
    version = '1.3.0',
    description = 'Rexbot is a discord bot build to help in day to day tasks!',

    packages = [
        'rexbot'
    ],

    install_requires = [
        requirements
    ],

)