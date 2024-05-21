from machine import ADC, Pin
import time

# 配置ADC引脚
adc = ADC(Pin(35))  # GPIO35 (ADC1 channel 0)
adc.width(ADC.WIDTH_12BIT)
adc.atten(ADC.ATTN_11DB)

# 录音参数
SAMPLE_RATE = 16000  # 采样率 16kHz


# 录音函数
def record():
    while True:
        data = adc.read()
        binary_data = bin(data)  # 将读取到的值转换为二进制
        print(binary_data)
        time.sleep(1 / SAMPLE_RATE)


# 启动录音
record()
