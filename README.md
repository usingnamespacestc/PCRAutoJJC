# PCRBoxRecognizer
使用OpenCV进行角色的自动识别
## 环境
本人使用了python3.6版本，需要依赖的包在requirements.txt中，安装方法`pip install requirements.txt`，也可视情况使用`conda install`指令进行安装，方法不再赘述。
## 函数使用说明
### findTemplateFromSource(source, template, value, width)
#### 功能
在图片中找到模板图标并返回图标位置的中心。函数返回值为形如`[{'x': 0, 'y': 0}, {'x': 100, 'y': 100}]`。~~暂未去重。~~已做去重处理。
#### 参数
##### source和template
source是查找的图片，template是查找的角色图标，两个参数目前均为传入path即可，函数执行过程中会读取图片（日后会优化为一开始全部读取进内存中）。
##### value
value为检测的阈值，越高越严格，可设置为0.6。
##### width
width为模板图片需要缩放到的宽度（因为角色头像是正方形所以高度和宽度相等），只有当模板和被搜索图片中的元素大小相近时才能匹配到。
