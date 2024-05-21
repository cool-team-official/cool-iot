from machine import I2S, Pin
import urequests
import utime
import _thread


# 播放音频
class AudioPlayer:
    def __init__(
        self,
        sck_pin_num,
        ws_pin_num,
        sd_pin_num,
        rate=16000,
        bits=16,
        format=I2S.MONO,
        ibuf=20000,
    ):
        self.sck_pin = Pin(sck_pin_num)  # BCLK
        self.ws_pin = Pin(ws_pin_num)  # LRC
        self.sd_pin = Pin(sd_pin_num)  # DIN
        self.i2s = I2S(
            1,
            sck=self.sck_pin,
            ws=self.ws_pin,
            sd=self.sd_pin,
            mode=I2S.TX,
            bits=bits,
            format=format,
            rate=rate,
            ibuf=ibuf,
        )
        self.stop_flag = False
        self.play_thread = None
        self.buffer = bytearray()

    def _play_stream(self):
        print("begin playing...")

        try:
            while not self.stop_flag:
                if len(self.buffer) > 0:
                    byte = self.buffer[:1024]
                    self.i2s.write(byte)  # Write data to I2S device
                    self.buffer = self.buffer[1024:]
                else:
                    utime.sleep(0.01)  # Wait for buffer to fill
        except Exception as err:
            print("Error:", err)

    def _play_url(self, url):
        response = urequests.get(url, stream=True)
        response.raw.read(100)  # Skip initial distorted audio
        print("begin playing...")

        try:
            while not self.stop_flag:
                byte = response.raw.read(1024)
                if byte:
                    self.i2s.write(byte)  # Write data to I2S device
                else:
                    print("Playback finished.")
                    break  # Exit loop when no more data
        except Exception as err:
            print("Error:", err)
        finally:
            response.close()
            self.stop()

    def _play_file(self, file_path):
        print("begin playing...")

        try:
            with open(file_path, "rb") as f:
                f.read(100)  # Skip initial distorted audio
                while not self.stop_flag:
                    byte = f.read(1024)
                    if byte:
                        self.i2s.write(byte)  # Write data to I2S device
                    else:
                        print("Playback finished.")
                        break  # Exit loop when no more data
        except Exception as err:
            print("Error:", err)
        finally:
            self.stop()

    # 开始播放音频（通过缓冲区）
    def play(self):
        self.stop_flag = False
        self.play_thread = _thread.start_new_thread(self._play_stream, ())

    # 停止播放
    def stop(self):
        self.stop_flag = True
        if self.play_thread:
            _thread.exit()
        utime.sleep(1)
        self.i2s.deinit()
        print("Playbackstopped .")

    # 向缓冲区添加音频数据
    def add_to_buffer(self, data):
        self.buffer.extend(data)

    # 根据 URL 播放音频
    def play_from_url(self, url):
        self.stop_flag = False
        self.play_thread = _thread.start_new_thread(self._play_url, (url,))

    # 根据文件播放音频
    def play_from_file(self, file_path):
        self.stop_flag = False
        self.play_thread = _thread.start_new_thread(self._play_file, (file_path,))


# Usage example:
# player = AudioPlayer(sck_pin_num=26, ws_pin_num=25, sd_pin_num=33)
# player.play_from_url("http://example.com/audiofile")
# or
# player.play_from_file("path/to/audiofile.wav")
# or
# player.play()
# player.add_to_buffer(audio_data)  # Add audio data to buffer
# utime.sleep(10)  # Play for 10 seconds
# player.stop()
