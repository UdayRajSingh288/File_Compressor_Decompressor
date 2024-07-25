from tkinter import Toplevel, Text, filedialog, Button, END
from PIL import Image, ImageTk
import zstandard as zstd
import lz4.frame
import zipfile
import shutil
import snappy
import gzip
import lzma
import zlib
import bz2


def set_icon(root):
	icon_image = Image.open('icon.png')
	icon_photo = ImageTk.PhotoImage(icon_image)
	root.iconphoto(False, icon_photo)

def select_src_file(txt):
	fp = filedialog.askopenfilename(title = 'Select file to compress')
	txt.delete(1.0, END)
	txt.insert(END, fp)

def select_dst_file_zip(txt):
	fp = filedialog.asksaveasfilename(defaultextension = ".zip", filetypes=[("Zip files", "*.zip"), ("All files", "*.*")], title = "Save zip file")
	txt.delete(1.0, END)
	txt.insert(END, fp)

def select_dst_file_gzip(txt):
	fp = filedialog.asksaveasfilename(defaultextension = ".gz", filetypes=[("Gzip files", "*.gz"), ("All files", "*.*")], title = "Save gzip file")
	txt.delete(1.0, END)
	txt.insert(END, fp)

def select_dst_file_bzip2(txt):
	fp = filedialog.asksaveasfilename(defaultextension = ".bz2", filetypes=[("Bzip2 files", "*.bz2"), ("All files", "*.*")], title = "Save bzip2 file")
	txt.delete(1.0, END)
	txt.insert(END, fp)

def select_dst_file_lzma(txt):
	fp = filedialog.asksaveasfilename(defaultextension = ".xz", filetypes=[("Lzma files", "*.xz"), ("All files", "*.*")], title = "Save lzma file")
	txt.delete(1.0, END)
	txt.insert(END, fp)

def select_dst_file_zlib(txt):
	fp = filedialog.asksaveasfilename(defaultextension = ".zlib", filetypes=[("Zlib files", "*.zlib"), ("All files", "*.*")], title = "Save zlib file")
	txt.delete(1.0, END)
	txt.insert(END, fp)

def select_dst_file_lz4(txt):
	fp = filedialog.asksaveasfilename(defaultextension = ".lz4", filetypes=[("Lz4 files", "*.lz4"), ("All files", "*.*")], title = "Save lz4 file")
	txt.delete(1.0, END)
	txt.insert(END, fp)

def select_dst_file_snappy(txt):
	fp = filedialog.asksaveasfilename(defaultextension = ".snappy", filetypes=[("Snappy files", "*.snappy"), ("All files", "*.*")], title = "Save snappy file")
	txt.delete(1.0, END)
	txt.insert(END, fp)


def cmp_zip_compress(src, dst):
	src_fp = src.get(1.0, END).strip()
	dst_fp = dst.get(1.0, END).strip()
	if src_fp and dst_fp:
		with zipfile.ZipFile(dst_fp, 'w', compression = zipfile.ZIP_DEFLATED, compresslevel = 9) as zipf:
			zipf.write(src_fp, arcname = src_fp.split('/')[-1])

def cmp_zip(root):
	cw = Toplevel(root)
	cw.title('ZIP Compression Algorithm')
	cw.geometry('400x300')
	cw.resizable(False, False)
	set_icon(cw)
	src_txt = Text(cw, height = 1, width = 30)
	src_txt.pack(pady = 15)
	src_select = Button(cw, text = 'Select file to compress', command = lambda: select_src_file(src_txt))
	src_select.pack(pady = 15)
	dst_txt = Text(cw, height = 1, width = 30)
	dst_txt.pack(pady = 15)
	dst_select = Button(cw, text = 'Select zip file path', command = lambda: select_dst_file_zip(dst_txt))
	dst_select.pack(pady = 15)
	cmp = Button(cw, text = 'Compress', command = lambda: cmp_zip_compress(src_txt, dst_txt))
	cmp.pack(pady = 20)

def cmp_gzip_compress(src, dst):
	src_fp = src.get(1.0, END).strip()
	dst_fp = dst.get(1.0, END).strip()
	if src_fp and dst_fp:
		with open(src_fp, 'rb') as f_in:
			with gzip.open(dst_fp, 'wb', compresslevel = 9) as f_out:
				shutil.copyfileobj(f_in, f_out)

def cmp_gzip(root):
	cw = Toplevel(root)
	cw.title('GZIP Compression Algorithm')
	cw.geometry('400x300')
	cw.resizable(False, False)
	set_icon(cw)
	src_txt = Text(cw, height = 1, width = 30)
	src_txt.pack(pady = 15)
	src_select = Button(cw, text = 'Select file to compress', command = lambda: select_src_file(src_txt))
	src_select.pack(pady = 15)
	dst_txt = Text(cw, height = 1, width = 30)
	dst_txt.pack(pady = 15)
	dst_select = Button(cw, text = 'Select gzip file path', command = lambda: select_dst_file_gzip(dst_txt))
	dst_select.pack(pady = 15)
	cmp = Button(cw, text = 'Compress', command = lambda: cmp_gzip_compress(src_txt, dst_txt))
	cmp.pack(pady = 20)

def cmp_bzip2_compress(src, dst):
	src_fp = src.get(1.0, END).strip()
	dst_fp = dst.get(1.0, END).strip()
	if src_fp and dst_fp:
		with open(src_fp, 'rb') as f_in:
			with bz2.open(dst_fp, 'wb', compresslevel = 9) as f_out:
				f_out.writelines(f_in)

