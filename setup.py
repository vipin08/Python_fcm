from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='python_fcm',
      version='0.2',
      description='Simple FCM notification',
      long_description='Simple FCM notification',
      url='http://github.com/vipin08/halofun',
      author='Vipin Kumar',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      # entry_points = {
      #   'console_scripts': ['halo-fun=halofun.command_line:main'],
      # },
      author_email='vpnkumar.kumar1@gmail.com',
      license='MIT',
      packages=['python_fcm'],
      test_suite='nose.collector',
      # scripts=['bin/halo-fun'],
      tests_require=['nose'],
      # install_requires=[
      #     'markdown',
      # ],
      zip_safe=False)