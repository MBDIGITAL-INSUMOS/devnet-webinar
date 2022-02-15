from CUCMConnectorAXL import *
import logging

class JabberCreator(CUCMConnectorAXL):
    def add_jabber_device(self, device_name, lines, site, Location, username):
        """
            Creates a Jabber device with the specified settings
            This example takes as default many of the common settings, although it can be adjusted according to your needs
        """
        phone={
                    'name': device_name,
                    'devicePoolName': f'DP_{site}',
                    'ownerUserName': username,
                    #'description': f'({team}) Remote Agent - Site {site}',
                    'description': device_name,
                    'product': 'Cisco Unified Client Services Framework',
                    'class': 'Phone',
                    'protocol': 'SIP',
                    'protocolSide': 'User',
                    'locationName': f'LOC_{Location}',
                    'sipProfileName': 'Standard SIP Profile',
                    'commonPhoneConfigName': 'Standard Common Phone Profile',
                    'phoneTemplateName': 'Standard Client Services Framework',
                    'useTrustedRelayPoint': 'Default',
                    'builtInBridgeStatus': 'Default',
                    'packetCaptureMode': 'None',
                    'certificateOperation': 'No Pending Operation',
                    'deviceMobilityMode': 'Default',
                    'lines': {
                        'line': lines
                    }
                }

        try:
            return self._CLIENT.addPhone(phone)
        except Exception as e:
            if self._logger:
                self._logger.error(str(e))
            return f'ERROR: {str(e)}'