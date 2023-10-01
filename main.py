from moviepy.editor import *

def black_video(size, duration):
    ColorClip(size, color=(0, 0, 0), duration=duration).write_videofile("black.mp4", fps=30)

def overlay_video(video_path):
    video = VideoFileClip(video_path)
    flipped_ratio_ratio = video.size[0] / video.size[1]
    width = video.size[1] / flipped_ratio_ratio
    nearest_integer = round(width)
    black_video((nearest_integer,video.size[1]), video.duration)
    bg = VideoFileClip("black.mp4", audio=False)
    result = CompositeVideoClip([bg, video.set_position("center")])
    result.write_videofile("result.mp4", fps=30)

if __name__ == '__main__':
    overlay_video("input_video.mp4")
