#import module
from datetime import date
from tkinter import *
from PIL import ImageTk, Image

#funcition

def year():
    birthyear = 2006
    birthmonth = 3
    birthday = 4

    daynow = date.today().strftime('%Y-%m-%d').split('-')
    age_y = int(daynow[0])-int(birthyear)
    age_m = int(daynow[1])-int(birthmonth)
    age_d = int(daynow[2])-int(birthday)

root = Tk()
root.title("Resume By HereSeok Power BY JSJLABS.DEV")
root.wm_iconbitmap('logo.ico')
img = Image.open("1.jpg")
img = img.resize((int(img.width * .5), int(img.height * .5)))
photo = ImageTk.PhotoImage(img)
lbl = Label(image=photo)
lbl.grid(row=3,column=2)
lable1 = Label(root, text = 'นาย ธนกร เจริญเลิศกมล ชื่อเล่น ซอกจิน').grid(row=6,column=2)

lable2 = Label(root, text = 'เกิดวันที่ 4 มีนาคม 2549').grid(row=7,column=2)

lable3 = Label(root,text ='อายุ 15 ปี').grid(row=8,column=2)

lable4 = Label(root,text ='สัญชาติ ไทย เชื่อชาติ ไทย ศาสนา คริสต์').grid(row=9,column=2)

lable5 = Label(root,text ='กรุ๊บเลือด โอ').grid(row=10,column=2)

lable6 = Label(root,text ='สถานศึกษา โรงเรียน เทพศิรินทร์ สายการเรียน ศิลป์ภาษา ญี่ปุ่น').grid(row=11,column=2)

lable7 = Label(root,text ='email : root.jeongseokjin@outlook.com').grid(row=12,column=2)

lable8 = Label(root,text ='เบอร์โทร 095-791-3410').grid(row=13,column=2)

lable9 = Label(root,text = 'งานอดิเรก Coding').grid(row=14,column=2)

button = Button(root, text='ออก', width=30, command=root.destroy).grid(row=15,column=2)
img2 = Image.open('9.jpg')
img2 = img2.resize((int(img2.width * .15), int(img2.height * .15)))
photo2 = ImageTk.PhotoImage(img2)
lbl2 = Label(image=photo2)
lbl2.grid(row=16,column=2)
root.mainloop()