import tkinter as tk
from PIL import Image, ImageTk
import random
import glob # HL this library basically allow us to traverse the file and get the images

class gui:
    def __init__(self, mainwin):
        self.counter = 0
        self.mainwin = mainwin
        self.mainwin.title('inSight Picture Frame')
        self.mainwin.state('zoomed')
        self.mainwin.configure(bg = 'blue')
        self.frame = tk.Frame(mainwin)
        self.img = tk.Label(self.frame)
        self.frame.place(relheight = 0.85, relwidth = 0.9, relx = 0.05, rely=0.05)
        self.img.pack()
        # self.color()
        self.pic()

    # def color(self):
    #     self.colors = ['snow', 'old lace', 'linen']
    #     change = random.choice(self.color)
    #     self.mainwin.configure(bg = change)
    #     root.after(2000, self.color)
    
    def pic(self):
        self.pic_list = []
        # self.counter  = 0
        for name in glob.glob('C:/Users/hayun/OneDrive/Documents/1Alpha Master Cybernetics/Group CPS Project/Bulk-Bing-Image-downloader/bbid/*'):
        # for name in glob.glob(r'C:\Users\hayun\OneDrive\Documents\1Alpha Master Cybernetics\Group CPS Project\Bulk-Bing-Image-downloader\bbid'):    
            val = name
            self.pic_list.append(val)# HL i missed this line forever
        if self.counter == len(self.pic_list) - 1: #HL first index value is 0. So the counter is always going to be 1 less than the length of the list
            #so having the above line makes the loop never ending
            self.counter= 0
            print("if " +str(self.counter))
        else:
            self.counter = self.counter + 1
            print("else " +str(self.counter))
        self.file = self.pic_list[self.counter]
        self.load = Image.open(self.file)

        self.pic_width = self.load.size[0]
        self.pic_height = self.load.size[1]
        self.real_aspect = self.pic_width/self.pic_height #this will be the original aspect of the photo
        self.cal_width = int(self.real_aspect * 800)
        self.load2 = self.load.resize((self.cal_width, 800))
        self.render = ImageTk.PhotoImage(self.load2)
        self.img.config(image = self.render)
        self.img.image = self.render
        root.after(2000, self.pic)#change colours and change pictures This basically fires the function

root = tk.Tk()
myprog = gui(root)
# root.geometry("1000 x 1000")
root.mainloop()
# myprog()

