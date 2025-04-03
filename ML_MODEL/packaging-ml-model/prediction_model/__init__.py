import os
import sys

import pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from prediction_model.config import config

#print(os.path.join(config.PACKAGE_ROOT,'VERSION'))
version_file = open(os.path.join(config.PACKAGE_ROOT,'VERSION'))
#print(version_file.read())
__version__ = version_file.read().strip()
version_file.close()