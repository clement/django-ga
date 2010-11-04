# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from ga import VERSION
 
setup(
    name='django-ga',
    version=VERSION,
    description='Google analytics django helper',
    author='Clément Nodet',
    author_email='clement.nodet@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
