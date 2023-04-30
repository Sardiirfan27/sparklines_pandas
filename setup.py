from setuptools import setup
from sparklines import __version__
setup(
    name='sparklines',
    version=__version__,
    description='creating sparklines on a pandas dataframe',
    url='https://github.com/sardiirfan27/sparklines_pandas',
    author='Sardi Irfansyah',
    author_email='sardiirfan27@gmail.com',
    packages=['sparklines'],
    install_requires=[
        'numpy',
        'pandas',
	'matplotlib',
    ],
)
