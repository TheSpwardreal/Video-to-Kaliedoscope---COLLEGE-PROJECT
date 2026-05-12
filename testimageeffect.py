from PIL import Image


def main():
    with (Image.open("cloudsfortest.png") as img,
          Image.open("cloudsfortest.png") as overlay_img, 
          Image.open("cloudsfortest.png") as overtop_img):
        forg_img = img
        vert_img = overlay_img.transpose(Image.FLIP_LEFT_RIGHT)
        horz_img = overtop_img.transpose(Image.FLIP_TOP_BOTTOM)
        backg_img = vert_img
        mirroredvert_img = Image.blend(forg_img, backg_img, 0.5)
        mirroredhor_img = Image.blend(forg_img, horz_img, 0.5)
        out_img = Image.blend(mirroredhor_img, mirroredvert_img, 0.5)
        mirroredvert_img.show()
        out_img.show()





if __name__ == "__main__":
    main()