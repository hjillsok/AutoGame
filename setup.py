from setuptools import setup, find_packages

setup(name='AutoGame',
    version='0.0.0',
    url='https://github.com/hjillsok/AutoGame',
    description='A dumb auto-playing roguelike',
    author='Brian Marble',
    author_email='hjillsok@hotmail.com',
    license='MIT',
    zip_safe=False,
    packages=find_packages(exclude=['tests']),
#    install_requires=[
#        'requests==2.11.1',
#        'gcloud==0.17.0',
#        'oauth2client==3.0.0',
#        'requests_toolbelt==0.7.0',
#        'python_jwt==2.0.1',
#        'pycryptodome==3.4.3'
#    ]
)
