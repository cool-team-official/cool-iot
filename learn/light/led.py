# 点亮和熄灭LED灯

from machine import Pin  # 导入Pin类，用于操作GPIO
import time  # 导入time模块，用于时间相关的操作

led = Pin(32, Pin.OUT)  # 创建一个Pin对象，代表GPIO2，设置为输出模式

while True:  # 无限循环
    led.value(not led.value())  # 读取LED当前的值，取反后再设置回去，实现LED的闪烁
    time.sleep(1)  # 暂停1秒
