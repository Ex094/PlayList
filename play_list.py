import os

#List of Filenames from the Play List
playlist = []

#Get path from the User
path = raw_input("Input Directory Path: ")

#Function to write Playlist to a text file
def save_list(filenames, filename):
	with open(filename + ".txt", 'w') as file:
		for name in playlist:
			file.write(name + "\n")


def main():
	if not os.path.isdir(path):
		print("Path Invalid or does not Exist")
		sys.exit();

	#Iterate through each file in the given Path
	for file in os.listdir(path):
		#Check if audio file
		if(".mp3" in file):
			playlist.append(file.replace(".mp3", ""))

	#Ask for filename
	filename = raw_input("Enter Playlist Name: ")
	save_list(playlist, filename)