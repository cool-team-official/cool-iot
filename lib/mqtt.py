from umqtt.simple import MQTTClient


# Mqtt服务 用于连接MQTT服务器  订阅主题 发布消息 server 为MQTT服务器地址 client_id 为客户端ID
class MQTTService:
    def __init__(self, server, client_id, message_handler=None):
        self.client = MQTTClient(client_id, server)
        self.message_handler = (
            message_handler if message_handler is not None else self.on_message
        )
        self.client.set_callback(self.message_handler)

    def connect(self):
        """连接到MQTT服务器"""
        self.client.connect()

    def disconnect(self):
        """从MQTT服务器断开连接"""
        self.client.disconnect()

    def subscribe(self, topic):
        """订阅MQTT主题"""
        self.client.subscribe(topic)

    def publish(self, topic, message):
        """发布消息到MQTT主题"""
        self.client.publish(topic, message.encode())

    def on_message(self, topic, msg):
        """默认接收到消息时的回调函数"""
        print((topic, msg.decode()))

    def wait_message(self):
        """等待接收消息"""
        self.client.wait_msg()

    def check_messages(self):
        """检查是否有消息到达"""
        self.client.check_msg()
