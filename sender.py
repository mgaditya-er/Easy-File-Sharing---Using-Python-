import socket
from tkinter import *

s = socket.socket()

def save(event):
    host = socket.gethostname()
    port = 85
    s.bind((host, port))
    s.listen(1)
    print('host name :', host)
    print('Configuring ...\n Please wait ...')
    conn, addr = s.accept()
    if(addr):
        filename = sendingfile.get()
        file = open(filename, "rb")
        file_data = file.read(4096)
        conn.send(file_data)
        print("Data has been sent successfully to the reciever")

screen = Tk()
screen.geometry("500x500")
screen.title("Sender")
heading = Label(text="python form ",bg="grey",fg="black",height="5",width="400")
heading.pack()

systemname_text = Label(text="your Host Name *")
sendingfile_text = Label(text="FileName *")
portnumber_text = Label(text="portNumber *")

systemname_text.place(x =15,y = 100)
sendingfile_text.place(x =15,y = 150)
portnumber_text.place(x =15,y = 200)

systemname = StringVar()
sendingfile = StringVar()
portnumber = IntVar()

systemname_entry = Entry(textvariable = systemname)
lastname_entry = Entry(textvariable = sendingfile)
age_entry = Entry(textvariable = portnumber)

systemname_entry.place(x=200,y=100,width="200")
lastname_entry.place(x=200,y=150,width="200")
age_entry.place(x=200,y=200,width="200")
text = Text(screen)

register=Button(text = "send",width="500",height="2", bg="grey")
register.place(x=75,y=250,width="200")

register.bind('<Button-1>',save)

register.bind('<Double-1>',quit)



screen.mainloop()