#for the stack data structure
import dst


#for parsing html file
from html.parser import HTMLParser


#for exit codes
import sys

#For filesystem navigation.
import os


class parser(HTMLParser):
	def __init__(self):
		super().__init__()
		self.stack = dst.Stack()

	#method handles all opening tags and push them 
	#to the stack
	def handle_starttag(self, tag, attrs):
		self.stack.push(tag)

	#method handles all closing tags and pops
	#the stack for each closing tag
	def handle_endtag(self, tag):
		self.stack.pop()

	#method handles all text and ignores them
	def handle_data(self, data):
		pass

	#method returns True if stack is empty
	def check_tags(self):
		return self.stack.is_empty()





class HTML_CHECK:
	"""This object is the main driver of the checker.
	"""
	def __init__(self):
		"""initializing all the needed variables"""
		self.balanced = False
		self.platform = None
		self.file_path = None
		self.file_name = input("Enter your file name:: ")



	def get_platform(self):
		"""Gets platform at which the code is being used"""
		self.platform = os.name
		if self.platform == 'nt':
			sep = '\\'
		else:
			sep = '/'
		return sep

	def get_file_name(self):
		"""Returns the filepath"""
		pwd = os.getcwd()
		self.file_path = pwd + self.get_platform() + self.file_name
		return self.file_path

	def file_handler(self):
		"""Opens the filepath and does all the file handling
		including getting file size and feeding the parser the 
		html text"""
		try:
			fi = self.get_file_name()
			with open(fi, 'r') as file:
				file_attrs = os.fstat(file.fileno())
				file_size = file_attrs.st_size
				if file_size == 0:
					print("Your File is Empty.....")
					sys.exit(-1)
				else:
					text = file.read()
					parse = parser()
					parse.feed(text)
					if parse.check_tags():
						print(f"Your HTML tags are balanced")
					else:
						print("Your HTML tags are not balanced")
			sys.exit(0)

		except FileNotFoundError:
			print('File Not Found. Exiting')
			sys.exit(-1)
if __name__ == '__main__':
	checker = HTML_CHECK()
	checker.file_handler()


