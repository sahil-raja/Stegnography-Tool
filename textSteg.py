from tkinter.constants import TOP
from loremipsum import get_paragraphs, get_sentences, generate_paragraph, generate_sentence
from tkinter import messagebox, filedialog
import aes
import hashlib
import sys

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
    global returnValue, top
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Window (root)
    root.mainloop()
    temp=returnValue
    returnValue = None
    return temp

w = None

def destroy_Window():
    global w
    w.destroy()
    w = None

class Window:
    def __init__(self, top=None):
        global enableEncryption
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

        top.geometry("600x350+468+138")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(0,  0)
        top.title("Steganography Tool")
        top.configure(background="#ced5cf")
        top.configure(highlightbackground="#f0f0f0f0f0f0")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)


        self.label_input_password = ttk.Label(top)
        self.label_input_password.place(relx=0.67, rely=0.13, height=25
                , width=60)
        self.label_input_password.configure(background="#d9d9d9")
        self.label_input_password.configure(foreground="#000000")
        self.label_input_password.configure(font="TkDefaultFont")
        self.label_input_password.configure(relief="flat")
        self.label_input_password.configure(anchor='w')
        self.label_input_password.configure(justify='left')
        self.label_input_password.configure(text='''Password:''')

        self.label_input_key = ttk.Label(top)
        self.label_input_key.place(relx=0.667, rely=0.45, height=26, width=27)
        self.label_input_key.configure(background="#d9d9d9")
        self.label_input_key.configure(foreground="#000000")
        self.label_input_key.configure(font="TkDefaultFont")
        self.label_input_key.configure(relief="flat")
        self.label_input_key.configure(anchor='w')
        self.label_input_key.configure(justify='left')
        self.label_input_key.configure(text='''Key:''')


        self.TEntry1 = ttk.Entry(top)
        self.TEntry1.place(relx=0.667, rely=0.200, relheight=0.085
                , relwidth=0.31)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")

        self.button_enable_encryption = tk.Checkbutton(top, variable=enableEncryption, onvalue='a', offvalue='b', command=enableEncryptionF)
        self.button_enable_encryption.place(relx=0.657, rely=0.4
                , relwidth=0.217, relheight=0.0, height=17)
        #self.button_enable_encryption.configure(variable=autosave_support.tch50)
        self.button_enable_encryption.configure(takefocus="")
        self.button_enable_encryption.configure(background="#d9d9d9")
        self.button_enable_encryption.configure(foreground="#000000")
        self.button_enable_encryption.configure(text='''Enable Encryption:''')

        self.TEntry2 = ttk.Entry(top)
        self.TEntry2.place(relx=0.667, rely=0.526, relheight=0.085
                , relwidth=0.31)
        self.TEntry2.configure(state="disabled")
        self.TEntry2.configure(takefocus="")
        self.TEntry2.configure(cursor="ibeam")


        self.back_button_label = ttk.Button(top, command=lambda: destroy("back"))#, command=lambda: destroy_Toplevel1("back"))
        self.back_button_label.place(relx=0.01, rely=0.87, height=35
                                       , width=100)
        self.back_button_label.configure(takefocus="")
        self.back_button_label.configure(text='''Back''')
        self.back_button_label.configure(cursor="hand2")

        self.save_button_label = ttk.Button(top, command=encode)
        self.save_button_label.place(relx=0.827, rely=0.87, height=35
                                       , width=100)
        self.save_button_label.configure(takefocus="")
        self.save_button_label.configure(text='''Save''')
        self.save_button_label.configure(cursor="hand2")

        self.decode_button_label = ttk.Button(top, command=decode)
        self.decode_button_label.place(relx=0.41, rely=0.87, height=35
                                       , width=100)
        self.decode_button_label.configure(takefocus="")
        self.decode_button_label.configure(text='''Decode''')
        self.decode_button_label.configure(cursor="hand2")

        self.text_input_label = tk.Text(top)
        self.text_input_label.grid(column=20, row=10)
        self.text_input_label.configure(font="Arial 10")
        self.text_input_label.place(relx=0.05, rely=0.15, relheight=0.6
                                    , relwidth=0.6)
        self.text_input_label.configure(takefocus="")
        self.text_input_label.configure(cursor="ibeam")
        self.text_input_label.configure(relief="groove")

        self.label_intput_text = tk.Label(top)
        self.label_intput_text.place(relx=0.05, rely=0.11, width=65, height=15)
        self.label_intput_text.configure(background="#d9d9d9")
        self.label_intput_text.configure(foreground="#000000")
        self.label_intput_text.configure(relief="flat")
        self.label_intput_text.configure(anchor='w')
        self.label_intput_text.configure(justify='left')
        self.label_intput_text.configure(text="Input Text:")


