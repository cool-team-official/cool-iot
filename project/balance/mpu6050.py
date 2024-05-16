import machine
import math

class MPU6050:
    """
    用于读取MPU6050陀螺仪和加速度计数据的工具类。
    """

    def __init__(self, scl_pin, sda_pin):
        """
        初始化MPU6050。

        :param scl_pin: I2C时钟线的引脚。
        :param sda_pin: I2C数据线的引脚。
        """
        self.i2c = machine.SoftI2C(scl=machine.Pin(scl_pin), sda=machine.Pin(sda_pin))
        self.address = 0x68  # MPU6050 I2C 地址
        self.i2c.writeto_mem(self.address, 0x6B, b'\x00')  # 唤醒MPU6050

    def read_raw_data(self, addr):
        """
        从MPU6050读取原始数据。

        :param addr: 寄存器地址。
        :return: 原始数据值。
        """
        high = self.i2c.readfrom_mem(self.address, addr, 1)
        low = self.i2c.readfrom_mem(self.address, addr+1, 1)
        value = (high[0] << 8) | low[0]

        if value > 32768:
            value -= 65536
        return value

    def get_accel_data(self):
        """
        获取加速度数据。

        :return: 加速度数据的字典（x, y, z）。
        """
        ax = self.read_raw_data(0x3B)
        ay = self.read_raw_data(0x3D)
        az = self.read_raw_data(0x3F)

        return {'x': ax, 'y': ay, 'z': az}

    def get_gyro_data(self):
        """
        获取陀螺仪数据。

        :return: 陀螺仪数据的字典（x, y, z）。
        """
        gx = self.read_raw_data(0x43)
        gy = self.read_raw_data(0x45)
        gz = self.read_raw_data(0x47)

        return {'x': gx, 'y': gy, 'z': gz}

    def calculate_tilt_angle(self):
        """
        计算倾斜角度。

        :return: 倾斜角度（以度为单位）。
        """
        accel_data = self.get_accel_data()
        try:
            # 以y轴和z轴为基准计算倾斜角度
            tilt_angle = math.degrees(math.atan2(accel_data['y'], accel_data['z']))
            return tilt_angle
        except ZeroDivisionError:
            return 0  # 如果z轴的读数为0，返回0度

    def get_gyro_rate(self):
        """
        获取角速度。

        :return: 陀螺仪数据的字典（x, y, z），以度/秒为单位。
        """
        gyro_data = self.get_gyro_data()

        # MPU6050的陀螺仪敏感度，默认设置为±250度/秒
        scale = 131

        gyro_rate = {
            'x': gyro_data['x'] / scale,
            'y': gyro_data['y'] / scale,
            'z': gyro_data['z'] / scale
        }
        return gyro_rate
 
