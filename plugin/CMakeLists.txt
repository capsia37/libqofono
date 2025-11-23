cmake_minimum_required(VERSION 3.14)
project(QOfonoQtDeclarative LANGUAGES CXX)

find_package(Qt5 COMPONENTS Qml DBus REQUIRED)

set(PLUGIN_SOURCES
    qofonodeclarativeplugin.cpp
    qofononetworkoperatorlistmodel.cpp
    qofonosimlistmodel.cpp
)

add_library(QOfonoQtDeclarative SHARED ${PLUGIN_SOURCES})

target_include_directories(QOfonoQtDeclarative PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_SOURCE_DIR}/src
)

target_link_libraries(QOfonoQtDeclarative PRIVATE
    Qt5::Qml
    Qt5::DBus
    qofono-qt${QT_MAJOR_VERSION}
)

set_target_properties(QOfonoQtDeclarative PROPERTIES
    OUTPUT_NAME "QOfonoQtDeclarative"
    CXX_STANDARD 11
    CXX_STANDARD_REQUIRED ON
)

install(TARGETS QOfonoQtDeclarative
    LIBRARY DESTINATION lib
)

install(FILES qmldir plugin.json plugins.qmltypes
    DESTINATION lib/qt5/qml/QOfono
)

add_custom_command(
    OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/plugins.qmltypes
    COMMAND /bin/sh -c "qmlplugindump -nonrelocatable QOfono 0.2 > ${CMAKE_CURRENT_SOURCE_DIR}/plugins.qmltypes"
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    COMMENT "Generating plugins.qmltypes for QOfono"
    VERBATIM
)
add_custom_target(qmltypes DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/plugins.qmltypes)
