from setuptools import setup, find_namespace_packages

setup(name='pyCliAddressBook',
      version='1.0.22',
      description='Personal assistant with command line interface',
      url='https://github.com/DmytroLievoshko/MyCopyOfPyCliAddressBook.git',
      author='Yurii Skiter, Valerii Sydorenko, Dmytro Levoshko',
      author_email='contract@restriction.com',
      license='MIT',
      packages=find_namespace_packages(),
      include_package_data=True,
      install_requires=['python-dateutil<=2.8.2',
                        'rich<=12.5.1', 'prompt-toolkit<=3.0.31', 'phonenumbers<=8.12.55'],
      entry_points={'console_scripts': [
          'assistant=pyCliAddressBook.main:cli']}
      )
