from setuptools import setup

setup(name='rocket_lander_gym',
      version='0.1',
      url='http://github.com/jeetu95/rocket',
      author='Subhajit Das',
      author_email='jeetudas95@gmail.com',
      description='Rocket Lander',
      license='MIT',
      packages=['rocket_lander_gym','rocket_lander_gym.envs'],
      install_requires=['gym','box2d-py','numpy']
      )