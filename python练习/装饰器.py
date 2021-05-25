class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 定义计算面积的方法使用@property将其转为属性
    @property
    def area(self):
        return self.width * self.height


# 创建实例
rect = Rect(20, 30)
print('面积为：', rect.area)