# Author : Davide Pollicino



def show_file(file_path):
	try:
		# with close automatically the file 
		with open(file_path) as f:
			for line in f:
				print(line)
	except (OSError , IOError) as e:
		print("could not find the file {0}".format(file_path))
		return 0


# test1 
show_file('file_example.txt')

# test 2
show_file('hello.txt')
