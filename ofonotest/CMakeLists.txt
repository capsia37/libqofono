cmake_minimum_required(VERSION 3.14)
project(ofonotest LANGUAGES CXX)

find_package(Qt5 COMPONENTS Quick Qml REQUIRED)

add_executable(ofonotest
    main.cpp
)

target_link_libraries(ofonotest PRIVATE
    Qt5::Quick
    Qt5::Qml
)

set_target_properties(ofonotest PROPERTIES
    CXX_STANDARD 11
    CXX_STANDARD_REQUIRED ON
)

set(OFONO_EXAMPLES_PREFIX "/opt/examples/libqofono-qt${QT_MAJOR_VERSION}")

install(TARGETS ofonotest
    RUNTIME DESTINATION ${OFONO_EXAMPLES_PREFIX}
)

install(FILES qml/ofonotest/main.qml
    DESTINATION ${OFONO_EXAMPLES_PREFIX}/qml/ofonotest
)
