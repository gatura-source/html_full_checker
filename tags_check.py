####Written By Bedan Gatura#####
####Written on 3rd March 2023####
####Version 1 ##########
########################################################################
#This is a simple Python Script that uses htmlparser package and stack #                                                    
#ADT to check if HTML tags are balanced                                #
#                                                                      #
#
#
########################################################################

#for filesystem navigation and platform specifics
import os

#for exit status codes
import sys

#for parsing html Docs
from html.parser import HTMLParser



class Stack:
    """Object that defines the stack ADT"""
    def __init__(self):
        """initializing the object"""
        self.items = []
    def push(self, item):
        """Adding items to stack method"""
        self.items.append(item)

    def pop(self):
        """Removing items from stack"""
        self.items.pop()

    def peek(self):
        """Getting topmost item from stack"""
        return self.items[-1]

    def size(self):
        """Getting Stack size"""
        return len(self.items)


    def is_empty(self):
        """Checking if Stack is empty"""
        if len(self.items) == 0:
            return True
        else:
            return False


class Parser(HTMLParser):
    """Parses the HTML file to get the tags"""
    def __init__(self):
        """Init Method"""
        super().__init__()
        self.stack = Stack()

    def handle_starttag(self, tag, attrs):
        """Handles the start tags and adds them to the stack"""
        self.stack.push(tag)

    def handle_endtag(self, tag):
        """Handles all closing tags and pops the stack"""
        self.stack.pop()

    def handle_data(self, data):
        """Handles all data by ignoring them"""
        pass

    def check_tags(self):
        """Returns size of stack"""
        return self.stack.is_empty()

class tagschecker:
    """Main module that handles file opening and other related
    processes"""
    def __init__(self):
        self.filename = input("Please Enter the file name:: ")
        self.platform = None
        self.file_path = None

    def get_platform(self):
        """Gets type of OS"""
        platform = os.name
        if platform == 'nt':
            self.platform = '\\'
        else:
            self.platform = '/'
        return self.platform

    def get_file_name(self):
        """Returns the filepath"""
        pwd = os.getcwd()
        self.file_path = pwd + self.get_platform() + self.filename
        return self.file_path

    def file_handler(self):
        """File opening and feeding text to parser"""
        try:
            fi = self.get_file_name()
            with open(fi, 'r') as file:
                file_attrs = os.fstat(file.fileno())
                file_size = file_attrs.st_size
                if file_size == 0:
                    print("Your File is empty")
                    sys.exit(-1)
                else:
                    text = file.read()
                    parse = Parser()
                    parse.feed(text)
                    if parse.check_tags():
                        print("The HTML tags are balanced")
                    else:
                        print("The HTML  tags are not balanced")
            sys.exit(0)
        except FileNotFoundError:
            print("File Not Found")
            sys.exit(-1)

if __name__ == "__main__":
    checker = tagschecker()
    checker.file_handler()




