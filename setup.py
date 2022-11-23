from pathlib import Path

from skbuild import setup

# scikit-build/scikit-build#521 to workaround `pip install .`
for i in (Path(__file__).resolve().parent / "_skbuild").rglob("CMakeCache.txt"):
    i.unlink()

setup(
    name='skbuild_test',
    version='0.0.1',
    packages=['skbuild_test'],
    package_dir={'': 'src'},
    python_requires='>=3.8.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
