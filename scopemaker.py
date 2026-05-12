from PIL import Image

def rgba_alphazero(pixel):
    r, g, b, a = pixel
    zero_value = a - a
    return (r, g, b, zero_value)


def main():
    with Image.open("penlo3d.png") as img:
        forg_img = img #foreground image to not be changed
        xhalf_img = img.copy() #image used to be cut in half
        for y in range(img.height):
            for x in range(img.width//2): # 2nd in heirarchy is half the pixel width
                pix = img.getpixel((x,y)) # grabbing the pixel ratios in order to measure it when applying
                xhalf_img.putpixel((x,y), rgba_alphazero(pix)) # applying vertical / horizontals
        xcut_img = xhalf_img

        vert_img = xcut_img.transpose(Image.FLIP_LEFT_RIGHT) # vertically mirrored image

        out_img = Image.alpha_composite(forg_img, vert_img)
# ^^^^^^^^^^^^^^^^^^^^^^^^^ VERTICALLY MIRRORING ^^^^^^^^^^^^^^^^^ 
        yhalf_img = out_img.copy()
        for x in range(out_img.width):
            for y in range(out_img.height // 2): #this step will make a cut of the horizontal side of the image
                hpix = out_img.getpixel((x,y))
                yhalf_img.putpixel((x,y),rgba_alphazero(hpix))
        ycut_img = yhalf_img

        hor_img = ycut_img.transpose(Image.FLIP_TOP_BOTTOM) # horizontally mirrored image
        
        final_img = Image.alpha_composite(out_img, hor_img)

# ^^^^^^^^^^^^^^^^^^^^^^^^^ HORIZONTALLY MIRRORING ^^^^^^^^^^^^^^^^^ 

      #  final_img.show()
        duration_in_secs = 2.0
        fps = 24.0
        total_frames = int(duration_in_secs * fps)

        out_img_seq = []
        for n in range(total_frames):
            out_img_seq.append(final_img)

        out_img_seq[0].save('kaliedoscope.gif', append_images=out_img_seq[1:],
                            save_all=True, loop=0,
                            duration=1000/24.0)

if __name__ == "__main__":
    main()