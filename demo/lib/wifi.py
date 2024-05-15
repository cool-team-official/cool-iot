import network
import time


# 连接到指定的WiFi网络 ssid 和 password 是WiFi的名称和密码 timeout 是连接超时时间 默认为10秒
def connect(ssid, password, timeout=10):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to network...")
        wlan.connect(ssid, password)
        start_time = time.time()
        while not wlan.isconnected():
            if time.time() - start_time > timeout:
                print("Connection timed out")
                return False
            time.sleep(1)  # 等待一秒钟再检查
    print("Network config:", wlan.ifconfig())
    return True
