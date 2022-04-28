from PIL import Image


def decipher():
    black = 1

    with Image.open("code.png").convert() as img:
        pixel = img.load()
        w = img.size[0]
        h = img.size[1]

        return "".join([chr(j)
                     for i in range(w)
                     for j in range(h)
                        if pixel[i, j] == black])


if __name__ == "__main__":
    print(decipher())
