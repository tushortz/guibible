# GuiBible setup
# Last updated (TSK, 2015-09-21)

from sys import version
if version < '2.2.3':
	from distutils.dist import DistributionMetadata
	DistributionMetadata.classifiers = None
	DistributionMetadata.download_url = None
	
#from setuptools import setup
from distutils.core import setup

setup(
	name='guibible',
	version='0.1.4',
	description='Simple GUI for the Bible',
	long_description = open('README').read(),
	author='Taiwo Kareem',
	author_email='taiwo.kareem36@gmail.com',
	url='https://github.com/tushortz/guibible',
	packages=['guibible'],
	package_data={
		'guibible':["guibible/README.html"],
		},
	platforms='any',
	keywords='Bible, KJV, Graphical Bible, GUI Bible',
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Religion',
		'License :: OSI Approved',
		'Programming Language :: Python',
		'Topic :: Religion',
		'Programming Language :: Python :: 3',
	],
)
