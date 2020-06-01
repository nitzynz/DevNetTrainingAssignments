import json

def dnac_parser():
    data = json.load(open("C:/Users/nitg/DevNet/DevNetTrainingAssignments/data/dnac_devices.json", 'r'))
    for device in data['response']:
        print('Device ID :', device['id'])
        print('Device Type :', device['type'])
        print('Device Family :', device['family'])
        print('Software Type :', device['softwareType'])
        print('Management IP Address :', device['managementIpAddress'],'\n')

dnac_parser()