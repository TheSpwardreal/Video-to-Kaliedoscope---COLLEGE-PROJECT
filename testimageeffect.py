from PIL import Image


def main():
    with (Image.open("cloudsfortest.png") as img,
          Image.open("cloudsfortest.png") as overlay_img, 
          Image.open("cloudsfortest.png") as overtop_img):
        foreg_img = img
        vert_img = overlay_img.transpose(Image.FLIP_LEFT_RIGHT)
        horz_img = overtop_img.transpose(Image.FLIP_TOP_BOTTOM)
        backg_img = vert_img
        mirrored_img = Image.blend(foreg_img, backg_img, 0.5)
        out_img = Image.blend(horz_img, mirrored_img, 0.5)
        mirrored_img.show()
        out_img.show()





if __name__ == "__main__":
    main()