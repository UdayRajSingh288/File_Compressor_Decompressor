from tkinter import END
from pathlib import Path
from shutil import copy
import lz4.frame
import zipfile
import snappy
import gzip
import lzma
import zlib
import bz2

def decompress(src, dst):
	src_fp = src.get(1.0, END).strip()
	dst_fp = dst.get(1.0, END).strip()
	if src_fp and dst_fp:
		ext = Path(src_fp).suffix
		if ext == '.zip':
			with zipfile.ZipFile(src_fp, 'r') as zip_ref:
				zip_ref.extractall(dst_fp)
		elif ext == '.gz':
			with gzip.open(src_fp, 'rb') as f_in:
				with open(dst_fp + '/output.data', 'wb') as f_out:
					f_out.write(f_in.read())
		elif ext == '.bz2':
			with bz2.open(src_fp, 'rb') as f_in:
				with open(dst_fp + '/output.data', 'wb') as f_out:
					f_out.write(f_in.read())
		elif ext == '.xz':
			with lzma.open(src_fp, 'rb') as f_in:
				with open(dst_fp + '/output.data', 'wb') as f_out:
					f_out.write(f_in.read())
		elif ext == '.zlib':
			with open(src_fp, 'rb') as f_in:
				compressed_data = f_in.read()
				decompressed_data = zlib.decompress(compressed_data)
				with open(dst_fp + '/output.data', 'wb') as f_out:
					f_out.write(decompressed_data)
		elif ext == '.lz4':
			with lz4.frame.open(src_fp, 'rb') as f_in:
				with open(dst_fp + '/output.data', 'wb') as f_out:
					f_out.write(f_in.read())
		elif ext == '.snappy':
			with open(src_fp, 'rb') as f_in:
				compressed_data = f_in.read()
				decompressed_data = snappy.uncompress(compressed_data)
				with open(dst_fp + '/output.data', 'wb') as f_out:
					f_out.write(decompressed_data)
		else:
			copy(src_fp, dst_fp + '/output.data')