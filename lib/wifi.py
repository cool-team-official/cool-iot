import network  # 导入网络模块
import time  # 导入时间模块


# 连接到指定的WiFi网络
# ssid 是WiFi的名称
# password 是WiFi的密码
# timeout 是连接超时时间，默认为10秒
def connect(ssid, password, timeout=10):
    wlan = network.WLAN(network.STA_IF)  # 创建一个 WLAN 对象，用于 STA 模式
    wlan.active(True)  # 激活 WLAN 接口

    def attempt_connect():
        if not wlan.isconnected():  # 如果没有连接到WiFi
            print("Connecting to network...")  # 打印连接提示信息
            wlan.connect(ssid, password)  # 连接到指定的WiFi网络
            start_time = time.time()  # 记录开始连接的时间
            while not wlan.isconnected():  # 循环检查是否已连接
                if time.time() - start_time > timeout:  # 如果连接时间超过了超时时间
                    print("Connection timed out")  # 打印连接超时提示信息
                    return False  # 返回 False 表示连接失败
                print("Attempting to connect...")
                time.sleep(1)  # 等待一秒钟再检查连接状态
        print("Network config:", wlan.ifconfig())  # 打印网络配置
        return True  # 返回 True 表示连接成功

    # 初次连接尝试
    if attempt_connect():
        print("Initial connection successful")
    else:
        print("Initial connection failed, retrying...")
