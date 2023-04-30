from setuptools import setup

setup(
    name='sparklines_pandas',
    version='0.1.0',
    description='creating sparklines on a pandas dataframe',
    url='https://github.com/sardiirfan27/sparklines_pandas',
    author='Sardi Irfansyah',
    author_email='sardiirfan27@gmail.com',
    packages=['sparklines_pandas'],
    install_requires=[
        'numpy',
        'pandas',
	'matplotlib',
    ],
)