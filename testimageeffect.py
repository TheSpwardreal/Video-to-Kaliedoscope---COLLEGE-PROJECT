from PIL import Image




def main():
    with (Image.open("penlo3d.png") as img,
          Image.open("penlo3d.png") as overlay_img, 
          Image.open("penlo3d.png") as overtop_img):
        out_img = img.copy()
        vert_img = overlay_img.transpose(Image.FLIP_LEFT_RIGHT) # vertically mirrored image
        horz_img = overtop_img.transpose(Image.FLIP_TOP_BOTTOM) # horizontally mirrored image
        for y in range(img.height):
            for x in range(img.width//2): # 2nd in heirarchy is half the pixel width
                pix = img.getpixel((x,y)) # grabbing the pixel ratios in order to measure it when applying
                out_img.paste((x,y), vert_img(pix), horz_img(pix)) # applying vertical / horizontals
        forg_img = img # original image
        
        img.show()




if __name__ == "__main__":
    main()