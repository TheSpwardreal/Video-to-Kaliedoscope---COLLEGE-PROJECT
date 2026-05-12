from PIL import Image


def main():
    with (Image.open("penlo3d.png") as img,
          Image.open("penlo3d.png") as overlay_img, 
          Image.open("penlo3d.png") as overtop_img):
        x = img.width // 2
        y = img.height // 2
        forg_img = img # original image
        vert_img = overlay_img.transpose(Image.FLIP_LEFT_RIGHT) # vertically mirrored image
        horz_img = overtop_img.transpose(Image.FLIP_TOP_BOTTOM) # horizontally mirrored image
        forg_img.paste(vert_img, (x, y), mask=vert_img.crop(x,0)) # merging of vertical onto original
        img.show()




if __name__ == "__main__":
    main()