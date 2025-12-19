project(QOfonoQtDeclarative LANGUAGES CXX)

set(PLUGIN_SOURCES
    qofonodeclarativeplugin.cpp
    qofononetworkoperatorlistmodel.cpp
    qofonosimlistmodel.cpp
)

if(QT_MAJOR_VERSION STREQUAL "6")
    qt_policy(SET QTP0001 NEW)

    qt6_add_qml_module(
        QOfonoQtDeclarative
        URI QOfono
        VERSION 0.2
        SHARED
        PLUGIN_TARGET QOfonoQtDeclarative
        OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/QOfono
        SOURCES ${PLUGIN_SOURCES}
        NO_GENERATE_PLUGIN_SOURCE
        NO_PLUGIN_OPTIONAL
    )
else()
    add_library(QOfonoQtDeclarative SHARED ${PLUGIN_SOURCES})
endif()

target_include_directories(QOfonoQtDeclarative PRIVATE
    ${CMAKE_SOURCE_DIR}/src
)

target_link_libraries(QOfonoQtDeclarative PRIVATE
    ${QTQML_LIB}
    ${QTDBUS_LIB}
    qofono-qt${QT_MAJOR_VERSION}
)

if (QT_MAJOR_VERSION STREQUAL "5")
    install(TARGETS QOfonoQtDeclarative
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}/qt${QT_MAJOR_VERSION}/qml/QOfono
    )
else()
    install(TARGETS QOfonoQtDeclarative
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}/qt/qml/QOfono
    )
endif()

if(QT_MAJOR_VERSION STREQUAL "5")
    install(FILES qmldir plugins.qmltypes
        DESTINATION ${CMAKE_INSTALL_LIBDIR}/qt5/qml/QOfono
    )
endif()