def cmp_bzip2(root):
	cw = Toplevel(root)
	cw.title('BZIP2 Compression Algorithm')
	cw.geometry('400x300')
	cw.resizable(False, False)
	set_icon(cw)
	src_txt = Text(cw, height = 1, width = 30)
	src_txt.pack(pady = 15)
	src_select = Button(cw, text = 'Select file to compress', command = lambda: select_src_file(src_txt))
	src_select.pack(pady = 15)
	dst_txt = Text(cw, height = 1, width = 30)
	dst_txt.pack(pady = 15)
	dst_select = Button(cw, text = 'Select bzip2 file path', command = lambda: select_dst_file_bzip2(dst_txt))
	dst_select.pack(pady = 15)
	cmp = Button(cw, text = 'Compress', command = lambda: cmp_bzip2_compress(src_txt, dst_txt))
	cmp.pack(pady = 20)

def cmp_lzma_compress(src, dst):
	src_fp = src.get(1.0, END).strip()
	dst_fp = dst.get(1.0, END).strip()
	if src_fp and dst_fp:
		with open(src_fp, 'rb') as f_in:
			with lzma.open(dst_fp, 'wb', preset = 9) as f_out:
				f_out.writelines(f_in)

def cmp_lzma(root):
	cw = Toplevel(root)
	cw.title('LZMA Compression Algorithm')
	cw.geometry('400x300')
	cw.resizable(False, False)
	set_icon(cw)
	src_txt = Text(cw, height = 1, width = 30)
	src_txt.pack(pady = 15)
	src_select = Button(cw, text = 'Select file to compress', command = lambda: select_src_file(src_txt))
	src_select.pack(pady = 15)
	dst_txt = Text(cw, height = 1, width = 30)
	dst_txt.pack(pady = 15)
	dst_select = Button(cw, text = 'Select lzma file path', command = lambda: select_dst_file_lzma(dst_txt))
	dst_select.pack(pady = 15)
	cmp = Button(cw, text = 'Compress', command = lambda: cmp_lzma_compress(src_txt, dst_txt))
	cmp.pack(pady = 20)

def cmp_zlib_compress(src, dst):
	src_fp = src.get(1.0, END).strip()
	dst_fp = dst.get(1.0, END).strip()
	if src_fp and dst_fp:
		with open(src_fp, 'rb') as f_in:
			data = f_in.read()
			compressed_data = zlib.compress(data, level = 9)
			with open(dst_fp, 'wb') as f_out:
				f_out.write(compressed_data)

def cmp_zlib(root):
	cw = Toplevel(root)
	cw.title('Zlib Compression Algorithm')
	cw.geometry('400x300')
	cw.resizable(False, False)
	set_icon(cw)
	src_txt = Text(cw, height = 1, width = 30)
	src_txt.pack(pady = 15)
	src_select = Button(cw, text = 'Select file to compress', command = lambda: select_src_file(src_txt))
	src_select.pack(pady = 15)
	dst_txt = Text(cw, height = 1, width = 30)
	dst_txt.pack(pady = 15)
	dst_select = Button(cw, text = 'Select zlib file path', command = lambda: select_dst_file_zlib(dst_txt))
	dst_select.pack(pady = 15)
	cmp = Button(cw, text = 'Compress', command = lambda: cmp_zlib_compress(src_txt, dst_txt))
	cmp.pack(pady = 20)

def cmp_lz4_compress(src, dst):
	src_fp = src.get(1.0, END).strip()
	dst_fp = dst.get(1.0, END).strip()
	if src_fp and dst_fp:
		with open(src_fp, 'rb') as f_in:
			data = f_in.read()
			compressed_data = lz4.frame.compress(data)
			with open(dst_fp, 'wb') as f_out:
				f_out.write(compressed_data)

def cmp_lz4(root):
	cw = Toplevel(root)
	cw.title('LZ4 Compression Algorithm')
	cw.geometry('400x300')
	cw.resizable(False, False)
	set_icon(cw)
	src_txt = Text(cw, height = 1, width = 30)
	src_txt.pack(pady = 15)
	src_select = Button(cw, text = 'Select file to compress', command = lambda: select_src_file(src_txt))
	src_select.pack(pady = 15)
	dst_txt = Text(cw, height = 1, width = 30)
	dst_txt.pack(pady = 15)
	dst_select = Button(cw, text = 'Select lz4 file path', command = lambda: select_dst_file_lz4(dst_txt))
	dst_select.pack(pady = 15)
	cmp = Button(cw, text = 'Compress', command = lambda: cmp_lz4_compress(src_txt, dst_txt))
	cmp.pack(pady = 20)

def cmp_snappy_compress(src, dst):
	src_fp = src.get(1.0, END).strip()
	dst_fp = dst.get(1.0, END).strip()
	if src_fp and dst_fp:
		with open(src_fp, 'rb') as f_in:
			data = f_in.read()
			compressed_data = snappy.compress(data)
			with open(dst_fp, 'wb') as f_out:
				f_out.write(compressed_data)

def cmp_snappy(root):
	cw = Toplevel(root)
	cw.title('Snappy Compression Algorithm')
	cw.geometry('400x300')
	cw.resizable(False, False)
	set_icon(cw)
	src_txt = Text(cw, height = 1, width = 30)
	src_txt.pack(pady = 15)
	src_select = Button(cw, text = 'Select file to compress', command = lambda: select_src_file(src_txt))
	src_select.pack(pady = 15)
	dst_txt = Text(cw, height = 1, width = 30)
	dst_txt.pack(pady = 15)
	dst_select = Button(cw, text = 'Select snappy file path', command = lambda: select_dst_file_snappy(dst_txt))
	dst_select.pack(pady = 15)
	cmp = Button(cw, text = 'Compress', command = lambda: cmp_snappy_compress(src_txt, dst_txt))
	cmp.pack(pady = 20)