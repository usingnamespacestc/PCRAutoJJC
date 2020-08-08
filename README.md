# PCRBoxRecognizer
使用OpenCV进行角色的自动识别
## 环境
本人使用了python3.6版本，需要依赖的包在requirements.txt中，安装方法`pip install requirements.txt`，也可视情况使用`conda install`指令进行安装，方法不再赘述。
需要配合雷电模拟器使用，雷电模拟器的路径填写在config.py中，例：`path = 'D:/ChangZhi/dnplayer2/adb'`。
## 函数使用说明
### exec(command)
#### 功能
在adb中执行命令。
#### 返回值
当命令执行成功时返回执行后的标准输出，失败时返回错误信息。
#### 参数
##### command
字符串，为要执行的命令。例：`exec('shell netcfg')`。
### exec(command)
#### 功能
在adb中依次执行多条命令（重载）。
#### 返回值
当命令执行成功时返回执行后的标准输出，失败时返回错误信息。（执行多条命令各有成功失败的情况没有进行测试）
#### 参数
##### command
多条字符串构成的数组，为要执行的命令。例：`exec(['shell screencap -p /sdcard/screen.png', 'pull /sdcard/screen.png cache'])`。
### getScreen
#### 功能
获取当前屏幕截图。
#### 返回值
cv2的图片对象。
### findTemplateFromSource(source, template, value, width, height)
#### 功能
在图片中找到模板图标位置的中心。
#### 返回值
为找到的图标的中心位置，形如`[{'x': 0, 'y': 0}, {'x': 100, 'y': 100}]`。已做去重处理。
#### 参数
##### source和template
source是查找的图片，template是查找的角色图标，两个参数均为image对象。
##### value
value为检测的阈值，越高越严格，可设置为0.6。
##### width和height
width和height为模板图片需要缩放到的宽度和高度，只有当模板和被搜索图片中要寻找的元素大小相近时才能匹配到。
