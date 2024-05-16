import sys
sys.path.append('/lib')
from machine import Pin, SoftI2C
import ssd1306

class OLED:
    """
    用于控制SSD1306 OLED显示屏的类。
    """

    def __init__(self, scl_pin, sda_pin):
        """
        初始化OLED显示屏。

        :param scl_pin: I2C时钟线的引脚。
        :param sda_pin: I2C数据线的引脚。
        """
        self.i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))
        self.oled = ssd1306.SSD1306_I2C(128, 64, self.i2c)

    def display(self, text, x, y):
        """
        显示文本。

        :param text: 要显示的文本。
        :param x: 文本显示的X轴位置。
        :param y: 文本显示的Y轴位置。
        """
        self.oled.fill_rect(x, y, 128, 10, 0)  # 擦除旧文本
        self.oled.text(text, x, y)             # 显示新文本
        self.oled.show()                       # 更新显示

    def clear(self):
        """
        清除屏幕。
        """
        self.oled.fill(0)  # 使用黑色填充整个屏幕
        self.oled.show()   # 更新显示

