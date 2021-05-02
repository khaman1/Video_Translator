from library.image.image import Image
from library.video.video import Video


subtitle = Video(
    fps=48,
    video_name='video7',
    x1=950,
    y1=0,
    y2=2000,
    #stop_at_frame=10,
    lang='chi_sim_2',
    )


#subtitle.preview()



subtitle = subtitle.extract_subtitle()
subtitle.generate_version2()
