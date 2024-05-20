import lib.wifi as wifi
from lib.audio import AudioPlayer

# 连接wifi
wifi.connect("COOL", "666123456")

# 初始化音频播放器
player = AudioPlayer(sck_pin_num=12, ws_pin_num=14, sd_pin_num=13)

# 播放音频
player.play_from_url(
    "https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_example_zh.wav"
)
