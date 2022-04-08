from tkinter import *
import socket

s = socket.socket()
def connection(event):
    host = hostaddr.get()
    port = 85
    s.connect((host, port))
    print('connected')

def recieve_file(event):
    filename = recievingfile.get()
    file = open(filename, 'wb')
    file_data = s.recv(4096)
    file.write(file_data)
    file.close()
    print("File has been recieved succesfully")
    print("File has been saved in ur folde by name: ", recievingfile.get())


screen = Tk()
screen.geometry("500x500")
screen.title("reciever")
heading = Label(text="python form ",bg="grey",fg="black",height="5",width="400")
heading.pack()

hostaddr_text = Label(text="Your Host Name *")
recievingfile_text = Label(text="FileName *")
portnumber_text = Label(text="portNumber *")

hostaddr_text.place(x =15,y = 100)
recievingfile_text.place(x =15,y = 150)
portnumber_text.place(x =15,y = 200)

hostaddr = StringVar()
recievingfile = StringVar()
age = IntVar()

hostaddr_entry = Entry(textvariable = hostaddr)
recievingfile_entry = Entry(textvariable = recievingfile)
age_entry = Entry(textvariable = age)

hostaddr_entry.place(x=200,y=100,width="200")
recievingfile_entry.place(x=200,y=150,width="200")
age_entry.place(x=200,y=200,width="200")
text = Text(screen)

register=Button(text = "connect",width="500",height="2",bg="grey")
register.place(x=75,y=250,width="200")
register.bind('<Button-1>',connection)

register=Button(text = "recieve",width="500",height="2",bg="grey")
register.place(x=75,y=300,width="200")
register.bind('<Button-1>',recieve_file)
screen.mainloop()