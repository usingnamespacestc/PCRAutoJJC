import subprocess
import time
import config
import cv2
import numpy as np
import sys
from PIL import Image
from io import StringIO


# adb执行单行代码
def exec(command):
    process = subprocess.Popen(config.path + ' ' + command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    return out.decode('gbk') + err.decode('gbk')


# adb顺序执行多行代码
def exec(command):
    cmd = config.path + ' ' + command[0]
    for i in range(len(command) - 1):
        cmd = cmd + ' && ' + config.path + ' ' + command[i + 1]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    return out.decode('gbk') + err.decode('gbk')


def getScreen():
    process = subprocess.Popen(config.path+' shell screencap -p', shell=True, stdout=subprocess.PIPE)
    screenshot = process.stdout.read()
    if sys.platform == 'win32':
        screenshot = screenshot.replace(b'\r\r\n', b'\n')
    # f = open('test.png', 'wb')
    # f.write(screenshot)
    # f.close()
    screenshot = cv2.imdecode(np.frombuffer(screenshot, np.uint8), cv2.IMREAD_COLOR)
    return screenshot


if __name__ == '__main__':
    # a = exec(['shell screencap -p /sdcard/screen.png', 'pull /sdcard/screen.png cache'])
    for i in range(10):
        start = time.clock()
        a = getScreen()
        end = time.clock()
        print(end - start)

    # cv2.imwrite('cache/screen.png', a)