from tkinter import *
import random
import time
import datetime
root = Tk()
root.geometry('1200x6000')
root.title('Message Encryption and Decryption')
Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)
frame1 = Frame(root, width=800, height=700, relief=SUNKEN)
frame1.pack(side=LEFT)

myfont = ('Arial', 16, 'bold')

# ==============================================
#                  TIME
# ==============================================
localtime = time.asctime(time.localtime(time.time()))
lbl_info = Label(Tops, font=('Helvetica', 50, 'bold'),
                 text="SECRET MESSAGING \n Vigenère cipher",
                 fg='black', bd=10, anchor='w')
lbl_info.grid(row=0, column=0)
lbl_info = Label(Tops, font=('Arial', 20, 'bold'),
                 text=localtime, fg='steel blue',
                 bd=10, anchor='w')
lbl_info.grid(column=0, row=1)

rand = StringVar()
msg = StringVar()
key = StringVar()
mode = StringVar()
result = StringVar()

#exit function
def qExit():
    root.destroy()

#function to reset the window
def reset():
    rand.set('')
    msg.set('')
    key.set('')
    mode.set('')
    result.set('')

#reference
lbl_reference = Label(frame1, font=('Arial', 16, 'bold'),
                      text='Name:', bd=16, anchor='w')
lbl_reference.grid(row=0, column=0)

txt_reference = Entry(frame1, font=('Arial', 16, 'bold'),
                      textvariable=rand, bd=10, insertwidth=4,
                      bg='powder blue', justify='right')
txt_reference.grid(row=0, column=1)

#labels
lbl_msg = Label(frame1, font=('Arial', 16, 'bold'),
                text='MESSAGE', bd=16, anchor='w')
lbl_msg.grid(row=1, column=0)
txt_msg = Entry(frame1, font=('Arial', 16, 'bold'),
                textvariable=msg, bd=10, insertwidth=4,
                bg='powder blue', justify='right')
txt_msg.grid(row=1, column=1)
lbl_key = Label(frame1, font=myfont, text='KEY', bd=16, anchor='w')
lbl_key.grid(row=2, column=0)

txt_key = Entry(frame1, font=myfont, textvariable=key, bd=10,
                insertwidth=4, bg='powder blue', justify='right')
txt_key.grid(row=2, column=1)
lbl_mode = Label(frame1, font=myfont, text='MODE(e for encrypt, d for decrypt)',
                 bd=16, anchor='w')
lbl_mode.grid(row=3, column=0)
txt_mode = Entry(frame1, font=myfont, textvariable=mode,
                 bg='powder blue', justify='right')
txt_mode.grid(row=3, column=1)
lbl_service = Label(frame1, font=myfont, text='The Result-',
                    bd=16, anchor='w')
lbl_service.grid(row=2, column=2)
txt_service = Entry(frame1, font=myfont, textvariable=result, bd=10,
                    insertwidth=4, bg='powder blue', justify='right')
txt_service.grid(row=2, column=3)

# Vigenère cipher
import base64

#function to encode
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr(ord(clear[i]) + ord(key_c) % 256)

        enc.append(enc_c)

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#fucntion to decode
def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)

        dec.append(dec_c)
    return "".join(dec)

def ref():
    # print("Message= ", (msg.get()))
    '''mine mod'''
    from tkinter.messagebox import showinfo
    showinfo('Message', 'Message='+msg.get())

    clear = msg.get()
    k = key.get()
    m = mode.get()

    if (m == 'e'):
        result.set(encode(k, clear))
    else:
        result.set(decode(k, clear))

#show message button
btn_total = Button(frame1, padx=16, pady=8, bd=16, fg='black',
                   font=myfont, width=10, text='Show Message',
                   bg='powder blue', command=ref).grid(row=7, column=1)

#reset button
btn_reset = Button(frame1, padx=16, pady=8, bd=16, fg='black',
                   font=myfont, width=10, text='Reset', bg='green',
                   command=reset).grid(row=7, column=2)

#exit button
btn_exit = Button(frame1, padx=16, pady=8, bd=16, fg='black',text='Exit', bg='red',
                  command=qExit).grid(row=7, column=3)

#keeps the window alive
root.mainloop()