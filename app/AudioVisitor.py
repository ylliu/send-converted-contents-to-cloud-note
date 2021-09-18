import os


class AudioVisitor(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def get_supported_audio_files(self):
        result = []
        format_supported = ["wav", "flac", "opus", "m4a", "mp3"]
        files = os.listdir(self.file_path)
        for file in files:
            if file.split(".")[1] not in format_supported:
                continue
            result.append(os.path.join(self.file_path, file))
        if len(result) == 0:
            print("请检查" + self.file_path + "下是否放置了音频文件")
        return result
