from ppadb.client import Client
import time

def adb_connect():
    host = '127.0.0.1'
    port = 5037

    client = Client(host=host, port=port)
    find_devices = client.devices()

    if len(find_devices) == 0:
        print("No devices")
        quit()

    device = find_devices[0]
    print(device)

    return device, client

my_device, my_client = adb_connect()

my_device.shell('input keyevent 64')
time.sleep(3.0)