returnValue = "none"
enableEncryption = 0

def enableEncryptionF():
    global top, enableEncryption
    if enableEncryption == 'a':
        top.TEntry2.configure(state="disabled")
        enableEncryption = 'b'
    else:
        top.TEntry2.configure(state="normal")
        enableEncryption = 'a'



def destroy(option):
    global root, returnValue
    returnValue = option
    root.destroy()

def encode():
    global top
    if len(top.TEntry1.get()) == 0:
        messagebox.showerror("Error", "Enter the Password")
        return 0
    elif len(top.TEntry1.get()) < 5:
        messagebox.showerror("Error", "Password length should be greater than 4")
        return 0
    file = filedialog.asksaveasfilename(defaultextension="*.*", filetypes=[(".txt", ".txt")])
    if len(file) <= 4:
        return 0
    text = top.text_input_label.get("1.0","end")

    if(len(text)-1 == 0 ):
        messagebox.showwarning("Warning", "Text box is empty")

    text = text[:-1]
    text = hashlib.sha256(text.encode()).hexdigest() + text
    if enableEncryption == 'a':
        temp = aes.AESCipher(top.TEntry2.get())
        text = temp.encrypt(text)
        text = str(text)[2:-1]
        
    text = str(text) + hashlib.sha256(top.TEntry1.get().encode()).hexdigest()

    binary = ''.join(format(ord(i), '08b') for i in text)
    sentences = get_sentences(len(binary)+9)
    file = open(file, "w")
    count = 0
    # \t denotes that the file has steganography text hidden
    sentences[0] += '\t\n'
    file.write(sentences[0])

    for i in range(1, len(binary)):
        if binary[i] == '0':
            sentences[i] += ' '
            sentences[i] += '\n'
            file.write(sentences[i])
        elif binary[i] == '1':
            sentences[i] += '  '
            sentences[i] += '\n'
            file.write(sentences[i])
    file.close()
    return


def decode():
    global top
    if len(top.TEntry1.get()) == 0:
        messagebox.showerror("Error", "Enter the Password")
        return 0
    elif len(top.TEntry1.get()) < 5:
        messagebox.showerror("Error", "Password length should be greater than 4")
        return 0
    filepath = filedialog.askopenfilename(defaultextension="*.*", filetypes=[(".txt", ".txt")])
    if len(filepath) < 4:
        return 0
    try:
        file = open(filepath, "r")
    except IOError:
        messagebox.showerror("Error", "Invalid File")
        return


    lines = file.readlines()
    count = 0
    flag = True
    ch = ""
    text = ""
    #bincheck = ""

    for line in lines:
        if flag:
            if line[len(line) - 2] == '\t':
                flag = False
            else:
                print("\nFile does not have steganography text")
                return

        if line[len(line) - 2] == ' ' and line[len(line) - 3] == ' ':
            ch += '1'
        elif line[len(line) - 2] == ' ':
            ch += '0'
        count += 1
        if count % 8 == 0:
            text += chr(int(ch, 2))
            ch = ""

    if hashlib.sha256(top.TEntry1.get().encode()).hexdigest() != text[-64:]:
        messagebox.showerror("Error", "Text is empty")
        return 0
    text = text[:-64]
    if (enableEncryption == 'a'):
        temp = aes.AESCipher(top.TEntry2.get())
        text = temp.decrypt(text)
    if (hashlib.sha256(text[64:].encode())==text[:64]):
        messagebox.showerror("Error", "Invalid Output")
        return 0
    messagebox.showinfo("Decoded Text", text[64:])

    file.close()
    return


if __name__ == '__main__':
    vp_start_gui()

