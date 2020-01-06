from tkinter import *
import io
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import os
from tkinter import messagebox

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        # self.master = master
        # self.pack(fill=BOTH, expand=1)
        heading1=Label(root,text="Steganography Tool")
        heading1.pack()
        heading1.config(font=("Courier",30))
 
def upload():
    
    global filename
    filename = filedialog.askopenfilename(title='open image')
    return filename

def open_img():
    x = upload()
    img = Image.open(x)
    img = img.resize((410, 250))
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    staticpanel.forget()
    panel.image = img
    panel.pack()
    b1 = Button(root,text = "Decrypt",command=displaymessage,width= 15, height=2,bg="red",fg="white")
    b1.place(x=248, y=410)


def displaymessage():
    text=decode()
    label = Label( root,text=text, width= 35, height=10,bg="white",fg="red",font=("Times",15) )
    label.place(x=128,y=450) 

def decode(): 
    image = Image.open(filename, 'r') 
      
    data = '' 
    imgdata = iter(image.getdata()) 
      
    while (True): 
        pixels = [value for value in imgdata.__next__()[:3] +
                                  imgdata.__next__()[:3] +
                                  imgdata.__next__()[:3]] 

        binstr = '' 
          
        for i in pixels[:8]: 
            if (i % 2 == 0): 
                binstr += '0'
            else: 
                binstr += '1'
                  
        data += chr(int(binstr, 2)) 
        if (pixels[-1] % 2 != 0): 
            return data


root = Tk()
app = Window(root)
root.wm_title("Steganography Decrypter")
root.wm_title("Steganography Encrypter")
root.geometry("600x650")
uploadbutton=Button(root,text="Upload Image",command=open_img)  #file upload button
uploadbutton.pack(pady=40)

#static image code
img = Image.open("upload.png")
img = img.resize((360, 250))
img = ImageTk.PhotoImage(img)
staticpanel = Label(root, image=img)
staticpanel.image = img
staticpanel.pack()
#code ends

root.mainloop()

