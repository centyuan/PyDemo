"""
1.opencv-python:
2.ffmpeg-python:
3.moviepy:门槛低，处理常见需求,如截取,拼接,简单转场,特效,文件编码和读写也依赖ffmpeg

速度:opencv-python >ffmpeg-python > moviepy
"""
import json

"""1.获取视频时长"""
# 方式1
from moviepy.editor import VideoFileClip


def get_duration_from_moviepy(url):
    clip = VideoFileClip(url)
    return clip.duration


# 方式2
import cv2


def get_duration_from_cv2(url):
    """

    :param url: url或filename
    """
    cap = cv2.VideoCapture(url)
    if cap.isOpened():
        rate = cap.get(5)
        frame_num = cap.get(7)
        duration = frame_num / rate
        return duration
    return 0


# 方式3
import ffmpy3
import subprocess


def get_duration_from_ffmpeg(url):
    tup_resp = ffmpy3.FFprobe(
        inputs={url: None},
        global_options=[
            '-v', 'quiet',
            '-print_format', 'json',
            '-show_format', '-show_streams'
        ]
    ).run(stdout=subprocess.PIPE)
    meta = json.loads(tup_resp[0].decode('utf-8'))
    return meta['format']['duration']
