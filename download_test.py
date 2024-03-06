import unittest
from unittest import IsolatedAsyncioTestCase

from tools.platforms import YouTubeDownloader
from asyncio import run


class MyTestCase(IsolatedAsyncioTestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.downloader = YouTubeDownloader("https://www.youtube.com/watch?v=9bZkp7q19f0") # Rick Roll
        print(self.downloader)

    async def test_audio_quality_settings(self):
        settings = self.downloader.get_audio_quality_settings()
        print(settings)

    async def test_video_quality_settings(self):
        settings = self.downloader.get_video_quality_settings()
        print(settings)

    async def test_video(self):
        settings = self.downloader.get_video_quality_settings()
        print(settings)

        await self.downloader.extract_video(settings[0].itag)

    async def test_video_with_max_resolution(self):
        await self.downloader.extract_video_with_max_resolution()

    async def test_audio(self):
        settings = self.downloader.get_audio_quality_settings()
        print(settings)

        await self.downloader.extract_audio(settings[0].itag)

    async def test_audio_with_max_resolution(self):
        await self.downloader.extract_audio_with_max_resolution()

    async def test_image(self):
        await self.downloader.extract_image()


if __name__ == '__main__':
    unittest.main()
