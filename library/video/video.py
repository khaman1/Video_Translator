from ..image.image import Image
import cv2
import codecs
from math import floor
from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

class Video:
    unique_list=[]
    
    def __init__(self,
                 video_name='video',
                 fps=24,
                 stop_at_frame=0,
                 x1=900,
                 x2=1100,
                 y1=200,
                 y2=1700,
                 lang='chi_sim',
                 ):

        self.video_name = video_name
        self.video_url= 'input/'+ video_name +'.mp4'
        self.cap = cv2.VideoCapture(self.video_url)
        self.fps=fps
        
        self.start_time=0
        self.end_time=0

        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2

        self.stop_at_frame = stop_at_frame
        self.lang=lang

    def get_image(self):
        for i in range(0,self.fps):
            ret, frame = self.cap.read()

        self.end_time+=1

        return frame[self.x1:self.x2, self.y1:self.y2]

    def preview(self):
        cv2.imshow('Video', self.get_image())

    def extract_subtitle(self):
        previous_string=''
        CNT=0
        self.output=[]
        
        while True:
            try:
                img = self.get_image()
            except:
                print("ERROR!!!")
                break

            current_string, original_string = Image(img=img).toString(lang_src=self.lang)
            #current_string, original_string = Image(img=img).toChinese_version2()

            
            if previous_string != current_string and \
               similar(previous_string, current_string) < 0.88:# and original_string not in self.unique_list:

                previous_string = current_string

                self.output.append({
                    'start_time': self.start_time,
                    'end_time': self.end_time,
                    'text': current_string,
                    'original_text': original_string,
                })

                #self.unique_list.append(original_string)

                self.start_time = self.end_time

                CNT+=1

                print(str(CNT) + ' - Current time: ' + str(self.end_time) + 's')



                if self.stop_at_frame and CNT==self.stop_at_frame:
                    break

        return self

    def get_time_format(self,seconds=0):
        return str(floor(seconds/3600)) + ':'   + \
                str(floor(seconds/60)%60) + ':' + \
                str(seconds%60)

    def generate(self, url=''):
        with codecs.open('output/sub.srt','w','utf-8') as f:
            i=0
            for item in self.output:
                i+=1
                
                f.write(
                    str(i) + ' \n' +
                    self.get_time_format(item['start_time']) + ' --> ' + self.get_time_format(item['end_time']) + '\n' +
                    item['text'] + '\n\n')

    def generate_version2(self, url=''):
        with codecs.open('output/'+self.video_name+'.srt','w','utf-8') as f:
            i=0
            for item in self.output:
                i+=1
                
                f.write(
                    str(i) + ' \n' +
                    item['original_text'] + #'\n' +
                    #item['text'] + 
                    '\n\n')
