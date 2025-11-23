find_package(Qt5 COMPONENTS Core DBus XmlPatterns REQUIRED)

file(GLOB_RECURSE QOFONO_SOURCES CONFIGURE_DEPENDS "*.cpp")

add_library(qofono-qt${QT_MAJOR_VERSION} SHARED ${QOFONO_SOURCES})

target_include_directories(qofono-qt${QT_MAJOR_VERSION}
    PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}
)

set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_assisted_satellite_navigation.xml
    PROPERTIES
    CLASSNAME OfonoAssistedSatelliteNavigation
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_audio_settings.xml
    PROPERTIES
    CLASSNAME OfonoAudioSettings
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_call_barring.xml
    PROPERTIES
    CLASSNAME OfonoCallBarring
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_call_forwarding.xml
    PROPERTIES
    CLASSNAME OfonoCallForwarding
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_callmeter.xml
    PROPERTIES
    CLASSNAME OfonoCallMeter
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_call_settings.xml
    PROPERTIES
    CLASSNAME OfonoCallSettings
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_callvolume.xml
    PROPERTIES
    CLASSNAME OfonoCallVolume
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_cell_broadcast.xml
    PROPERTIES
    CLASSNAME OfonoCellBroadcast
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_connection_context.xml
    PROPERTIES
    CLASSNAME OfonoConnectionContext
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_connection_manager.xml
    PROPERTIES
    CLASSNAME OfonoConnectionManager
    INCLUDE ${CMAKE_CURRENT_SOURCE_DIR}/dbustypes.h
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_location_reporting.xml
    PROPERTIES
    CLASSNAME OfonoLocationReporting
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_handsfree.xml
    PROPERTIES
    CLASSNAME OfonoHandsfree
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_handsfree_audio_agent.xml
    PROPERTIES
    CLASSNAME OfonoHandsfreeAudioAgent
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_handsfree_audio_card.xml
    PROPERTIES
    CLASSNAME OfonoHandsfreeAudioCard
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_handsfree_audio_manager.xml
    PROPERTIES
    CLASSNAME OfonoHandsfreeAudioManager
    INCLUDE ${CMAKE_CURRENT_SOURCE_DIR}/dbustypes.h
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_manager.xml
    PROPERTIES
    CLASSNAME OfonoManager
    INCLUDE ${CMAKE_CURRENT_SOURCE_DIR}/dbustypes.h
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_message.xml
    PROPERTIES
    CLASSNAME OfonoMessage
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_message_manager.xml
    PROPERTIES
    CLASSNAME OfonoMessageManager
    INCLUDE ${CMAKE_CURRENT_SOURCE_DIR}/dbustypes.h
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_messagewaiting.xml
    PROPERTIES
    CLASSNAME OfonoMessageWaiting
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_modem.xml
    PROPERTIES
    CLASSNAME OfonoModem
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_network_operator.xml
    PROPERTIES
    CLASSNAME OfonoNetworkOperator
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_network_registration.xml
    PROPERTIES
    CLASSNAME OfonoNetworkRegistration
    INCLUDE ${CMAKE_CURRENT_SOURCE_DIR}/dbustypes.h
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_phonebook.xml
    PROPERTIES
    CLASSNAME OfonoPhonebook
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_push_notification.xml
    PROPERTIES
    CLASSNAME OfonoPushNotification
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_radio_settings.xml
    PROPERTIES
    CLASSNAME OfonoRadioSettings
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_simmanager.xml
    PROPERTIES
    CLASSNAME OfonoSimManager
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_smart_messaging.xml
    PROPERTIES
    CLASSNAME OfonoSmartMessaging
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_supplementary_services.xml
    PROPERTIES
    CLASSNAME OfonoSupplementaryServices
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_text_telephony.xml
    PROPERTIES
    CLASSNAME OfonoTextTelephony
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_voice_call.xml
    PROPERTIES
    CLASSNAME OfonoVoiceCall
)
set_source_files_properties(
    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_voicecallmanager.xml
    PROPERTIES
    CLASSNAME OfonoVoiceCallManager
    INCLUDE ${CMAKE_CURRENT_SOURCE_DIR}/dbustypes.h
)

qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_assisted_satellite_navigation.xml ofono_assisted_satellite_navigation_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_audio_settings.xml ofono_audio_settings_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_call_barring.xml ofono_call_barring_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_call_forwarding.xml ofono_call_forwarding_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_callmeter.xml ofono_callmeter_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_call_settings.xml ofono_call_settings_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_callvolume.xml ofono_callvolume_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_cell_broadcast.xml ofono_cell_broadcast_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_connection_context.xml ofono_connection_context_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_connection_manager.xml ofono_connection_manager_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_location_reporting.xml ofono_location_reporting_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_handsfree.xml ofono_handsfree_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_handsfree_audio_agent.xml ofono_handsfree_audio_agent_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_handsfree_audio_card.xml ofono_handsfree_audio_card_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_handsfree_audio_manager.xml ofono_handsfree_audio_manager_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_manager.xml ofono_manager_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_message.xml ofono_message_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_message_manager.xml ofono_message_manager_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_messagewaiting.xml ofono_messagewaiting_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_modem.xml ofono_modem_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_network_operator.xml ofono_network_operator_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_network_registration.xml ofono_network_registration_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_phonebook.xml ofono_phonebook_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_push_notification.xml ofono_push_notification_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_radio_settings.xml ofono_radio_settings_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_simmanager.xml ofono_simmanager_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_smart_messaging.xml ofono_smart_messaging_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_supplementary_services.xml ofono_supplementary_services_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_text_telephony.xml ofono_text_telephony_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_voice_call.xml ofono_voice_call_interface)
qt_add_dbus_interface(_dbus_ifaces ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_voicecallmanager.xml ofono_voicecallmanager_interface)
target_sources(qofono-qt${QT_MAJOR_VERSION} PRIVATE ${_dbus_ifaces})
target_include_directories(qofono-qt${QT_MAJOR_VERSION} PRIVATE ${CMAKE_CURRENT_BINARY_DIR})

