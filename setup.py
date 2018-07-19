from setuptools import setup

setup(name='rocket_lander_gym',
      version='0.1',
      url='https://github.com/Jeetu95/Rocket_Lander_Gym',
      author='Subhajit Das',
      author_email='jeetudas95@gmail.com',
      description='Rocket Lander',
      license='MIT',
      packages=['rocket_lander_gym','rocket_lander_gym.envs'],
      install_requires=['gym','box2d-py','numpy']
      )