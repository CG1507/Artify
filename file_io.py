import codecs
import os

def make_dir(dir_list, dir_location):
	for item in dir_list:
		directory = dir_location + item 
		if not os.path.exists(directory):
		    os.makedirs(directory)

def create_file(file_address, mode = 'w'):
	fout = codecs.open(file_address, mode, 'utf-8')
	return fout

def read_file(file_address, mode = 'r'):
	fout = codecs.open(file_address, mode, 'utf-8')
	return fout

def write_line(file_pointer, line):
	file_pointer.write(str(line))

def list_txt_files(folder_address, ends_with = ".txt"):
	return [file.split('.')[-2] for file in os.listdir(folder_address) if file.endswith(ends_with)]
