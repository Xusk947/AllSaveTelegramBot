from tools.platforms.save_file import SaveFile
from pytube import YouTube, Stream
from tools.platforms.const import SAVE_PATH, get_current_time_in_ns
import pythumb


class YouTubeDownloader(SaveFile):
    def __init__(self, link: str) -> None:
        super().__init__(link)
        self.yt = YouTube(self.link)

    def get_video_quality_settings(self) -> list[Stream]:
        return self.yt.streams.filter(only_video=True)

    def get_audio_quality_settings(self) -> list[Stream]:
        return self.yt.streams.filter(only_audio=True)

    async def extract_audio(self, itag: int) -> None:
        stream = self.yt.streams.get_by_itag(itag)
        filename = stream.default_filename

        # replace WEBM to MP3
        filename = filename.replace(".webm", ".mp3")

        stream.download(output_path=SAVE_PATH, filename=get_current_time_in_ns() + filename, filename_prefix=filename[:-4], skip_existing=True)

    async def extract_video(self, itag: int) -> None:
        stream = self.yt.streams.get_by_itag(itag)
        filename = stream.default_filename

        # replace WEBM to MP4
        filename = filename.replace(".webm", ".mp4")


        stream.download(output_path=SAVE_PATH, filename=get_current_time_in_ns() + filename, filename_prefix=filename[:-4], skip_existing=True)

    async def extract_image(self, quality: int = 0) -> None:
        thumb = pythumb.Thumbnail(self.link)

        thumb.fetch()

        thumb.save(dir=SAVE_PATH, filename=get_current_time_in_ns() + ".jpg", overwrite=True)

    async def extract_video_with_max_resolution(self, **kwargs) -> None:
        stream = self.yt.streams.get_by_itag(self.get_video_quality_settings()[-1].itag)
        filename = stream.default_filename

        # replace WEBM to MP4
        filename = filename.replace(".webm", ".mp4")

        stream.download(output_path=SAVE_PATH, filename=get_current_time_in_ns() + filename, filename_prefix=filename[:-4], skip_existing=True)

    async def extract_audio_with_max_resolution(self) -> None:
        stream = self.yt.streams.get_by_itag(self.get_audio_quality_settings()[-1].itag)
        filename = stream.default_filename

        # replace WEBM to MP3
        filename = filename.replace(".webm", ".mp3")

        stream.download(output_path=SAVE_PATH, filename=get_current_time_in_ns() + filename, filename_prefix=filename[:-4], skip_existing=True)
