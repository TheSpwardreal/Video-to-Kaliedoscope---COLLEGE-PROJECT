from PIL import Image


def main():
    with (Image.open("cloudsfortest.png") as img,
          Image.open("cloudsfortest.png") as overlay_img):
        foreg_img = img
        mirror_img = overlay_img.transpose(Image.FLIP_LEFT_RIGHT)
        backg_img = mirror_img
        out_img = Image.blend(foreg_img, backg_img, 0.5)
        foreg_img.show()
        backg_img.show()
        out_img.show()





if __name__ == "__main__":
    main()