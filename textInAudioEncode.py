#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Dec 13, 2021 09:39:21 PM PKT  platform: Windows NT

import sys
import aes
import hashlib
from tkinter import BooleanVar, Label, messagebox, filedialog
from PIL import Image
import wave
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

#import autosave_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root, top, returnMsg
    root = tk.Tk()
    #autosave_support.set_Tk_var()
    top = Toplevel1 (root)
    #autosave_support.init(root, top)
    root.mainloop()

    temp = returnMsg
    returnMsg = None
    return temp

w = None
returnMsg = None

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

def destroy(option):
    global returnMsg, root
    returnMsg = option
    root.destroy()
    root = None

class Toplevel1:
    def __init__(self, top=None):
        global enableEncryption, enableTextFile
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

        top.geometry("600x363+468+138")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(0,  0)
        top.title("Audio Steganography (Encode)")
        top.configure(background="#d9d9d9")

        self.input_txt_label = tk.Text(top)
        self.input_txt_label.place(relx=0.017, rely=0.094, relheight=0.54
                , relwidth=0.523)
        self.input_txt_label.configure(background="white")
        self.input_txt_label.configure(font="TkTextFont")
        self.input_txt_label.configure(foreground="black")
        self.input_txt_label.configure(highlightbackground="#d9d9d9")
        self.input_txt_label.configure(highlightcolor="black")
        self.input_txt_label.configure(insertbackground="black")
        self.input_txt_label.configure(selectbackground="blue")
        self.input_txt_label.configure(selectforeground="white")
        self.input_txt_label.configure(wrap="word")

        self.back_button_label = ttk.Button(top, command= lambda: destroy("back"))
        self.back_button_label.place(relx=0.033, rely=0.865, height=35, width=76)

        self.back_button_label.configure(takefocus="")
        self.back_button_label.configure(text='''Back''')
        self.back_button_label.configure(cursor="hand2")

        self.label_input_text = ttk.Label(top)
        self.label_input_text.place(relx=0.017, rely=0.022, height=26, width=45)
        self.label_input_text.configure(background="#d9d9d9")
        self.label_input_text.configure(foreground="#000000")
        self.label_input_text.configure(font="TkDefaultFont")
        self.label_input_text.configure(relief="flat")
        self.label_input_text.configure(anchor='w')
        self.label_input_text.configure(justify='left')
        self.label_input_text.configure(text='''Text:''')

        self.label_input_name = ttk.Label(top)
        self.label_input_name.place(relx=0.557, rely=0.20, height=26, width=100)
        self.label_input_name.configure(background="#d9d9d9")
        self.label_input_name.configure(foreground="#000000")
        self.label_input_name.configure(font="TkDefaultFont")
        self.label_input_name.configure(relief="flat")
        self.label_input_name.configure(anchor='w')
        self.label_input_name.configure(justify='left')
        self.label_input_name.configure(text='''please import the file''')
        #self.style.map('TCheckbutton',background=
        #    [('selected', _bgcolor), ('active', _ana2color)])
        # self.button_enable_password = tk.Checkbutton(top, variable=enablePassword, onvalue=1, offvalue=0, command=enablePasswordF)
        # self.button_enable_password.place(relx=0.557, rely=0.248, relwidth=0.217
        #         , relheight=0.0, height=16)
        # #self.button_enable_password.configure(variable=autosave_support.tch48)
        # self.button_enable_password.configure(takefocus="")
        # self.button_enable_password.configure(background="#d9d9d9")
        # self.button_enable_password.configure(foreground="#000000")
        # self.button_enable_password.configure(text='''Enable Password:''')

        self.TEntry1 = ttk.Entry(top)
        self.TEntry1.place(relx=0.667, rely=0.309, relheight=0.085
                , relwidth=0.31)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")

        self.button_enable_encryption = tk.Checkbutton(top, variable=enableEncryption, onvalue='a', offvalue='b', command=enableEncryptionF)
        self.button_enable_encryption.place(relx=0.557, rely=0.463
                , relwidth=0.217, relheight=0.0, height=17)
        #self.button_enable_encryption.configure(variable=autosave_support.tch50)
        self.button_enable_encryption.configure(takefocus="")
        self.button_enable_encryption.configure(background="#d9d9d9")
        self.button_enable_encryption.configure(foreground="#000000")
        self.button_enable_encryption.configure(text='''Enable Encryption:''')

        self.TEntry2 = ttk.Entry(top)
        self.TEntry2.place(relx=0.617, rely=0.526, relheight=0.107
                , relwidth=0.36)
        self.TEntry2.configure(state="disabled")
        self.TEntry2.configure(takefocus="")
        self.TEntry2.configure(cursor="ibeam")

        self.button_input_file = ttk.Button(top, command=openfile)
        self.button_input_file.place(relx=0.567, rely=0.094, height=35
                , width=246)
        self.button_input_file.configure(takefocus="")
        self.button_input_file.configure(text='''Import''')

        self.button_save = ttk.Button(top, command=saveF)
        self.button_save.place(relx=0.433, rely=0.862, height=35, width=326)
        self.button_save.configure(takefocus="")
        self.button_save.configure(text='''Save''')

        self.label_input_password = ttk.Label(top)
        self.label_input_password.place(relx=0.567, rely=0.325, height=25
                , width=55)
        self.label_input_password.configure(background="#d9d9d9")
        self.label_input_password.configure(foreground="#000000")
        self.label_input_password.configure(font="TkDefaultFont")
        self.label_input_password.configure(relief="flat")
        self.label_input_password.configure(anchor='w')
        self.label_input_password.configure(justify='left')
        self.label_input_password.configure(text='''Password:''')

        self.label_input_key = ttk.Label(top)
        self.label_input_key.place(relx=0.567, rely=0.543, height=26, width=25)
        self.label_input_key.configure(background="#d9d9d9")
        self.label_input_key.configure(foreground="#000000")
        self.label_input_key.configure(font="TkDefaultFont")
        self.label_input_key.configure(relief="flat")
        self.label_input_key.configure(anchor='w')
        self.label_input_key.configure(justify='left')
        self.label_input_key.configure(text='''Key:''')

        self.enable_file_radiobutton = tk.Checkbutton(top, variable=enableTextFile, onvalue=1, offvalue=0, command=enableTextFileF)
        self.enable_file_radiobutton.configure(background="#d9d9d9")
        self.enable_file_radiobutton.configure(foreground="#000000")
        self.enable_file_radiobutton.place(relx=0.025, rely=0.741, relwidth=0.182
                , relheight=0.0, height=18)

        self.enable_file_radiobutton.configure(text='''Hide File''')
        self.enable_file_radiobutton.configure(cursor="hand2")

        self.select_file_button = ttk.Button(top, command=openfileTohide)
        self.select_file_button.place(relx=0.217, rely=0.865, height=35
                , width=96)
        self.select_file_button.configure(takefocus="")
        self.select_file_button.configure(text='''Select File''')
        self.select_file_button.configure(state="disabled")



