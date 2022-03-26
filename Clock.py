# Created by Angel G. Romero Rosario on 10/24/2021

# This programs simulates the Working set clock page
# replacement algorithm 

import sys
from page import page

# With this the user can specify physical memory size and virtual memory path
if __name__ == "__main__":
    physical_memory_size = int(sys.argv[1])
    tau = int(sys.argv[2])
    virtual_memory_path = str(sys.argv[3])

page_faults = 0                                     # Page fault's counter
page_hits = 0                                       # Page hit's counter
total_tola = 1                                      # Current virtual time

virtual_memory = []                                 # Virtual memory list
physical_memory = [None] * physical_memory_size     # Physical Memory List
position = 0                                        # Position on the Physical memory

# Initialize virtual memory
def init_virtualM():
    # Open file containing the virtual memory pages
    with open(virtual_memory_path, 'r') as pageGetter:
        page_data = pageGetter.read().split()        # Read page data from file

    for p in range(len(page_data)):

        tmp = page_data[p].split(":")    # Separate the operation from the page number
        mypage = page(tmp[0], tmp[1])    # Create page object
        virtual_memory.append(mypage)    # Append page object to end of the virtual memory list

# This function creates a "loop" condition on the physical memory list
def update_position(position):
    
    # If the position is at the end, change to the start
    if position == len(physical_memory)-1:
        return 0
    else:
        return position + 1     # Increment otherwise

# Where all the magic occurs
def clock_replacement():

    global page_hits, page_faults, total_tola, position

    # Travel all the virtual memory
    while len(virtual_memory) != 0:

        # Extract next page in VM
        vpage = virtual_memory.pop(0)

        # '''First Condition'''
        # If there is space available and the page is not on physical memory
        if None in physical_memory:
            # print("Entre aqui")

            found = False

            # Check if the page is in memory
            for i in physical_memory:

                if i == None:                 # Empty space: do nothing
                    break
                if i.get_page_address() == vpage.get_page_address():
                    i.change_operation(vpage.get_operation())    # Change operation 
                    i.change_tola(total_tola) # Update tola value
                    page_hits += 1            # Found page so increment counter
                    found = True              # found page so move on
                    break                     # Break out of the loop                 

            if not found:
                page_faults += 1                            # Increment page_faults counter 
                physical_memory[position] = vpage           # Add page to current position 
                physical_memory[position].change_tola(total_tola) # Save the tola to the page 
                position = update_position(position)        # Update current position

        # If there is not space available on physical memory    
        # '''Second Condition'''    
        else:
            
            page_found = False
            counter = 0

            # Check if the page exists in physical memory
            for i in physical_memory:

                # If the page exists, update the operation of the page and the tola
                if i.get_page_address() == vpage.get_page_address():
                    i.change_operation(vpage.get_operation())    # Change operation 
                    i.change_tola(total_tola)                    # Update tola value
                    page_hits += 1                               # Found page so increment counter
                    page_found = True                            # found page so move on
                    break                                        # Break out of the loop
            
            # If the page was found, exit from the 'else'
            if page_found:
                continue

            page_faults += 1 # Increment page faults counter

            # While the optimal page for replacement has not been found
            while not page_found:

                # If we searched the whole vm, look for the page with less tola
                if counter == physical_memory_size - 1:

                    minor = physical_memory[0].get_tola()   # The page with less tola
                    idx = 0                                 # Index of that page

                    # Search for the page with lowest tola and replace
                    for i in range(len(physical_memory)):

                        if physical_memory[i].get_tola() < minor:   # If th page's tola is smaller
                            minor = physical_memory[i].get_tola()   # Update minor's tola
                            idx = i                                 # Index of page with less tola

                    # Insert new page 
                    physical_memory[idx] = vpage                    # Replace page with new page
                    physical_memory[idx].change_tola(total_tola)    # Update tola on new page
                    position = update_position(idx)                 # Move hand by 1
                    page_found = True                               # exit loop
                    

                # If the page at current position is referenced
                elif physical_memory[position].is_referenced():
                     
                    physical_memory[position].dereference_page() # Dereference the page 
                    position = update_position(position)         # Update the position 
                    counter += 1                                 # Update counter

                # If page is not referenced
                elif not physical_memory[position].is_referenced():

                    # if total tola - tola not in working set, replace page
                    if (total_tola - physical_memory[position].get_tola()) > tau:

                        physical_memory[position] = vpage                 # Replace page 
                        physical_memory[position].change_tola(total_tola) # Update tola
                        position = update_position(position)              # Move hand by 1
                        page_found = True                                 # Found, exit loop
                    # Page was in working set, so move to the next page
                    else:
                        counter += 1                            # Increment counter
                        position = update_position(position)    # Move hand by 1

        total_tola += 1               # Increment time
    

############################################################################################################
'''Main Function'''
def main():

    # Initialize virtual memory
    init_virtualM()

    # Run the page replacement algorithm
    clock_replacement()

    # Print the results
    print("This is the final state of the list: ")

    for page in physical_memory:

        pagina = page.get_page_address()
        operation = page.get_operation()
        stringP = "Pagina - " + str(operation) + ":" + str(pagina)

        print(stringP)

    print("Page faults: ", page_faults-1)
    print("Page hits: ", page_hits)

main()