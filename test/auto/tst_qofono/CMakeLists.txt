cmake_minimum_required(VERSION 3.14)
project(tst_qofonotest LANGUAGES CXX)

find_package(Qt5 COMPONENTS Test DBus REQUIRED)

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

set_target_properties(tst_qofonotest PROPERTIES
    CXX_STANDARD 11
    CXX_STANDARD_REQUIRED ON
)

install(TARGETS tst_qofonotest
    RUNTIME DESTINATION /opt/tests/libqofono-qt${QT_MAJOR_VERSION}
)
