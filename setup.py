from distutils.core import setup


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
    url='https://github.com/nedap/dateinfer',
    license='Apache 2.0',
    author='Jeffrey Starr',
    author_email='will@pedalwrencher.com',
    description="Infers date format from examples"
)
