from PIL import Image


def main():
    with (Image.open("penlo3d.png") as img,
          Image.open("penlo3d.png") as overlay_img, 
          Image.open("penlo3d.png") as overtop_img):
        x = img.width // 2
        y = img.height // 2
        forg_img = img
        vert_img = overlay_img.transpose(Image.FLIP_LEFT_RIGHT)
        horz_img = overtop_img.transpose(Image.FLIP_TOP_BOTTOM)
        img.paste(vert_img, (0, 0), mask=vert_img.crop(x,0))
        img.show()




if __name__ == "__main__":
    main()