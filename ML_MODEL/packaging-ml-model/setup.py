import os
from setuptools import setup, find_packages


#Metadata of package
Name = 'prediction_model'
Description = 'Loan prediction model'
URL = 'https://github.com/bipulshahi'
Email = 'bipul@abc.com'
AUTHOR = 'Bipul Kumar Shahi'
REQUIRES_PYTHON = '>=3.7.0'


#get the list of packages to be installed automatically
pwd = os.path.abspath(os.path.dirname(__file__))
print(pwd)

def list_reqs(fname = 'requirements.txt'):
    with open(os.path.join(pwd,fname) , encoding='utf-8') as f:
        return f.read().splitlines()
    
#print(list_reqs())
PACKAGE_DIR = os.path.join(pwd,Name)
#print(PACKAGE_DIR)
about = {}
version_info = open(os.path.join(PACKAGE_DIR,"VERSION"))
_version = version_info.read().strip()
about['__version__'] = _version
#print(about)
version_info.close()


setup(
    name = Name,
    version = about['__version__'],
    description = Description,
    author = AUTHOR,
    author_email = Email,
    python_requires = REQUIRES_PYTHON,
    url = URL,
    packages = find_packages(exclude=('tests')),
    include_package_data=True,
    package_data={
        '':['*.txt', '*.md', '*.py' , 'datasets/*.csv' , 
            'trained_models/*.pkl', 'processing/*.py' , 'VERSION']
    },
    install_requires = list_reqs(),
    license = 'ABC',
    classifiers = [
        'License :: OSI Approved :: ABC License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
