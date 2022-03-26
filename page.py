# Created by Angel G. Romero Rosario on 10/24/2021

# This class simulates an address page 
class page:

    # Class constructor
    def __init__(self, operation : chr, page_address : int):
        self.operation = operation      # Page operation : R/W
        self.address = page_address     # Page address
        self.modified = 1               # Referenced bit
        self.tola = 0                   # Page tola

    # This function changes the operation of the page
    # read or write (r, w)
    def change_operation(self, o : chr):
        self.operation = o

    # This function returns the current page's address
    def get_page_address(self):
        return self.address

    # This function returns the operation type 
    def get_operation(self):
        return self.operation

    # This function returns if the page has been modified or not
    def is_referenced(self):
        return self.modified

    # This functions changes the modified state of the page class
    def reference_page(self):
        self.modified = 1

    def dereference_page(self):
        self.modified = 0

    # This function changes the tola of the page
    def change_tola(self, t):
        self.tola = t

    # This function returns the page's tola
    def get_tola(self):
        return self.tola