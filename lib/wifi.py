import network


# 连接到指定的WiFi网络 ssid: 网络名称 password: 网络密码
def connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to network...")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print("Network config:", wlan.ifconfig())
