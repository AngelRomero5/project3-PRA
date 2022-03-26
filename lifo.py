# Created by Angel G. Romero Rosario on 10/24/2021

# This programs simulates the First in First Out Page
# replacement algorithm 

import sys
from page import page 

# With this the user can specify physical memory size and virtual memory path
if __name__ == "__main__":
    physical_memory_size = int(sys.argv[1])
    virtual_memory_path = str(sys.argv[2])

physical_memory = [None] * physical_memory_size   # Populate the "physical memory" with None
page_data = []                                    # Page data from the file
vm = []                                           # This is the virtual memory, currently empty

page_faults = 0                                   # Times a page fault happened
page_hits = 0                                     # Times a page hit happened
position = 0                                      # Position on physical memory       


# Open file containing the virtual memory pages
with open(virtual_memory_path, 'r') as page_getter:
    page_data = page_getter.read().split()   # Read text file

# For every entry in the page_data list
for p in range(len(page_data)):

    tmp = page_data[p].split(":")    # Separate the operation from the page number
    mypage = page(tmp[0], tmp[1])    # Create page object
    vm.append(mypage)                # Append page object to end of the virtual memory list

# Page replacement algorithm
for p in range(len(vm)):

    # If the physical memory has space and the page is not in physical memory
    if None in physical_memory and (vm[p].get_page_address() not in physical_memory):

        physical_memory[position] = vm[p].get_page_address()    # Add the page to the physical memory
        position += 1                                           # Increment position on physical memory
        page_faults += 1                                        # Increment page fault counter

    # If the page is not in physical memory and the physical memory is full
    elif vm[p].get_page_address() not in physical_memory and None not in physical_memory:

        physical_memory[position-1] = vm[p].get_page_address()   # Replace last page for new one  
        page_faults += 1                                         # Increment page faults counter
    
    # Else: page was found. Increment page hits counter
    else:
        page_hits +=1


'''Print all the results'''

print("\n This is the final state of the physical memory : ")
print(*physical_memory, sep=", ")                              # Print final result on physical memory
print(" Times a page fault occured : ", page_faults)           # Print quantity of page faults
print(" Print the page hits: ", page_hits)                     # Page hits