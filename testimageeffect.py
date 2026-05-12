from PIL import Image

def rgba_alphazero(pixel):
    r, g, b, a = pixel
    zero_value = a - a
    return (r, g, b, zero_value)


def main():
    with Image.open("penlo3d.png") as img:
        forg_img = img
        half_img = img.copy()
        for y in range(img.height):
            for x in range(img.width//2): # 2nd in heirarchy is half the pixel width
                pix = img.getpixel((x,y)) # grabbing the pixel ratios in order to measure it when applying
                half_img.putpixel((x,y), rgba_alphazero(pix)) # applying vertical / horizontals
        cut_img = half_img

        vert_img = cut_img.transpose(Image.FLIP_LEFT_RIGHT) # vertically mirrored image

        out_img = Image.blend(vert_img, forg_img, 1)
        
        out_img.show()

if __name__ == "__main__":
    main()