from abc import ABC


class SaveFile(ABC):
    def __init__(self, link: str) -> None:
        self.link = link

    def get_video_quality_settings(self) -> None:
        ...

    def get_audio_quality_settings(self) -> None:
        ...

    def extract_audio(self,  **kwargs) -> None:
        ...

    def extract_video(self,  **kwargs) -> None:
        ...

    def extract_image(self,  **kwargs) -> None:
        ...

    def extract_video_with_max_resolution(self) -> None:
        ...

    def extract_audio_with_max_resolution(self) -> None:
        ...
