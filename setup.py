from setuptools import setup

install_requires = {
      'os',
      'logging',
      # 'yaml'
}

setup(name='logger_yaml',
      version='0.1',
      description='Configure logger using YAML file (example included)',
      url='https://github.com/paulha/logger_yaml.git',
      author='Paul Hanchett',
      author_email='paul.hanchett@gmail.com',
      license='MIT',
      packages=['logger_yaml'],
      zip_safe=False)