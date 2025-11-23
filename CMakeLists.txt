cmake_minimum_required(VERSION 3.14)
project(libqofono LANGUAGES CXX)

set(QT_MAJOR_VERSION 5 CACHE STRING "Qt major version (fixed to 5)")

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)

enable_testing()

add_subdirectory(src)
add_subdirectory(plugin)
add_subdirectory(test)
add_subdirectory(ofonotest)