# FIXME: qdbusxml2cpp doesn't use QMetaObject::invokeMethod(parent(), ...) to emit signals, when using the qt_add_dbus_adaptor generated adaptors because it is invoked with a parent class.
# Might be useful to set a specific parent class that implements all the methods to emit signals.
# For now, we manually invoke qdbusxml2cpp to generate the adaptors without a parent class.
#qt_add_dbus_adaptor(
#    _adaptor_files 
#    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_positioning_request_agent.xml
#    ${CMAKE_CURRENT_SOURCE_DIR}/qofonopositioningrequestagent.h
#    QOfonoPositioningRequestAgent
#    ofono_positioning_request_agent_adaptor
#    QOfonoPositioningRequestAgentAdaptor
#)
#qt_add_dbus_adaptor(
#    _adaptor_files 
#    ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_smart_messaging_agent.xml
#    ${CMAKE_CURRENT_SOURCE_DIR}/qofonosmartmessagingagent.h
#    QOfonoSmartMessagingAgent
#    ofono_smart_messaging_agent_adaptor
#    QOfonoSmartMessagingAgentAdaptor
#)

# Generate adaptor sources/headers into the CMake binary dir using qdbusxml2cpp.

# List of generated adaptor files
set(_adaptor_files
    ${CMAKE_CURRENT_BINARY_DIR}/ofono_positioning_request_agent_adaptor.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/ofono_positioning_request_agent_adaptor.h
    ${CMAKE_CURRENT_BINARY_DIR}/ofono_smart_messaging_agent_adaptor.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/ofono_smart_messaging_agent_adaptor.h
)

# Generate ofono_positioning_request_agent_adaptor.{cpp,h}
add_custom_command(
    OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/ofono_positioning_request_agent_adaptor.cpp ${CMAKE_CURRENT_BINARY_DIR}/ofono_positioning_request_agent_adaptor.h
    COMMAND qdbusxml2cpp -a ${CMAKE_CURRENT_BINARY_DIR}/ofono_positioning_request_agent_adaptor -N -c QOfonoPositioningRequestAgentAdaptor ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_positioning_request_agent.xml
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_positioning_request_agent.xml
    COMMENT "Generating QDBus adaptor for ofono_positioning_request_agent"
    VERBATIM
)

# Generate ofono_smart_messaging_agent_adaptor.{cpp,h}
add_custom_command(
    OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/ofono_smart_messaging_agent_adaptor.cpp ${CMAKE_CURRENT_BINARY_DIR}/ofono_smart_messaging_agent_adaptor.h
    COMMAND qdbusxml2cpp -a ${CMAKE_CURRENT_BINARY_DIR}/ofono_smart_messaging_agent_adaptor -N -c QOfonoSmartMessagingAgentAdaptor ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_smart_messaging_agent.xml 
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/dbus/ofono_smart_messaging_agent.xml
    COMMENT "Generating QDBus adaptor for ofono_smart_messaging_agent"
    VERBATIM
)

add_custom_target(qofono_adaptors ALL DEPENDS ${_adaptor_files})
add_dependencies(qofono-qt${QT_MAJOR_VERSION} qofono_adaptors)


target_sources(qofono-qt${QT_MAJOR_VERSION} PRIVATE ${_adaptor_files})
target_include_directories(qofono-qt${QT_MAJOR_VERSION} PRIVATE ${CMAKE_CURRENT_BINARY_DIR})
target_link_libraries(qofono-qt${QT_MAJOR_VERSION}
    PRIVATE Qt5::Core Qt5::DBus Qt5::XmlPatterns
)

install(TARGETS qofono-qt${QT_MAJOR_VERSION}
    LIBRARY DESTINATION lib
)

target_compile_definitions(qofono-qt${QT_MAJOR_VERSION} PRIVATE QOFONO_LIBRARY)
target_compile_options(qofono-qt${QT_MAJOR_VERSION} PRIVATE -Wno-unused-parameter)

# Install public headers (private headers ending with _p.h excluded)
file(GLOB PUBLIC_HEADER_FILES "${CMAKE_CURRENT_SOURCE_DIR}/*.h")
list(FILTER PUBLIC_HEADER_FILES EXCLUDE REGEX "_p\\.h$")
install(FILES ${PUBLIC_HEADER_FILES}
    DESTINATION include/qofono-qt${QT_MAJOR_VERSION}
)

# Install DBus XML files
install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/dbus/
    DESTINATION include/qofono-qt${QT_MAJOR_VERSION}/dbus
    FILES_MATCHING PATTERN "*.xml"
)

# Install .prf file
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/qofono-qt${QT_MAJOR_VERSION}.prf
    DESTINATION share/qt${QT_MAJOR_VERSION}/mkspecs/features
)

# Generate pkg-config file (qmake create_pc)
file(READ "${CMAKE_CURRENT_SOURCE_DIR}/version.pri" _vcontent)
string(REGEX MATCH "VERSION[ \t]*=[ \t]*([0-9.]+)" _match "${_vcontent}")
set(QOFONO_VERSION "${CMAKE_MATCH_1}")
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/qofono-qt.pc.in ${CMAKE_CURRENT_BINARY_DIR}/qofono-qt${QT_MAJOR_VERSION}.pc @ONLY)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/qofono-qt${QT_MAJOR_VERSION}.pc
    DESTINATION lib/pkgconfig
)
