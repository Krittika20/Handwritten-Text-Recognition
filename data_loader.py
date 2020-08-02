# data_loader.py
# Created by Prachi Goyal on 01/08/20.
# Copyright © 2020 Prachi Goyal. All rights reserved.

import os
from PIL import Image
import numpy as np


def resize(img):
	w, h = img.size
	BASE_WIDTH, BASE_HEIGHT = 128, 32

	def adjust_dim():
		if BASE_HEIGHT >= h * BASE_WIDTH / w:
			return BASE_WIDTH, h * BASE_WIDTH / w
		elif BASE_WIDTH >= w * BASE_HEIGHT / h:
			return w * BASE_HEIGHT / h, BASE_HEIGHT
		else:
			return BASE_WIDTH, BASE_HEIGHT

	new_dim = tuple(map(int, adjust_dim()))
	new_img = Image.new('L', (BASE_WIDTH, BASE_HEIGHT), 255)
	img = img.resize(new_dim, Image.ANTIALIAS)
	assert(img.size[0] <= new_img.size[0] and img.size[1] <= new_img.size[1])
	new_img.paste(img)
	return new_img
	

def image_loader(filepath):
	X = []
	X_filename = []
	for dir, parent_file, files in os.walk(filepath):
		for filename in files:
			path = os.path.join(dir, filename)
			if filename[-3 : ] == 'png' and os.stat(path).st_size > 0:
				img = resize(Image.open(path).copy())
				X.append(np.array(img.histogram()))
				X_filename.append(filename[:-4])
				i += 1
	return np.array(X), X_filename
	

def text_loader(filepath):
	Y = {}
	file = open(filepath, 'r')
	for info in file:
		if info[0] == '#':
			pass
		info = info.split(" ")
		filename = info[0]
		word = info[-1]	
		Y[filename] = word
	return Y				


def data_loader(image_filepath, text_filepath):
	X, X_filename = image_loader(image_filepath)
	Y = text_loader(text_filepath)
	return X, X_filename, Y