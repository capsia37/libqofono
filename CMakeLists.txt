cmake_minimum_required(VERSION 3.12.0 FATAL_ERROR)

set(LIBQOFONO_VERSION "0.124" CACHE STRING "libqofono version")
set(QT_MAJOR_VERSION 5 CACHE STRING "Qt major version")

project(libqofono
    VERSION ${LIBQOFONO_VERSION}
    DESCRIPTION "Library for accessing the ofono daemon"
    HOMEPAGE_URL "https://github.com/sailfishos/libqofono"
    LANGUAGES CXX
)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)

enable_testing()

include(FeatureSummary)

# Prefer Qt5 by default; allow building with Qt6 by setting -DQT_MAJOR_VERSION=6
if(QT_MAJOR_VERSION STREQUAL "6")
    find_package(Qt6 COMPONENTS Core DBus Qml Quick Test)
    set_package_properties(Qt6
        PROPERTIES
        TYPE REQUIRED
        DESCRIPTION "Qt6 libraries"
        URL "https://www.qt.io"
    )
    set(QTCORE_LIB Qt6::Core)
    set(QTDBUS_LIB Qt6::DBus)
    set(QTQML_LIB Qt6::Qml)
    set(QTQUICK_LIB Qt6::Quick)
    set(QTTEST_LIB Qt6::Test)
else()
    find_package(Qt5 COMPONENTS Core DBus Qml Quick Test)
    set_package_properties(Qt5
        PROPERTIES
        TYPE REQUIRED
        DESCRIPTION "Qt5 libraries"
        URL "https://www.qt.io"
    )
    set(QTCORE_LIB Qt5::Core)
    set(QTDBUS_LIB Qt5::DBus)
    set(QTQML_LIB Qt5::Qml)
    set(QTQUICK_LIB Qt5::Quick)
    set(QTTEST_LIB Qt5::Test)
endif()

feature_summary(WHAT REQUIRED_PACKAGES_NOT_FOUND FATAL_ON_MISSING_REQUIRED_PACKAGES)

add_subdirectory(src)
add_subdirectory(plugin)
add_subdirectory(test)
add_subdirectory(ofonotest)
