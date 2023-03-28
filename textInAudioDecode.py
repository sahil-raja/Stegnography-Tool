#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Dec 13, 2021 10:22:03 PM PKT  platform: Windows NT

import sys
import wave
import aes
import hashlib
from tkinter import messagebox, filedialog
from tkinter.constants import DISABLED
from PIL import Image

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def vp_start_gui():
    global root, returnMsg, top
    '''Starting point when module is the main routine.'''
    global val, w, root, top
    root = tk.Tk()
    top = Toplevel1 (root)
    root.mainloop()
    temp = returnMsg
    returnMsg = None
    return temp

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    return (w, top)


def destroy(option):
    global root, returnMsg
    returnMsg = option
    root.destroy()
    root = None

returnMsg = None

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        global enablePassword, enableEncryption
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("405x403+468+138")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Audio Steganography (Decode)")
        top.configure(background="#d9d9d9")

        self.import_button = ttk.Button(top, command=openfile)
        self.import_button.place(relx=0.15, rely=0.025, height=35, width=323)
        self.import_button.configure(takefocus="")
        self.import_button.configure(text='''Import''')
        self.import_button.configure(cursor="hand2")

        self.back_button = ttk.Button(top, command=lambda: destroy("back"))
        self.back_button.place(relx=0.049, rely=0.025, height=35, width=38)
        self.back_button.configure(takefocus="")
        self.back_button.configure(text='''Back''')
        self.back_button.configure(cursor="hand2")

        self.decode_button = ttk.Button(top, command=printdecode)
        self.decode_button.place(relx=0.049, rely=0.744, height=35, width=366)
        self.decode_button.configure(takefocus="")
        self.decode_button.configure(text='''Decode''')
        self.decode_button.configure(cursor="hand2")

        self.saveInFile_button_1 = ttk.Button(top, command=saveInFile)
        self.saveInFile_button_1.place(relx=0.049, rely=0.868, height=35
                , width=366)
        self.saveInFile_button_1.configure(takefocus="")
        self.saveInFile_button_1.configure(text='''SaveInFile (*.txt)''')
        self.saveInFile_button_1.configure(cursor="hand2")

        self.style.map('TCheckbutton',background=
            [('selected', _bgcolor), ('active', _ana2color)])
        # self.enable_password = ttk.Checkbutton(top, variable=enablePassword, onvalue='a', offvalue='b', command=enablePasswordF)
        # self.enable_password.place(relx=0.049, rely=0.174, relwidth=0.321
        #         , relheight=0.0, height=21)
        # self.enable_password.configure(takefocus="")
        # self.enable_password.configure(text='''Enable Password''')
        # self.enable_password.configure(cursor="hand2")

        self.enable_encryption = ttk.Checkbutton(top, variable=enableEncryption, onvalue='c', offvalue='d', command=enableEncryptionF)
        self.enable_encryption.place(relx=0.049, rely=0.447, relwidth=0.321
                , relheight=0.0, height=21)
        self.enable_encryption.configure(takefocus="")
        self.enable_encryption.configure(text='''Enable Encryption''')
        self.enable_encryption.configure(cursor="hand2")

        self.password_entry = ttk.Entry(top)
        self.password_entry.place(relx=0.049, rely=0.298, relheight=0.102
                , relwidth=0.904)
        self.password_entry.configure(takefocus="")
        #self.password_entry.configure(state="disabled")
        self.password_entry.configure(cursor="ibeam")

        self.password_entry_1 = ttk.Entry(top)
        self.password_entry_1.place(relx=0.049, rely=0.571, relheight=0.102
                , relwidth=0.904)
        self.password_entry_1.configure(takefocus="")
        self.password_entry_1.configure(state="disabled")
        self.password_entry_1.configure(cursor="ibeam")

        self.label_key = ttk.Label(top)
        self.label_key.place(relx=0.049, rely=0.521, height=19, width=45)
        self.label_key.configure(background="#d9d9d9")
        self.label_key.configure(foreground="#000000")
        self.label_key.configure(font="TkDefaultFont")
        self.label_key.configure(relief="flat")
        self.label_key.configure(anchor='w')
        self.label_key.configure(justify='left')
        self.label_key.configure(text='''Key:''')

        self.label_password = ttk.Label(top)
        self.label_password.place(relx=0.049, rely=0.248, height=19, width=85)
        self.label_password.configure(background="#d9d9d9")
        self.label_password.configure(foreground="#000000")
        self.label_password.configure(font="TkDefaultFont")
        self.label_password.configure(relief="flat")
        self.label_password.configure(anchor='w')
        self.label_password.configure(justify='left')
        self.label_password.configure(text='''Password:''')


file = ""
enablePassword = 'a'
enableEncryption = 0

def openfile():
    global file
    file = filedialog.askopenfilename(defaultextension="*.*", filetypes=[(".wav", ".wav")])
    try:
        imgwave = wave.open(file,'rb')
    except:
        messagebox.showerror("Error", "Invalid file format try again")
        file = ""
        return 0


def saveInFile():
    global enableEncryption, enablePassword, top, file
    if len(file) < 5:
        messagebox.showerror("Error", "Please Import audio first")
        return 0
    newfile = filedialog.asksaveasfilename()#defaultextension="*.*", filetypes=[(".txt", ".txt")])
    string = decode1()
    temp = open(newfile, 'w')
    temp.write(string)
    temp.close()




