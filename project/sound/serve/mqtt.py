import paho.mqtt.client as mqtt

# MQTT 服务器地址
MQTT_HOST = "192.168.0.119"
MQTT_PORT = 1883  # 默认MQTT端口
MQTT_KEEPALIVE_INTERVAL = 45  # 保持连接的时间间隔


# 当客户端从服务器收到连接响应时的回调
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # 订阅主题
    client.subscribe("cool")


# 当从服务器收到订阅的消息时的回调
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


# 创建 MQTT 客户端实例
client = mqtt.Client()

# 指定连接回调函数
client.on_connect = on_connect

# 指定接收消息的回调函数
client.on_message = on_message

# 连接 MQTT 服务器
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

# 进行网络堵塞循环
client.loop_forever()
