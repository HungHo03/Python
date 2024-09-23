#For Project 3
from PIL import Image
img1 = Image.open("Me.jpg") #open the image
img2 = Image.open("Star.jpg")
img3 = Image.open("Japan.jpg")

'''
This first function takes in an image (Me.jpg). It will create a new image with the left most 325 pixels and
the top most 1110 pixels of the original image (basically cropping a certain part of the original picture). Return the 
new cropped image and stored it in a variable called new_img1, which is the output of this function.
Tag: PARTIAL_MODIFICATION
'''
#Function 1: Partial Modification of the Me Image
def partial_modification_me_area(img1):
    result1 = img1.copy() 
    width, height = img1.size
    new_img1 = Image.new("RGB", (325, 1110)) 
    for x in range(1395, 1720):
        for y in range(2770, 3880): 
            r, g, b = result1.getpixel((x, y)) 
            new_img1.putpixel((x-1395, y-2770), (r, g, b)) 
    return new_img1

'''
This second function takes in an image (Star.jpg). It will create a new image with the left most 181 pixels and 
the top most 200 pixels of the original image (basically cropping a certain part of the original picture). Returns the
new cropped image and stored it in a variable called new_img2, which is the output of this function.
Tag: PARTIAL_MODIFICATION
'''
#Function 2: Partial Modification of the Star Image
def partial_modification_star_area(img2):
    result2 = img2.copy()
    width, height = img2.size 
    new_img2 = Image.new("RGB", (181, 200)) 
    for x in range(381, 562): 
        for y in range(113, 313): 
            r, g, b = result2.getpixel((x, y)) 
            new_img2.putpixel((x-381, y-113), (r, g, b)) 
    return new_img2

'''
This third function takes in an image (Japan.jpg) and the level of brightness. It will create a new image that has a 
filter applied to a portion of the image by reducing the brightness of the image by 20%. Returns the new image and stored 
it in a variable called new_img3, which is the output of this function.
Tag: FILTER
'''
#Function 3: Image Filter for Japan Image (Size: 1280 x 830)
def image_filter_japan(img3, brightness_factor=.8):
    result3 = img3.copy()
    width, height = img3.size
    new_img3 = result3
    for x in range(0, 1280):
        for y in range(0, 215):
            r, g, b = result3.getpixel((x, y))
            r = int(r * brightness_factor)
            g = int(g * brightness_factor)
            b = int(b * brightness_factor)
            new_img3.putpixel((x, y), (r, g, b))
    return new_img3

'''
This fourth function takes in two images, new_img2 from function #2 and new_img3 from function #3. It will create 
a new image, that is the size of new_img3 and resize new_img2 to be the same size, in order to blend the two images together. 
Returns the new image and stored it in a variable called new_img4, which is the output of this function.
Tag: COPY_BLEND
'''
#Function 4: Blend new_img2 and new_img3
def blend_images(new_img2, new_img3):
    result4 = new_img3.copy()
    width, height = new_img3.size
    new_img2 = new_img2.resize((width, height))
    new_img4 = result4
    for x in range(width):
        for y in range(height):
            r1, g1, b1 = new_img2.getpixel((x, y))
            r2, g2, b2 = new_img3.getpixel((x, y))
            result4.putpixel((x, y), ((r1 + r2)//2, (g1 + g2)//2, (b1 + b2)//2))
    return new_img4

'''
This fifth function takes in two images, new_img1 from function #1 and new_img4 from function #4. It will copy and paste
new_img1 onto new_img4. Returns the new image and stored it in a variable called result, which is the output of this function.
Tag: COPY_BlEND
'''
#Function 5: Copy and paste new_img1 into new_img4
def combine_images(new_img1, new_img4):
    result = new_img4.copy()
    width, height = new_img4.size
    result.paste(new_img1, (0, 0))
    result.save("result.jpg")
    result.show()
    
#call function
combine_images(partial_modification_me_area(img1), blend_images(partial_modification_star_area(img2), image_filter_japan(img3)))






