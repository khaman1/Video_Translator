from library.image.image import Image
from library.video.video import Video


subtitle = Video(
    fps=24,
    video_name='video 5',
    stop_at_frame=6,
    lang='chi_sim_new',
    )


subtitle.preview()
subtitle = subtitle.extract_subtitle()

subtitle.generate_version2()
