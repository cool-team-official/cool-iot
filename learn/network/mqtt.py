from lib.mqtt import MQTTService
import lib.wifi as wifi

# 连接wifi
wifi.connect("COOL", "666123456")


# 自定义消息处理函数
def custom_message_handler(topic, msg):
    print("Received on topic {}: {}".format(topic.decode(), msg.decode()))


# 创建MQTT服务实例，并指定自定义的消息处理函数
mqtt_service = MQTTService(
    server="192.168.0.119",
    client_id="cool_123",
    message_handler=custom_message_handler,
)
mqtt_service.connect()  # 连接到MQTT服务器
mqtt_service.subscribe("cool")  # 订阅主题"cool"
while True:
    mqtt_service.check_messages()  # 检查是否有消息到达
