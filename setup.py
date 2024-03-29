from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='cfn-transform',
    version='1.1.0',
    author = 'Trek10, Inc',
    author_email = 'package-management@trek10.com',
    license='MIT',
    url='https://github.com/trek10inc/cfn-transform',
    long_description=readme,
    long_description_content_type='text/markdown',
    py_modules=['transformation'],
    install_requires=[
        'cfn-lint~=0.83.2',
        'click==7.1.2',
    ],
    entry_points='''
        [console_scripts]
        cfn-transform=transformation:cli
    ''',
)
