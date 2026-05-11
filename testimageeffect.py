from PIL import Image


def main():
    with Image.open("cloudsfortest.png") as img:
        out_img = img.resize((320,180))
        out_img.save("thumbnail.png")



if __name__ == "__main__":
    main()