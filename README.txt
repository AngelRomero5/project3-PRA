Created by Ángel G. Romero Rosario on 10/24/2021

README.txt

The purpose of this collection of files is to represent 3 types of 
page replacement algorithms using python.

PM = physical memory
VM = virtual memory 

The page class simulates a page in memory:

  has the following methods: 
    def __init__(self, operation : chr, page_address : int):  # Class constructor
        self.operation = operation      # Page operation : R/W
        self.address = page_address     # Page address
        self.modified = 1               # Referenced bit
        self.tola = 0                   # Page tola
    
    def change_operation(self, o : chr) # This function changes the operation of the page
    def get_page_address(self) # This function returns the current page's address
    def get_operation(self)   # This function returns the operation type 
    def is_referenced(self)   # This function returns if the page has been modified or no
    def reference_page(self)  # This function changes reference bit
    def dereference_page(self) # This function changes reference bit
    def change_tola(self, t)  # This function changes the tola of the page
    def get_tola(self)        # This function returns the page's tola


ALGORITHMS -----------------------------------------------------------------------------------------

I. lifo.py :

    To run the program open the terminal and type:
            python lifo.py <physical-memory-size> <path-of-virtual-memory>


    This program accepts two arguments: 
        1. The physical memory size
        2. and the path of the virtual memory content

    When program starts, it simulates a physical memory using a list structure and it populates the list
    with Nones. After opening the file containing the virtual memory it creates a local copy of the virtual 
    memory appending page objects. After this is done, we set a for loop to go through every page in the vm:

        - if the page is not in the physical memory and a space is available, then add the page to the 
          physical memory but a page fault occurs because the page was not in the physical memory, increment
          page fault's counter variable and to next available position in physical memory.

        - if the page is not in the physical memory and the physical memory is full, use LIFO:
          replace the last page inserted into the physical memory with the new page. Basically this algorithm 
          will always replace only the last page inserted. After the new page is replaced, increment page 
          fault's counter. 

        - if there is a page hit increment page_hits counter, the program reads the next page in "virtual memory"

    This algorithm continues until the end of the "virtual memory" is reached. Finally, print the final state 
    of the physical memory and the number of page faults occured.  


II. Optimal.py:

    To run the program open the terminal and type:
            python Optimal.py <physical-memory-size> <path-of-virtual-memory>

    This program accepts 3 arguments:
            1. The physical memory size
            2. The tau 
            3. The path of the file with the virtual memory data

    When program starts, it simulates a physical memory using a list structure and it populates the list
    with Nones. After opening the file containing the virtual memory it creates a local copy of the virtual 
    memory appending page objects. After this is done, we set a for loop to go through every page in the vm
    and extracts the next page in VM:

      - If there is space in the physical memory and the page is not already in PM, add the page to the 
        next available spot and increment page_faults' counter
      
      - If the PM is full and the page is not on PM, run the Optimal replacement algorithm:
        * This algorithm goes through every page on the physical memory checking the following:
          1) If the current page in PM is not found in the VM, replace the page
             and exit the function.
        
          2) If the current page matches a page in VM, check if the index of that page is greater 
             than the current position index and save that PM page.
        
        After all of this is done, replace the page that wont be used for a while in the physical 
        memory with the new page

      - If the above was not True, increment Page Hits' counter

    This algorithm continues until the end of the "virtual memory" is reached. Finally, print the final state 
    of the physical memory and the number of page faults occured.  


III. Clock.py:

    To run the program open the terminal and type:
            python Clock.py <physical-memory-size> <tau> <path-of-virtual-memory>

  
    This program accepts 3 arguments:
            1. The physical memory size
            2. The tau - value to determine if a page is in the working set
            3. The path of the file with the virtual memory data

    # This program has 4 functions: 
        init_virtualM(),        # This function initializes the VM by reading from a dile containing the pages 
        update_position(),      # This function updates the position of the hand on the physicalmemory
        clock_replacement(),    # This function works as the working set clock page replacement algorithm 
        main()                  # main function where all the other functions are called

    hen program starts, it simulates a physical memory using a list structure and it populates the list
    with Nones. After opening the file containing the virtual memory it creates a local copy of the virtual 
    memory appending page objects. After this is done, we set a for loop to go through every page in the vm
    and extracts the next page in VM:

        - If there is space in the physical memory:

          1) Check first if the page is already in PM and replace it, update Reference bit, tola and the operation
             If the page is not on PM, add the page on PM, update page_fault's counter, save the tola and move hand by 1

        - If the memory is full:

          1) Check first if the page is already in memory, if so, update tola, reference bit and operation
          
          2) While the page to be replaced has not been found:

            * If the hand is pointing to a referenced page, dereference the page,
              increment the counter and move the hand by 1

            * If the hand is pointing to a dereferenced page, check if the page is in the working set
                 - If the page is not in working set:
                  replace the page in PM with the new page, move hand by 1, update referenced bit and 
                  tola and exit the loop

                - Of the page is in working set, increment counter and move hand by 1

            * If the hand did a complete turn and could not find a candidate:

              Look for the page with less tola and replace it with the new page, update tola, referencebit and 
              move hand by 1

            Print the final state of the list, with the page faults and the page hits. 