from setuptools import setup, find_packages

with open("README", 'r') as f:
    long_description = f.read()

#with open('LICENSE') as f:
#    license = f.read()


setup(
    name='music-tree',
    version='0.0.1',
    description='A useful module',
    # license="MIT",
    long_description=long_description,
    author='deitry',
    author_email='dm.s.vornychev@gmail.com',
    # url="http://www.foopackage.com/",

    #namespace_packages=['src'],
    packages=find_packages(),
    #[
    #    'src.base'
    #],

    # install_requires=['bar', 'greek'], #external packages as dependencies
    #scripts=[
    #         'scripts/cool',
    #         'scripts/skype',
    #        ]
)
