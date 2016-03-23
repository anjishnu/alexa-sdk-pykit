#!/usr/bin/env python

from distutils.core import setup

setup(name='ask-alexa-pykit',
      version='0.4',
      description="Minimalist SDK for developing skills for Amazon's Alexa Skills Kit",
      author='Anjishnu Kumar',
      author_email='anjishnu.kr@gmail.com',
      url='https://github.com/anjishnu/ask-alexa-pykit',
      packages=['ask'], #FIXME collides with https://pypi.python.org/pypi/ask/0.0.8
      license='MIT',
     )
