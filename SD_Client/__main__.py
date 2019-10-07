import os
import time
import yaml
import logging
from opcua import Client


def main():
    directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_file_name = os.path.join(directory, 'conf', 'prod.yaml')
    if not os.path.exists(config_file_name):
        config_file_name = os.path.join(directory, 'conf', 'dev.yaml')
    with open(config_file_name, 'r') as ymlfile:
        config = yaml.load(ymlfile)

    logger = logging.getLogger(__name__)

    while True:
        sd_client = Client('opc.tcp://' + config['discovery_server']['hostname'] + ':'
                        + str(config['discovery_server']['port']) + '/')

        # Get device location
        if config['device']['location']:
            location = config['device']['location']
        else:
            device_client = Client('opc.tcp://' + str(config['device']['local_opcua_server']) + ':'
                                   + str(config['device']['local_opcua_port']) + '/')
            try:
                device_client.connect()
                root_node = device_client.get_root_node()
                location_node = root_node.get_child(['0:Objects', '2:iot_ready_kit', '2:carriage_location'])
                location = location_node.get_value()
                device_client.disconnect()
            except Exception as e:
                location = 'na'
                logger.critical("Error while determining location: {0}".format(e))

        # Update service discorvery
        try:
            sd_client.connect()
            root_node = sd_client.get_root_node()
            update_device = root_node.get_child(['0:Objects', '4:service_discovery', '4:update-device'])
            if update_device:
                root_node.call_method(update_device, config['device']['name'], config['device']['hostname'],
                                      config['device']['device_class'], location)
            sd_client.disconnect()
        except Exception as e:
            logger.critical("Error while update_device: {0}".format(e))

        time.sleep(config['discovery_server']['update_every_sec'])


if __name__ == '__main__':
    main()
