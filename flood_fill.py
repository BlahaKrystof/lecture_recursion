import matplotlib.pyplot as plt

def flood_fill(img, x, y):
    if x in range(len(img[0])) and y in range(len(img)):
        if  img[y][x] == 1.:
            img[y][x] = 2.
            plt.imshow(img, cmap="gray") # UKAZE POSTUPNE VYBARVOVANI
            plt.show(block=False)
            plt.pause(0.005)
            plt.clf()
            flood_fill(img, x + 1, y)
            flood_fill(img, x, y + 1)
            # flood_fill(img, x + 1, y + 1)
            flood_fill(img, x - 1, y)
            flood_fill(img, x, y - 1)
            # flood_fill(img, x -1, y -1)
        elif img[y][x] == 0.:
            img[y][x] = 0.

    return img

def main():
    # img = plt.imread("files/img0.png")[:, :, 0]
    # img = plt.imread("files/img1.png")[:, :, 0]
    img = plt.imread("files/img2.png")[:, :, 0]

    img = flood_fill(img, 0, 0)

    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(20)
    plt.clf()


if __name__ == "__main__":
    main()
