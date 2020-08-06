from pynput.mouse import Button, Controller
import time
import win32clipboard


win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

mouse = Controller()
mouse.click(Button.right)

'''
print(mouse.position)
time.sleep(3)
print('The current pointer position is {0}'.format(mouse.position))

# set pointer positon
mouse.position = (277, 645)
print('now we have moved it to {0}'.format(mouse.position))

# 鼠标移动（x,y）个距离
mouse.move(5, -5)
print(mouse.position)

mouse.click(Button.right)

mouse.press(Button.left)
mouse.release(Button.left)

# Double click
mouse.click(Button.left, 1)

# scroll two steps down
mouse.scroll(0, 500)
'''