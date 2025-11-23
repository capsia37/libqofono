find_package(Qt5 REQUIRED COMPONENTS Core Test DBus)

file(GLOB TEST_SRCS "tst_*.cpp")

set(QOFONO_SRC_DIR ${CMAKE_SOURCE_DIR}/src)

foreach(SRC ${TEST_SRCS})
  get_filename_component(TEST_NAME ${SRC} NAME_WE)
  add_executable(${TEST_NAME} ${SRC})
  target_include_directories(${TEST_NAME} PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/../lib
    ${CMAKE_CURRENT_SOURCE_DIR}/..
    ${QOFONO_SRC_DIR}
  )
  target_link_libraries(${TEST_NAME} PRIVATE Qt5::Test Qt5::Core Qt5::DBus qofono-qt${QT_MAJOR_VERSION})
  add_test(NAME ${TEST_NAME} COMMAND ${TEST_NAME})
endforeach()
