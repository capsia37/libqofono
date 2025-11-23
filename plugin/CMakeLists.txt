project(QOfonoQtDeclarative LANGUAGES CXX)

set(PLUGIN_SOURCES
    qofonodeclarativeplugin.cpp
    qofononetworkoperatorlistmodel.cpp
    qofonosimlistmodel.cpp
)

add_library(QOfonoQtDeclarative SHARED ${PLUGIN_SOURCES})

target_include_directories(QOfonoQtDeclarative PRIVATE
    ${CMAKE_SOURCE_DIR}/src
)

target_link_libraries(QOfonoQtDeclarative PRIVATE
    Qt5::Qml
    Qt5::DBus
    qofono-qt${QT_MAJOR_VERSION}
)

install(TARGETS QOfonoQtDeclarative
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}/qt5/qml/QOfono
)

install(FILES qmldir plugins.qmltypes
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/qt5/qml/QOfono
)