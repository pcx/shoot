import setuptools


setuptools.setup(name='Shoot',
                 version='0.0.1',
                 author='Phaneendra Chiruvella',
                 author_email='hi@pcx.io',
                 packages=['shoot',],
                 url='https://github.com/pcx/shoot',
                 description='Kick-start your prototype with Django templates',
                 install_requires=["Django",],
                 entry_points={
                     'console_scripts': [
                         ['shoot = shoot.run:run',],
                     ]
                 },
                 package_data={'': ['LICENSE.txt', 'README.rst']},
                 include_package_data=True,
                 license=open('LICENSE').read(),
                 long_description=open('README.rst').read(),
             )