file = ""
#enablePassword = 0
enableEncryption = 0
enableTextFile = 0
filetohide = ""
filetype = 0

def openfileTohide():
    global filetohide, filetype
    filetohide = filedialog.askopenfilename()#defaultextension="*.*", filetypes=[('text files', 'text'), ("jpg", "jpg"), ("wav", "wav")])
    
    if len(filetohide) < 5:
        filetohide = ""
        return 0
    try:
        with open(filetohide,'r') as data:
            data.readlines()
    except:
        if filetohide[filetohide.rfind('.'):] == ".wav":
            try:
                wave.open(filetohide, 'r')
                filetype = 1
            except:
                messagebox.showerror("Error", "Invalid file format try again")
                filetohide = ""
        elif filetohide[filetohide.rfind('.'):] == ".jpg" or filetohide[filetohide.rfind('.'):] == ".JPG":
            # try:
            #     Image.open(filetohide, 'r')
            #     filetype = 2
            # except:
            #     messagebox.showerror("Error", "Invalid file format try again")
            #     filetohide = ""
            filetype = 2
        else:
            messagebox.showerror("Error", "Invalid file format try again")
            filetohide = ""
        return 0
    # if len(file) <= 4:
    #     return 0
    
    # temp = open(file, 'r')
    # text = temp.read()
    

def saveF():
    global top, file, enableTextFile, filetohide, enableEncryption
    text =""
    if len(file) <= 4:
        messagebox.showerror("Error", "Please Import Image")
        return 0
    if filetype == 1:
        encodeAudioInAudio()
        return 0
    
    elif filetype == 2:
        encodeImageInAudio()
        return 0
    # if filetype == 2:
    #     encodeImgInAudio()
    #     return
    # elif filetype == 1:
    #     encodeAudioInAudio()
    #     return
    if len(top.TEntry1.get()) <= 0:
        messagebox.showerror("Error", "Please Enter the password")
        return 0
    if enableTextFile == 1:
        if len(filetohide) <= 4:
            messagebox.showerror("Error", "Please Select the file to hide first")
            return 0
        if filetype == 1:
            encodeAudioInAudio()
            return
        temp = open(filetohide, 'r')

        text = temp.read()
        temp.close()
    else:
        text = top.input_txt_label.get("1.0", "end")
        text = text[:-1]
        if len(text)==0:
            messagebox.showwarning("Warning", "Text is empty")
    newfile = filedialog.asksaveasfilename(defaultextension="*.*", filetypes=[(".wav", ".wav")])
    if len(newfile) <= 4:
        return 0
    temp = hashlib.sha256(text.encode())
    temp = temp.hexdigest()
    temp0 = temp + text
    text = temp0
    if enableEncryption == 'a':
        temp1 = aes.AESCipher(top.TEntry2.get())
        text = str(temp1.encrypt(text))
        text = text[2:-1]

    text += hashlib.sha256(top.TEntry1.get().encode()).hexdigest()

    
    encode(file, newfile, text)
        

