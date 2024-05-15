from oled import OLED
from machine import sleep

# 使用示例
oled = OLED(18, 19)
oled.clear()
oled.display('init...', 0, 0)


# 导入MPU6050类
from mpu6050 import MPU6050

# 初始化MPU6050
# 假设你的I2C引脚为GPIO22 (SCL) 和 GPIO21 (SDA)
mpu = MPU6050(scl_pin=32, sda_pin=33)

while True:
    sleep(200)
      # 获取倾斜角度
    tilt_angle = mpu.calculate_tilt_angle()
   
    # 在OLED上显示倾斜角度
    angle_text = "Angle: {:.2f}".format(tilt_angle)
    oled.display(angle_text, 0, 10)
    
    # 获取角速度数据
    gyro_rate = mpu.get_gyro_rate()
    gyro_y = gyro_rate['x']  # 关注y轴的角速度
    # 将倾斜角度和角速度格式化为一行文本
    gyro_text = "Gyro X: {:.2f}".format(gyro_y)
    oled.display(gyro_text, 0, 20)
