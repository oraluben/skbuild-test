cmake_minimum_required(VERSION 3.23)
project(skbuild_test)

set(CMAKE_CXX_STANDARD 14)

find_package(PythonExtensions REQUIRED)

add_compile_definitions(Py_BUILD_CORE)

add_library(skbuild_test MODULE src/skbuild_test/library.cpp)
python_extension_module(skbuild_test)

install(TARGETS skbuild_test LIBRARY DESTINATION "${PYTHON_RELATIVE_SITE_PACKAGES_DIR}")
