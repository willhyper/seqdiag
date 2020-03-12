from setuptools import setup

setup(
    name='seqdiag',
    packages=['seqdiag'],
    version='0.1',
    description='sequence diagram',
    author='Chao-Wei Chen',
    author_email='willhyper@gmail.com',
    url='https://github.com/willhyper/seqdiag.git',
    keywords=['seqdiag'],
    license='MIT',
    entry_points={
        'console_scripts': [
            'seqdiag = seqdiag:main',
        ]
    },
    install_requires=['bokeh','flask'],
)
