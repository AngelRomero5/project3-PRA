# Created by Angel G. Romero Rosario on 10/24/2021

# This programs simulates the Optimal
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

# This function looks for the best page to replace using the optimal replacement algorithm
def optimal_replacement(vpage : page):
    
    # Set the fartest var to the first item in virtual memory
    fartest = 0 
    replacePage = 0

    # Check if the physical page is going to be accesed in the future
    for ppage in range(len(physical_memory)):

        # Check if the number will repeat later and then return if false
        if not any(x.get_page_address() == physical_memory[ppage] for x in vm):
            # Replace the page not referenced in the future
            physical_memory[ppage] = vpage.get_page_address()
            # print("Entre aqui")
            return

        # The program never worked as expected. It always replaced the last
        # Instance of a page: Ex: If the page "1" appeared 2 times it will pick 
        # the last time the page "1" appeared on VM. I tried to fix this with 
        # different approaches but coulnt come up with a solution. I left the break 
        # hoping it could work. Ill wait for feedback on this one

        # Check the first match of the fartest page in vm
        for i in range(len(vm)):
            
            # If the page matches on VM
            if vm[i].get_page_address() == physical_memory[ppage]:
                # If page index is greater than the current fartest index 
                if i > fartest:
                    fartest = i         # Update index
                    # print(fartest)
                    replacePage = ppage # Save the page to be replaced
                    break               # Exit so it takes only the first instance
                    

    # Replace the page with the virtual memory page
    # print(replacePage)
    physical_memory[replacePage] = vpage.get_page_address()

    
# Open file containing the virtual memory pages
with open(virtual_memory_path, 'r') as pageGetter:
    page_data = pageGetter.read().split()        # Read page data from file

for p in range(len(page_data)):

    tmp = page_data[p].split(":")    # Separate the operation from the page number
    mypage = page(tmp[0], tmp[1])    # Create page object
    vm.append(mypage)                # Append page object to end of the virtual memory list

while len(vm) != 0:
     
    vpage = vm.pop(0)  # Select next page in VM

    # If the page is not present in physical memory
    if None in physical_memory and vpage.get_page_address() not in physical_memory:

        physical_memory[position] = vpage.get_page_address()     # Save page to physical memory
        position += 1                       # Move to next available slot   
        page_faults += 1                    # Page fault occurs because page was not present
        # print(physical_memory)
        
    # If the page is not in PM and the PM is empty
    elif vpage.get_page_address() not in physical_memory and None not in physical_memory:
    
        page_faults += 1
        optimal_replacement(vpage)  # Optimal PRA
        # print(physical_memory)
    # Otherwise page hit
    else:
        page_hits +=1 
        # print(physical_memory)


''' Print Results '''

print(" This is the final form of the physical memory : ")
print(physical_memory)                              # Print final result on physical memory
print(" Times a page fault occured : ", page_faults)         # Print quantity of page faults
print("Page hits : ", page_hits)

