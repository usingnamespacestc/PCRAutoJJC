#导入所需库文件
import cv2
import numpy as np
import imutils

def findTemplateFromSource(image, Target, value, widthPix):
    #加载原始RGB图像
    img_rgb = cv2.imread(image)
    #创建一个原始图像的灰度版本，所有操作在灰度版本中处理，然后在RGB图像中使用相同坐标还原
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    #加载将要搜索的图像模板
    template = cv2.imread(Target,0)
    #记录图像模板的尺寸
    w, h = template.shape[::-1]
    #对模板进行缩放
    resizedTemplate = imutils.resize(template, width=widthPix)
    #使用matchTemplate对原始灰度图像和图像模板进行匹配
    res = cv2.matchTemplate(img_gray, resizedTemplate, cv2.TM_CCOEFF_NORMED)
    #设定阈值
    threshold = value
    loc = np.where( res >= threshold)
    location = []
    #使用灰度图像中的坐标对原始RGB图像进行标记
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + widthPix, pt[1] + widthPix), (7,249,151), 2)
        location.append({'x': pt[0] + 0.5 * widthPix, 'y': pt[1] + 0.5 * widthPix})
    #查看三组图像(图像标签名称，文件名称)
    #cv2.imshow('Detected', img_rgb)
    #cv2.imshow('gray', img_gray)
    #cv2.imshow('template', template)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #cv2.imwrite('res.png', img_rgb, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
    cv2.imwrite('res.png', img_rgb)
    #print(widthPix)
    return location

if __name__ == '__main__':
    value = 0.6 #阈值，越高越严格
    image = 'source.png'
    Target = 'object.png'
    a = findTemplateFromSource(image, Target, value, 100)