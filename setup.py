from setuptools import setup

setup(name='jalapeno',
      version='0.0',
      description='Journal and Presentation Figures and Movies with Matplotlib',
      url='https://github.com/michael-a-hansen/jalapeno',
      author='Mike Hansen',
      author_email='mike.hansen.utah@gmail.com',
      license='MIT',
      packages=['jalapeno'],
      install_requires=['numpy','matplotlib'],
      zip_safe=False)