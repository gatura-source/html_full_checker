import dst

t_stack = dst.Stack()


import os
import sys

base_dir = os.getcwd()




def prime(fn):
    def wrapper(*args, **kwargs):
        v = fn(*args, **kwargs)
        v.send(None)
        return v
    return wrapper

class tag_checker():
    def __init__(self):
        #initializing states
        self.start = self._create_start()
        self.opening_tag = self._opening_tag()
        self.keyword = self._keyword()
        self.closing_tag = self._closing_tag()


        self.current_state = self.start
        self.stopped = False
        self.alphabet = " abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*{}()~"



    def send(self, char):
        """The method sends the current input to the current state
        it captures the stopiteration exception and marks the stopped
        flag"""

        try:
            self.current_state.send(char)

        except StopIteration:
            self.stopped = True



    def does_match(self):
        """The function at any point in time returns if till the current input
        the string matches the given regular expression.

        It does so by comparing the current state with the end state `q3`.
        It also checks for `stopped` flag which sees that due to bad input the iteration of FSM had to be stopped.
        """
        if self.stopped:
            return False
        return self.current_state == self.closing_tag



    @prime
    def _create_start(self):
        while True:
            char = yield
            if char == '<':
                self.current_state = self._opening_tag
            else:
                break


    @prime
    def _opening_tag(self):
        while True:
            char = yield
            if char in self.alphabet:
                self.current_state = self._keyword
            elif char == '>':
                self.current_state = self._closing_tag
            else:
                break

    @prime
    def _keyword(self):
        while True:
            char = yield
            if char in self.alphabet:
                self.current_state = self._keyword
            elif char == '>':
                self.current_state = self._closing_tag
            else:
                break

    @prime
    def _closing_tag(self):
        while True:
            char = yield
            break
def tags_match(word):
    evaluator = tag_checker()
    for ch in word:
        evaluator.send(ch)
    answer = evaluator.does_match()

tags_match("<html>")
# f = input('Please enter the file that needs checking:: ')
# ok = "Your HTML file is OK"
# err = "The tags are not balanced"
# f_error = "File not Found"
# file_dir = base_dir +'/'+ f
# reverse = []
# try:
#   with open(file_dir, 'r') as file:
#       for line in file:
#           for word in line.split():
#               tags_match(word)
#   if t_stack.is_empty():
#       print(f"{ok}")
#   else:
#       print(f"{err}")

# except FileNotFoundError:
#   print(f"{f_error}")

#   sys.exit(-1)



