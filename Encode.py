from tkinter import *
import io
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import os
from tkinter import messagebox

import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 







class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        heading1=Label(root,text="Steganography Tool")
        heading1.pack()
        heading1.config(font=("Courier",30))
     

        # self.pack(fill=BOTH, expand=1)

        
        # load = Image.open("tesla.jpg")
        # render = ImageTk.PhotoImage(load)
        # img = Label(self, image=render)
        # img.image = render
        # img.place(x=0, y=0)


def genData(data): 
 
        newd = []  
          
        for i in data: 
            newd.append(format(ord(i), '08b')) 
        return newd 

def modPix(pix, data): 
      
    datalist = genData(data) 
    lendata = len(datalist) 
    imdata = iter(pix) 
  
    for i in range(lendata): 
          

        pix = [value for value in imdata.__next__()[:3] +
                                  imdata.__next__()[:3] +
                                  imdata.__next__()[:3]] 
                                      
        for j in range(0, 8): 
            if (datalist[i][j]=='0') and (pix[j]% 2 != 0): 
                  
                if (pix[j]% 2 != 0): 
                    pix[j] -= 1
                      
            elif (datalist[i][j] == '1') and (pix[j] % 2 == 0): 
                pix[j] -= 1
                  

        if (i == lendata - 1): 
            if (pix[-1] % 2 == 0): 
                pix[-1] -= 1
        else: 
            if (pix[-1] % 2 != 0): 
                pix[-1] -= 1
  
        pix = tuple(pix) 
        yield pix[0:3] 
        yield pix[3:6] 
        yield pix[6:9] 
  
def encode_enc(newimg, data): 
    w = newimg.size[0] 
    (x, y) = (0, 0) 
      
    for pixel in modPix(newimg.getdata(), data): 

        newimg.putpixel((x, y), pixel) 
        if (x == w - 1): 
            x = 0
            y += 1
        else: 
            x += 1

def encode(): 
    image = Image.open(filename, 'r') 
    data=ent.get("1.0","end-1c")
    
    if (len(data) == 0): 
        raise ValueError('Data is empty') 
          
    newimg = image.copy() 
    encode_enc(newimg, data) 
    new_img_name="Encrypted.png"
    newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))
    messagebox.showinfo("Alert", "MESSAGE SUCCESSFULLY ENCRYPTED")
    
    receiverAddrLabel = Label(root,text="Receiver's E-mail: ",font=("Times",10)) #pseudo code label
    receiverAddrLabel.place(x=100,y=570)

    sendButton = Button(root,text = "Send",width= 15, height=2,command=send,bg="orange",fg="white")
    sendButton.place(x=344,y=597)

    global emailBox
    emailBox = Text(root,bd=2,width='38',height='1.50',font=("Times",9))
    emailBox.place(x=240, y=563)

      
    sendButton = Button(root,text = "Send",width= 15, height=2,command=send,bg="orange",fg="white")
    sendButton.place(x=344,y=597)


    # ent.insert("Image Encrypted Successful!")
def content():
    b1 = Button(root,text = "Encrypt",width= 15, height=2,command=encode,bg="green",fg="white")
    b1.place(x=200, y=597)
    #b2 = Button(root,text = "Send",width= 15, height=1,command=send)
    #b2.place(x=600,y=600)
    ent.place()
    ent.bind("<Return>",encode)
def getorigin(eventorigin):
      global x,y
      x = eventorigin.x
      y = eventorigin.y
      print(x,y)
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

        
root = Tk()
app = Window(root)
root.resizable(width=True, height=True)
root.wm_title("Steganography Encrypter")
root.geometry("600x650")
root.bind("<Button 1>",getorigin)

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

ent = Text(root,bd=2,width='40',height='8',font=("Times", 11))
ent.place(x=128, y=450)
message = Label(root,text="Enter message in the box to hide",font=("Times",11)) #pseudo code label
message.place(x=170,y=420)





#sending the image
def send():
    global receiverAddr
    receiverAddr =  emailBox.get("1.0","end-1c")
    print(receiverAddr)
    print(filename)

    fromaddr = "sender mail"
    toaddr = receiverAddr
    
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    
    # storing the senders email address   
    msg['From'] = fromaddr 
    
    # storing the receivers email address  
    msg['To'] = toaddr 
    
    # storing the subject  
    msg['Subject'] = "Encrypted Image"
    
    # string to store the body of the mail 
    body = "Confidential data handle with care"
    
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    
    # open the file to be sent  
    attachmentFilename = filename
    attachment = open(attachmentFilename, "rb") 
    
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    
    # encode into base64 
    encoders.encode_base64(p) 
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % attachmentFilename) 
    
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    
    # start TLS for security 
    s.starttls() 
    
    # Authentication 
    s.login("useremail", "password") 
    
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
    
    # terminating the session 

    s.quit() 
    messagebox.showinfo("Alert", "MESSAGE SENT SUCCESSFULLY")
    root.destroy()


content()

root.mainloop()