def openfile():
    global file, top
    file = filedialog.askopenfilename(defaultextension="*.*", filetypes=[(".wav", ".wav")])
    if len(file) < 5:
        return 0
    try:
        wave.open(file,'rb')
        top.label_input_name.configure(text="*" + file[file.rfind('/'):])
    except:
        messagebox.showerror("Error", "Invalid file format try again")
        file = ""
        return 0


def encode(file, newfile, string):
    wavetemp = wave.open(file, 'rb')
    wavearr = list(wavetemp.readframes(wavetemp.getnframes()))
    
    binary = ''.join(format(ord(i), '08b') for i in string)
    
    if len(binary) > len(wavearr):
        messagebox.showerror("Error","Message is too large")
        return 0
    for i in range(len(binary)):
        if wavearr[i] % 2 == 0:
            if binary[i] == '1':
                wavearr[i] += 1
        else:
            if binary[i] == '0':
                wavearr[i] -= 1


    newaudio = wave.open(newfile, 'wb')
    newaudio.setparams(wavetemp.getparams())
    newaudio.writeframes(bytes(wavearr))
    newaudio.close()
    wavetemp.close()
    return

def encodeAudioInAudio():
    global file
    wavetemp = wave.open(file)
    wavearr = list(wavetemp.readframes(wavetemp.getnframes()))

    newaudio = wave.open(filetohide, 'rb')
    newwave = list(newaudio.readframes(newaudio.getnframes()))

    string = str(newaudio.getparams())
    string = chr(1) + string
    string += "####"
    binary = ''.join(format(ord(i), '08b') for i in string)
    
    if len(string) + len(newwave)*8 > len(wavearr):
        messagebox.showerror("Error","Message is too large")
        return 0

    a = 0
    for i in range(len(binary)):
        if wavearr[i] % 2 == 0:
            if binary[i] == '1':
                wavearr[i] += 1
        else:
            if binary[i] == '0':
                wavearr[i] -= 1
        a += 1

    for j in newwave:
        rgb = format(j, '08b')
        for k in rgb:
            if wavearr[a]%2 == 0:
                if k == '1':
                    wavearr[a] += 1
            else:
                if k == '0':
                    wavearr[a] -= 1
            a += 1

    newfile = filedialog.asksaveasfilename(defaultextension="*.*", filetypes=[(".wav", ".wav")])
    if(len(newfile)<=4):
        return 
    stegaudio = wave.open(newfile, 'wb')
    stegaudio.setparams(wavetemp.getparams())
    stegaudio.writeframes(bytes(wavearr))
    stegaudio.close()
    return

def enableEncryptionF():
    global top, enableEncryption
    if enableEncryption == 'a':
        top.TEntry2.configure(state="disabled")
        enableEncryption = 'b'
    else:
        top.TEntry2.configure(state="normal")
        enableEncryption = 'a'


def encodeImageInAudio():
    img2 = Image.open(filetohide)
    wavetemp = wave.open(file, 'rb')

    wavearr = list(wavetemp.readframes(wavetemp.getnframes()))
    pixels= img2.load()
    a = 0
    string = "00000010" + format(img2.size[0]//256, '08b') + format(img2.size[0]%256, '08b') + format(img2.size[1]//256, '08b') + format(img2.size[1]%256, '08b')
    
    if len(string) + img2.size[0]*img2.size[1]*24 > len(wavearr):
        messagebox.showerror("Error","Message is too large")
        return 0
    for k in string:
        if a >= len(wavearr):
            return
        if wavearr[a]%2 == 0:
            if k == '1':
                wavearr[a] += 1
        else:
            if k == '0':
                wavearr[a] -= 1 
        a += 1
        
    height1, width1 = 0, 0
    rgb2=None
    for i in range(img2.size[0]):
        for j in range(img2.size[1]):
            rgb = pixels[i, j]
            rgb = inttobin(rgb)
            for k in rgb:
                if a >= len(wavearr):
                    return
                if wavearr[a]%2 == 0:
                    if k == '1':
                        wavearr[a] += 1
                else:
                    if k == '0':
                        wavearr[a] -= 1 
                a += 1
    
    newfile = filedialog.asksaveasfilename(defaultextension="*.*", filetypes=[(".wav", ".wav")])
    if(len(newfile)<=4):
        return 
    newaudio = wave.open(newfile, 'wb')
    newaudio.setparams(wavetemp.getparams())
    newaudio.writeframes(bytes(wavearr))
    newaudio.close()





def inttobin(rgb):
    r, g, b = rgb
    return (format(r, '08b')+format(g, '08b')+format(b, '08b'))

def bintoint(rgb):
    return (int(rgb[0:8], 2), int(rgb[8:16], 2), int(rgb[16:24], 2))



def enableTextFileF():
    global top, enableTextFile
    if enableTextFile == 0:
        top.input_txt_label.configure(state="disabled")
        top.select_file_button.configure(state="normal")
        enableTextFile = 1
    else:
        top.input_txt_label.configure(state="normal")
        top.select_file_button.configure(state="disabled")
        enableTextFile = 0



if __name__ == '__main__':
    vp_start_gui()
