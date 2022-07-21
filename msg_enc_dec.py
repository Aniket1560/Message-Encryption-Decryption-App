from tkinter import *
import base64

root = Tk()
root.geometry('500x300')
root.resizable(0,0)

root.title("Message Encryption and Decryption Application")

Label(root, text ='ENCRYPTION DECRYPTION', font = 'arial 20 bold').pack()
Label(root, text ='By Aniket', font = 'arial 10 bold').pack(side= BOTTOM)

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))    
    return "".join(dec)

def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')

def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")
#Message
Label(root, font= 'arial 12 bold', text='MESSAGE').place(x= 60,y=60)
Entry(root, font = 'arial 10', textvariable = Text, bg = 'ghost white').place(x=290, y = 60)
#key
Label(root, font = 'arial 12 bold', text ='KEY').place(x=60, y = 90)
Entry(root, font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=290, y = 90)
#mode
Label(root, font = 'arial 12 bold', text ='MODE(e-encode, d-decode)').place(x=60, y = 120)
Entry(root, font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)
#result
Label(root, font = 'arial 12 bold', text ='RESULT').place(x=60, y = 150)
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='ghost white').place(x=290, y = 150)
#result button
Button(root, font = 'arial 10 bold', text = 'RESULT'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=150, y = 200)
#reset button
Button(root, font = 'arial 10 bold' ,text ='RESET ' , command = Reset,bg = 'LightGray', padx=2).place(x=250, y = 200)
root.mainloop()