def printdecode():
    global file
    if len(file) < 5:
        messagebox.showerror("Ereor", "Please Import audio first")
        return 0
    string = decode1()
    if string == 0:
        return 0
    messagebox.showinfo("Hidden text:", string)
    return
    
    
def decode1():
    if len(file) < 4:
        messagebox.showerror("Error", "Import Base file first")
        return

    deli ="####"
    if enablePassword == 'a':
        deli = top.password_entry.get()
        deli = hashlib.sha256(deli.encode()).hexdigest()
    
    wavetemp1 = wave.open(file, 'rb')
    wavearr1 = list(wavetemp1.readframes(wavetemp1.getnframes()))
    temp = ""
    string = ""
    first = True
    for i in range(0, 9):
        temp += str(wavearr1[i-1]%2)
        if i % 8 == 0 and i != 0:
            if first:
                first = False
                if int(temp, 2) == 1:
                    audiodecode()
                    return 0
                elif int(temp, 2) == 2:
                    decodeImageInAudio()
                    return 0


    string = decode(file, deli)
    if len(string) > 0:
        if enableEncryption == 'c':
            temp = aes.AESCipher(top.password_entry_1.get())
            string = temp.decrypt(string)
    if(string == 0):
        return 0
    cksum = hashlib.sha256(string[64:].encode()).hexdigest()
    
    return string[64:]
    

def decode(file, deli):
    wavetemp1 = wave.open(file, 'rb')
    wavearr1 = list(wavetemp1.readframes(wavetemp1.getnframes()))
    temp = ""
    string = ""
    first = True
    for i in range(0, len(wavearr1)):
        temp += str(wavearr1[i-1]%2)
        if i % 8 == 0 and i != 0:
            if first:
                first = False
                if int(temp, 2) == 1:
                    audiodecode()
                    return 0
            string += chr(int(temp, 2))
            if string.find(deli) != -1:
                return string[:string.find(deli)]
            temp = ""

    if(string.find(deli) == -1):
        return ""

    return string


def audiodecode():   
    global file     
    wavetemp = wave.open(file, 'rb')
    wavearr = list(wavetemp.readframes(wavetemp.getnframes()))

    newarr = []
    string = ""
    params=""
    first = False
    for i in wavearr:
        string += format(i, '08b')[-1]
        if len(string) >= 8:
            if not first:
                params += chr(int(string[0:8], 2))
                string = string[8:]
                if(params.find("####") != -1):
                    first = True
            else:
                newarr.append(int(string[0:8], 2))
                string = string[8:]

    newfile= filedialog.asksaveasfilename(defaultextension="*.*", filetypes=[(".wav", ".wav")])
    if len(newfile) < 4:
        return 0
    stegaudio = wave.open(newfile, 'wb')
    new = []
    temp = ""
    params = params[:-5].split(',')
    params = [i.split('=') for i in params]
    stegaudio.setparams(wave._wave_params(nchannels=int(params[0][1]), sampwidth=int(params[1][1]), framerate=int(params[2][1]), nframes=int(params[3][1]), comptype=params[4][1][1:-1], compname=params[5][1][1:-1]))
    stegaudio.writeframes(bytes(newarr[:int(params[3][1])*4]))


def decodeImageInAudio():
    newaudio = wave.open(file, 'rb')
    wavearr = list(newaudio.readframes(newaudio.getnframes()))

    string = ""

    
    for i in range(40):
        string += str(wavearr[i]%2)
    
    size1=( int(string[8:16], 2)*256 + int(string[16:24], 2), int(string[24:32], 2)*256 + int(string[32:40], 2))
    newimage = Image.new('RGB', size = size1)
    newpixels = newimage.load()
    j = 0
    k = 0
    for i in range(40,len(wavearr)):
        string += str(wavearr[i]%2)
        if len(string) > 23:
            if j < newimage.size[0]:
                if k < newimage.size[1]:
                    newpixels[j, k] = bintoint(string)
                    string = string[24:]
                    k += 1
                else:
                    j += 1
                    k = 0
            else:
                newfile = filedialog.asksaveasfilename(defaultextension="*.*", filetypes=[(".jpg", ".jpg"),(".png", ".png")])
                if(len(newfile)<=4):
                    return 
                newimage.save(newfile)
                return




def inttobin(rgb):
    r, g, b = rgb
    return (format(r, '08b')+format(g, '08b')+format(b, '08b'))

def bintoint(rgb):
    return (int(rgb[0:8], 2), int(rgb[8:16], 2), int(rgb[16:24], 2))


def enablePasswordF():
    global top, enablePassword
    if enablePassword == 'a':
        enablePassword = 'b'
        top.password_entry.configure(state="disabled")
    else:
        enablePassword = 'a'
        top.password_entry.configure(state="normal")



def enableEncryptionF():
    global top, enableEncryption
    if enableEncryption == 'c':
        enableEncryption = 'd'
        top.password_entry_1.configure(state="disabled")
    else:
        enableEncryption = 'c'
        top.password_entry_1.configure(state="normal")


if __name__ == '__main__':
    vp_start_gui()
