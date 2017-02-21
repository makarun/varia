#
#	moving/sorting filles
#
#	ToDo:
#		add creating directories
#		auto sorting - make dictionary
#


#import os
#import shutil
#def move(src, dest):
#	shutil.move(src,dest)

#print("os.path.basename(os.path.dirname(os.path.realpath(__file__))):")
#print(os.path.basename(os.path.dirname(os.path.realpath(__file__))))

#print(os.getcwd()+"mp3")

#for filename in os.listdir():
#	if filename.endswith('.py'):
#		print(filename)

#for filename in os.listdir():
#	if filename.endswith('.py'):
#		move(filename, os.getcwd()+'/mp3')


#import os

#for filename in os.listdir():
#	if filename.endswith(".mp3"):
#		move(filename, os.getcwd()+"/mp3")

import os
import shutil

def move(src, dest):
	shutil.move(src,dest)

for filename in os.listdir():
	if filename.endswith(".txt"):
		move(filename, os.getcwd()+"/txt")
#
#	make sure directory exist beffore running!
#

