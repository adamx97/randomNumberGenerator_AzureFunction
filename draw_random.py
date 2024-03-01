from PIL import Image, ImageDraw
import random
import rd_functions_p
import time
import math


def InternalPythonFunction():

    # Create a new image
    im = Image.new("RGB", (512, 512), color=(0, 0, 0))
    start = time.time()
    # Draw random white pixels
    draw = ImageDraw.Draw(im)
    for y in range(512):
        for x in range(512):
            if random.randint(0, 1):
                draw.point((x, y), (255, 255, 255))
    end = time.time()
    # Save the image to a file
    im.save("random_image_internal.png")
    print("{0:.3f} seconds for internal function".format(end - start))


def HardwarePythonFunction():
    # Create a new image
    im = Image.new("RGB", (512, 512), color=(0, 0, 0))
    rdObj = rd_functions_p.RdFunctions()
    bigs = []
    start = time.time()
    for i in range(math.ceil((512 * 512) / 64)):
        bigs.append(rdObj.RdRand64_Retry())
    # rdObj.RdRand64_Retry(3)
    mybits = get64BitsGenerator(bigs)
    # Draw random white pixels
    draw = ImageDraw.Draw(im)

    for y in range(512):
        for x in range(512):
            # if random.randint(0, 1):
            # for each bit in bigs, if the bit is 1, draw a pixel
            pixel = (next(mybits)) & 1
            if pixel:
                draw.point((x, y), (255, 255, 255))
    end = time.time()
    # Save the image to a file
    im.save("random_image_hardware.png")
    print("{0:.3f} seconds for hardware function".format(end - start))


def HardwareBlogBackground():
    # Create a new image
    width = 1800  # 1800
    height = 1600  # 1600
    squaresize = 7  # the size of each square, 1 pixel is too small for most uses
    im = Image.new(
        "RGB", (width, height), color=(197, 220, 233)
    )  # color=(197, 220, 233))
    rdObj = rd_functions_p.RdFunctions()
    bigs = []
    start = time.time()
    for i in range(math.ceil((width * height) / 64)):
        bigs.append(rdObj.RdRand64_Retry())
    # rdObj.RdRand64_Retry(3)
    mybits = get64BitsGenerator(bigs)
    # Draw random white pixels
    draw = ImageDraw.Draw(im)

    for y in range(0, height, squaresize):
        for x in range(0, width, squaresize):
            # if random.randint(0, 1):
            # for each bit in bigs, if the bit is 1, draw a pixel
            pixel = (next(mybits)) & 1
            if pixel:
                for x1 in range(x, x + squaresize):
                    for y1 in range(y, y + squaresize):
                        draw.point(
                            (x1, y1), (197, 202, 233)
                        )  # 197,202,233 is the light blue used on the resume site.
    end = time.time()
    # Save the image to a file
    im.save("random_image_blog.png")
    print("{0:.3f} seconds for blog image function".format(end - start))


def get64BitsGenerator(bigs):
    while bigs:
        num = bigs.pop(0)
        for i in range(64):
            bit = (num >> i) & 1
            # print("{0}, {1}".format(i, num))
            yield bit


def testGenerator():
    bigs = []
    rdObj = rd_functions_p.RdFunctions()
    bigs.append(rdObj.RdRand64_Retry())
    bigs.append(rdObj.RdRand64_Retry())
    mybits = get64BitsGenerator(bigs)
    for a in range(128):
        print("idx: {0} bit: {1}".format(a, next(mybits)))


if __name__ == "__main__":
    # InternalPythonFunction()
    # HardwarePythonFunction()
    HardwareBlogBackground()
