import glob
import os

import moviepy.editor as mpy


def main():
    img_seq = glob.glob(os.path.join('kaliedoscope', '.png'))
    img_seq.sort()
    print(img_seq)
    clip = mpy.ImageSequenceClip(img_seq, fps=24)
    clip.write_videofile('kaliedoscopevideo.mp4')
    clip.close()


if __name__ == "__main__":
    main()