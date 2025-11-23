cmake_minimum_required(VERSION 3.25.0 FATAL_ERROR)
project(libqofono-tests LANGUAGES CXX)

add_subdirectory(auto/tst_qofono)
add_subdirectory(auto/tests)
# add_subdirectory(auto/tst_location)