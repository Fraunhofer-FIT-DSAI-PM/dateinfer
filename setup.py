from distutils.core import setup
import re


def get_version(version_file):
    pattern = r"^__version__ = ['\"]([^'\"]*)['\"]"
    match = re.search(pattern, open(version_file, "rt").read(), re.MULTILINE)
    if match:
        return match.group(1)

    raise RuntimeError("Unable to find version string in %s." % (version_file,))


setup(
    name='guesstidate',
    version=get_version("guesstidate/__init__.py"),
    packages=['guesstidate'],
    url='https://github.com/Fraunhofer-FIT-DSAI-PM/guesstidate',
    license='Apache 2.0',
    author='Jeffrey Starr, Fraunhofer FIT',
    author_email='will@pedalwrencher.com, sebastiaan.van.zelst@fit.fraunhofer.de, alessandro.berti@fit.fraunhofer.de',
    description="Infers date format from examples"
)
