# 控制LED的亮度

from machine import Pin, PWM  # 导入PWM类，用于操作PWM
import time  # 导入time模块，用于时间相关的操作

led = PWM(Pin(32), freq=500, duty=0)  # 创建一个PWM对象，设置频率为500Hz，占空比为0

while True:  # 无限循环
    for i in range(1024):  # 从0递增到1023
        led.duty(i)  # 设置PWM的占空比
        time.sleep(0.001)  # 暂停1毫秒
    for i in range(1023, -1, -1):  # 从1023递减到0
        led.duty(i)  # 设置PWM的占空比
        time.sleep(0.001)  # 暂停1毫秒
