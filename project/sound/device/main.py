from machine import ADC, Pin
import lib.wifi as wifi
import time
from lib.mqtt import MQTTService


# 网络连接
def network_connect():
    # 连接wifi
    wifi.connect("COOL", "666123456")


# mqtt消息
def mqtt_connect():
    mqtt_service = MQTTService(
        server="192.168.0.119",
        client_id="cool_123",
        message_handler=mqtt_message_handler,
    )
    mqtt_service.connect()  # 连接到MQTT服务器
    mqtt_service.subscribe("cool")  # 订阅主题"cool"
    while True:
        mqtt_service.check_messages()  # 检查是否有消息到达


# mqtt消息处理
def mqtt_message_handler(topic, msg):
    print("Received on topic {}: {}".format(topic.decode(), msg.decode()))


# 录音
def mic_record():
    # 配置ADC引脚
    adc = ADC(Pin(35))  # GPIO35 (ADC1 channel 0)
    adc.width(ADC.WIDTH_12BIT)
    adc.atten(ADC.ATTN_11DB)

    # 录音参数
    SAMPLE_RATE = 16000  # 采样率 16kHz
    while True:
        data = adc.read()
        binary_data = bin(data)  # 将读取到的值转换为二进制
        print(binary_data)
        time.sleep(1 / SAMPLE_RATE)


# 主函数
if __name__ == "__main__":
    # 连接网络
    network_connect()
    # 连接MQTT服务器
    mqtt_connect()
    # 录音
    mic_record()
