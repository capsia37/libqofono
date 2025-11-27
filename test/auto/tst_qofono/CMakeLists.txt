cmake_minimum_required(VERSION 3.25.0 FATAL_ERROR)
project(tst_qofonotest LANGUAGES CXX)

add_executable(tst_qofonotest
    tst_qofonotest.cpp
)

target_include_directories(tst_qofonotest PRIVATE
    ${CMAKE_SOURCE_DIR}/src
)

target_link_libraries(tst_qofonotest PRIVATE
    Qt5::Test
    Qt5::DBus
    qofono-qt${QT_MAJOR_VERSION}
)

install(TARGETS tst_qofonotest
    RUNTIME DESTINATION /opt/tests/libqofono-qt${QT_MAJOR_VERSION}
)
