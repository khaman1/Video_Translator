from library.image.image import Image
from library.video.video import Video


subtitle = Video(
    fps=48,
    video_name='video4',
    x1=950,
    #stop_at_frame=10,
    lang='chi_sim',
    )


#subtitle.preview()



subtitle = subtitle.extract_subtitle()
subtitle.generate_version2()
