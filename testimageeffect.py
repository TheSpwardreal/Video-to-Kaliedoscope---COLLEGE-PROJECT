from PIL import Image


def main():
    with Image.open("cloudsfortest.png") as img:
        foreg_img = img
        backg_img = Image.open("cloudsfortest.png")
        out_img = Image.blend(foreg_img, backg_img, 0.5)
        foreg_img.show()
        backg_img.show()
        out_img.show()





if __name__ == "__main__":
    main()