from PIL import Image
from time import sleep
import unicornhat as unicorn
import numpy
unicorn.brightness(1)
unicorn.rotation(180)
unicorn.clear()
unicorn.show()

unicorn.set_pixel(9, 0, 0, 0, 255) #blue
unicorn.show()
sleep(3)

file = input("Please enter the name of the file ")

im = Image.open(file + ".jpg", "r") # name of file to scan
width, height = im.size
pixel_values = list(im.getdata())
print (pixel_values)
total = (len(pixel_values))
#pixel_list = pixel_values
print ("Found ", total, "Pixels")

if total == 100:
    unicorn.set_pixel(9, 0, 255, 0, 0)
    unicorn.show()
    sleep(3)
    npc = [] # list to stored new RGB values New Pixel Colours

    # Sorts GRB values into RGB values
    for i in range(0, 100): 
        pos = pixel_values[i] # pull first RGB values from list
        #print (pos) for testing
        green = pos[0] # pull out green value
        red = pos[1] # pull out red value
        blue = pos[2] # pull out blue value
        RGB_correct = (red, green, blue) 
        npc.append(RGB_correct) # adds correct RGB value to new pixel colour list
        #print (npc) #uncomment for testing

      
           
    pic =  [[npc[9],npc[8],npc[7],npc[6],npc[5],npc[4],npc[3],npc[2],npc[1],npc[0]],
            [npc[19],npc[18],npc[17],npc[16],npc[15],npc[14],npc[13],npc[12],npc[11],npc[10]],
            [npc[29],npc[28],npc[27],npc[26],npc[25],npc[24],npc[23],npc[22],npc[21],npc[20]],
            [npc[39],npc[38],npc[37],npc[36],npc[35],npc[34],npc[33],npc[32],npc[31],npc[30]],
            [npc[49],npc[48],npc[47],npc[46],npc[45],npc[44],npc[43],npc[42],npc[41],npc[40]],
            [npc[59],npc[58],npc[57],npc[56],npc[55],npc[54],npc[53],npc[52],npc[51],npc[50]],
            [npc[69],npc[68],npc[67],npc[66],npc[65],npc[64],npc[63],npc[62],npc[61],npc[60]],
            [npc[79],npc[78],npc[77],npc[76],npc[75],npc[74],npc[73],npc[72],npc[71],npc[70]],
            [npc[89],npc[88],npc[87],npc[86],npc[85],npc[84],npc[83],npc[82],npc[81],npc[80]],
            [npc[99],npc[98],npc[97],npc[96],npc[95],npc[94],npc[93],npc[92],npc[91],npc[90]]]
           
    unicorn.set_pixels(pic)
    unicorn.show()

else:
    print ("Image Too Large")
    unicorn.set_pixel(9, 0, 0, 255, 0)
    unicorn.show()
    




 
