from library.image.image import Image
from library.video.video import Video


subtitle = Video(
    fps=24,
    video_name='video2',
    x1=950,
    lang='chi_sim',
    )


#subtitle.preview()



subtitle = subtitle.extract_subtitle()
subtitle.generate_version2()
