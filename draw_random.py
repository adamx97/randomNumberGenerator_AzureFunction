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


def HardwareLinkedInBackground(
    color1Tuple, color2Tuple, pixelWidth=1584, pixelHeight=396
):
    # Create a new image
    width = pixelWidth  # 1800
    height = pixelHeight  # 1600
    squaresize = 12  # the size of each square, 1 pixel is too small for most uses
    im = Image.new(
        "RGB",
        (width, height),
        color=color1Tuple,  # color1 is the initial color, some might say background
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
                            (x1, y1), color2Tuple  # color2 is the foreground color
                        )  # 197,202,233 is the light blue used on the resume site.
    end = time.time()
    # Save the image to a file
    im.save("random_image_linkedIn.png")
    print("{0:.3f} seconds for linkedIn image function".format(end - start))


def LinkedInCurvedBackground(
    color1Tuple, color2Tuple, imgPixelWidth=1584, imgPixelHeight=396, pValue=-2
):
    # pValue is negative to curve towards the viewer.  Smaller numbers are steeper curve (Try -1 to -4 or so)
    # for a parabola:  x = math.sqrt(y * pValue * 4)
    # slope at x: is slope at dy/dx = x/2pValue
    # width of tile when slope is positive: slope = tangent (theta), theta = arctan(s), adjacent = hypotenuse * cos (theta)
    # width of tile when slope is negative: slope = abs(tangent (theta)), theta = arctan(s), adjacent = hypotenuse * sin (theta)
    # Create a new image
    width = imgPixelWidth  # 1800
    height = imgPixelHeight  # 1600

    squaresize = 9  # the size of each square, 1 pixel is too small for most uses
    im = Image.new(
        "RGB",
        (width, height),
        color=color1Tuple,  # color1 is the initial color, some might say background
    )  # color=(197, 220, 233))
    rdObj = rd_functions_p.RdFunctions()
    bigs = []
    start = time.time()
    for i in range(
        math.ceil((width * height) / 64)
    ):  # the maximum number of squares we can draw, which can vary with varying tile size. #FIX THIS
        bigs.append(rdObj.RdRand64_Retry())
    # rdObj.RdRand64_Retry(3)
    mybits = get64BitsGenerator(bigs)
    # Draw random white pixels
    draw = ImageDraw.Draw(im)
    drawnwidth = 0
    # we need to draw pixels starting with 0, 0 in top right corner.
    imageTopCursor = 0  # start at top

    for y in range(
        0, height, squaresize
    ):  # start at top of image, and draw a row, then move next row in y and draw row
        # for y in range(0, width):
        leftside = (
            -1 * width // 2
        )  # start at left end of curve, this is the left side of the tile
        imageLeftCursor = leftside + width // 2
        for x in range(0, width, squaresize):
            # for each bit in bigs, if the bit is 1, draw a pixel
            pixel = (next(mybits)) & 1

            # get width of square based what we see due to the curvature
            # for a parabola:  x = math.sqrt(y * pValue * 4)
            # point = (leftside, math.sqrt(leftside * pValue * 4))
            # slope at x = x/2pValue
            slope = leftside / (2 * pValue)
            slopePercent = slope / 100
            if slope >= 0:
                # width of tile when slope is positive: slope = tangent (theta), theta = arctan(s), adjacent = hypotenuse * cos (theta)
                theta = math.atan(slopePercent)
                adjacent = int(squaresize * math.cos(theta))
            if slope < 0:
                theta = math.atan(abs(slopePercent))
                adjacent = int(squaresize * math.cos(theta))
            if pixel:
                for x1 in range(
                    imageLeftCursor,
                    imageLeftCursor + adjacent,
                ):
                    for y1 in range(y, y + squaresize):
                        draw.point(
                            (x1, y1), color2Tuple  # color2 is the foreground color
                        )  # 197,202,233 is the light blue used on the resume site.
            leftside = leftside + squaresize
            imageLeftCursor = imageLeftCursor + squaresize

    end = time.time()
    # Save the image to a file
    im.save("random_image_linkedInCurved.png")
    print("{0:.3f} seconds for linkedIn curved image function".format(end - start))


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
    # testGenerator()
    # InternalPythonFunction()
    # HardwarePythonFunction()
    # HardwareBlogBackground()
    # HardwareLinkedInBackground((26, 35, 126), (197, 202, 233), 1584, 396)
    LinkedInCurvedBackground((26, 35, 126), (197, 202, 233), 1584, 396)
