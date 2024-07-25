from tkinter import Tk, filedialog, Button, Label, Toplevel, Text
from PIL import Image, ImageTk
from cmp_script import *
from dcmp_script import *

def dummy():
	pass


def set_icon(root):
	icon_image = Image.open('icon.png')
	icon_photo = ImageTk.PhotoImage(icon_image)
	root.iconphoto(False, icon_photo)


def cmp_file(root):
	cw = Toplevel(root)
	cw.title('Compression Algorithm Select')
	cw.geometry('400x300')
	cw.resizable(False, False)
	set_icon(cw)
	alg1 = Button(cw, text = 'ZIP', command = lambda: cmp_zip(cw))
	alg1.grid(row = 0, column = 0, padx = 75, pady = 20)
	alg2 = Button(cw, text = 'GZIP', command = lambda: cmp_gzip(cw))
	alg2.grid(row = 0, column = 1, padx = 75, pady = 20)
	alg3 = Button(cw, text = 'BZIP2', command = lambda: cmp_bzip2(cw))
	alg3.grid(row = 1, column = 0, padx = 75, pady = 20)
	alg4 = Button(cw, text = 'LZMA/XZ', command = lambda: cmp_lzma(cw))
	alg4.grid(row = 1, column = 1, padx = 75, pady = 20)
	alg5 = Button(cw, text = 'Zlib', command = lambda: cmp_zlib(cw))
	alg5.grid(row = 2, column = 0, padx = 75, pady = 20)
	alg6 = Button(cw, text = 'LZ4', command = lambda: cmp_lz4(cw))
	alg6.grid(row = 2, column = 1, padx = 75, pady = 20)
	alg7 = Button(cw, text = 'Snappy', command = lambda: cmp_snappy(cw))
	alg7.grid(row = 3, column = 0, padx = 75, pady = 20)

def select_cmp(txt):
	file_types = [("ZIP files", "*.zip"), ("GZIP files", "*.gz"), ("BZ2 files", "*.bz2"), ("LZMA/XZ files", "*.xz"), ("LZ4 files", "*.lz4"), ("ZLIB files", "*.zlib"), ("SNAPPY files", "*.snappy"), ("All files", "*.*")]
	fp = filedialog.askopenfilename(title = 'Select compressed file', filetypes = file_types)
	txt.delete(1.0, END)
	txt.insert(END, fp)

def select_dst(txt):
	fp = filedialog.askdirectory(title = 'Select destination folder')
	txt.delete(1.0, END)
	txt.insert(END, fp)

def dcmp_file(root):
	cw = Toplevel(root)
	cw.title('Decompression')
	cw.geometry('400x300')
	cw.resizable(False, False)
	set_icon(cw)
	src_txt = Text(cw, height = 1, width = 30)
	src_txt.pack(pady = 15)
	src_select = Button(cw, text = 'Select compressed file', command = lambda: select_cmp(src_txt))
	src_select.pack(pady = 15)
	dst_txt = Text(cw, height = 1, width = 30)
	dst_txt.pack(pady = 15)
	dst_select = Button(cw, text = 'Select destination folder', command = lambda: select_dst(dst_txt))
	dst_select.pack(pady = 15)
	dcmp_bu = Button(cw, text = 'Decompress', command = lambda:  decompress(src_txt, dst_txt))
	dcmp_bu.pack(pady = 20)

def info_win(root):
	cw = Toplevel(root)
	cw.title('All About Me')
	cw.geometry('400x300')
	cw.resizable(False, False)
	set_icon(cw)
	img = Image.open('self_img.gif')
	w = img.width // 4
	h = img.height // 4
	img = img.resize((w, h), Image.LANCZOS)
	ph = ImageTk.PhotoImage(img)
	l = Label(cw, image = ph)
	l.image = ph
	l.pack(pady = 10)
	l2 = Label(cw, text = 'Hi! This is me.\n\nYou can contact me at udayrajsingh288@gmail.com\n\nGithub: https://github.com/udayRajSingh288/\n\nLinkedIn: www.linkedin.com/in/uday-raj-singh-367537224')
	l2.pack(pady = 10)

if __name__ == "__main__":
	root = Tk()
	root.title('File Compressor Decompressor')
	root.geometry('400x300')
	root.resizable(False, False)
	set_icon(root)
	label = Label(root, text = 'Select the operation you want to perform')
	label.pack(pady = 20)
	cmp = Button(root, text="Compress File", command = lambda: cmp_file(root))
	cmp.pack(pady = 20)
	dcmp = Button(root, text="Decompress File", command = lambda: dcmp_file(root))
	dcmp.pack(pady = 20)
	info = Button(root, text="Meet The Dev", command = lambda: info_win(root))
	info.pack(pady = 20)
	root.mainloop()