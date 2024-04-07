# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup, Extension
from glob import glob
import os
import sys

__version__ = "0.0.4"

# The main interface is through Pybind11Extension.
# * You can add cxx_std=11/14/17, and then build_ext can be removed.
# * You can set include_pybind11=false to add the include directory yourself,
#   say from a submodule.
#
# Note:
#   Sort input source files if you glob sources to ensure bit-for-bit
#   reproducible builds (https://github.com/pybind/python_example/pull/53)

# Detect if Eigen is installed
eigen_include_dir = "D:\\cpp_libs\\eigen-3.4.0\\"
if not os.path.exists(eigen_include_dir):
    sys.exit("Eigen not found. Please specify the correct path to Eigen.")


ext_modules = [
    Pybind11Extension("python_example",
        sorted(glob("src/*.cpp")),  # Sort source files for reproducibility
        # Example: passing in the version to the compiled code
        define_macros = [('VERSION_INFO', __version__)],
        include_dirs=[eigen_include_dir],
        ),
    # Extension(
    #     "python_example",  # Change this to your module name
    #     ["src/*.cpp"],  # Change this to your source file name
    #     include_dirs=[eigen_include_dir],
    #     language='c++'
    # ),
]

# Custom build_ext command to handle Eigen inclusion
class CustomBuildExtCommand(build_ext):
    def run(self):
        # Add the include directory of Eigen
        self.include_dirs.append(eigen_include_dir)
        build_ext.run(self)


setup(
    name="python_example",
    version=__version__,
    author="Sylvain Corlay",
    author_email="sylvain.corlay@gmail.com",
    url="https://github.com/pybind/python_example",
    description="A test project using pybind11",
    long_description="",
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
)
