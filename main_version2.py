import cv2
import codecs
from math import floor
from difflib import SequenceMatcher



video_name = 'video7'
video_url= 'input/'+ video_name +'.mp4'
v = cv2.VideoCapture(video_url)
