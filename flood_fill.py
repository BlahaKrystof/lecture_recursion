import matplotlib.pyplot as plt

def flood_fill(img, x, y):
    if x in range(len(img[0])) and y in range(len(img)):
        if  img[x][y] == 1.:
            img[x][y] = 2.
            flood_fill(img, x +1, y)
            flood_fill(img, x, y +1)
            flood_fill(img, x + 1, y + 1)
        elif img[x][y] == 0.:
            img[x][y] = 0.



def main():
    img = plt.imread("files/img0.png")[:, :, 0]
    # img = plt.imread("files/img1.png")[:, :, 0]
    # img = plt.imread("files/img2.png")[:, :, 0]

    img = flood_fill(img, 0, 0)

    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()


if __name__ == "__main__":
    main()
