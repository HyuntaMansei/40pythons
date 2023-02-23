from ppadb.client import Client
import time

def adb_connect():
    host = '127.0.0.1'
    port = 5037

    # use default values
    client = Client()
    devices = client.devices()
    if len(devices) == 0:
        print('No device')
        quit()

    device = devices[0]

    return device, client

my_device, my_client = adb_connect()
print(my_device)
print(my_client)

#연결 후 작업 시작
my_device.shell('input keyevent 64')
time.sleep(2.0)

xyPosition = '423 136'
my_device.shell(f'input tap {xyPosition}')
time.sleep(2.0)

url = 'www.naver.com'
my_device.shell(f'input text {url}')
time.sleep(2.0)

my_device.shell('input keyevent 66')
time.sleep(2.0)

result = my_device.screencap()
with open('capture.png', 'wb') as fp:
    fp.write(result)
