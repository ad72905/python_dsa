# Data structures covered:
# ------------------------

def data_structures():
    print('Data Structures Covered:')
    print('-------------------------')

    print('Arrays')
    print('Linked Lists')
    print('Doubly Linked Lists')
    print('Binary Search Trees')
    print('AVL Trees')
    print('Red Black Trees')
    print('Heaps')
    print('Tries')


def abstract_data_types():
    print('Abstract Data Types Covered:')
    print('----------------------------')

    print('Stacks - implement via array and linked list')
    print('Queues - implement via array and linked list')
    print('Priority Queue - implement via heap')
    print('Associative Arrays (Dictionaries) / Hashtable / Hash Map - implement via array')

# Data Structures Overview:
# -------------------------

# Data structures are an efficient way to store and retrieve data with an aim to speed up data intensive applications

# Data structures consume memory but the cost is more than offset by reduction in application running time.

# The running time complexity of an algorithm is determined by the underlying data structures used in implementation

# The trade off between running time complexity of an algorithm and the memory complexity
# of the data structures used in the implementation pushes the need for intelligent choice
# for data structure and thereafter, it's corresponding implementation for exhaustive efficiency

# Abstract Data Types (ADT):
# --------------------------

# They define the model or the logical description for a certain data structure

# It is like a supertype in programming (like an interface or an abstract class)

# We define the methods the underlying data structure will have so as to define
# the basic behavioural working of the abstract data type

# Always remember that ADT is just the model / logical description / specification
# ADT NEVER specifies the CONCRETE IMPLEMENTATION or the PROGRAMMING LANGUAGE

# For example, a stack is an ADT and push(), pop(), peek() are the specifications/methods
# The details around what data structure to be used to provide corresponding implementation are not with ADT

# Data structures define the concrete implementation or the actual representation of data

# The goal is to have the fastest implementation for - insert, remove, find in O(1)

# Data structures example : arrays, linked lists, binary search trees, hashtable

# In nutshell, ADT defines behaviour, DS defines concrete implementation

# Arrays:
# -------
# Lists in python are dynamic arrays

# Items of an array are located right next to each other in the main memory(RAM)

# Items of an array can be accessed by an index - random access - O(1) running time for random access

# As opposed to other programming languages, an array in Python can store different types of data items

# Two types of arrays : Static Arrays and Dynamic Arrays

# Static Array : Size of the array does not change

# Dynamic Array : Size of the array may change dynamically

# Applications of Arrays : More complex data structures rely HEAVILY on arrays
# because of random accessing in O(1) - access of items with known indices
# For e.g. stacks, queues, dictionaries (hash-tables)
# Numerical methods use arrays : numpy, matrix related operations become easy

# Array Operations:
# -----------------

# Case 1 : Adding items at end of array until it is full - O(1)

# Implementation using static array allows non-wastage of memory (efficient memory)
# utilisation but we have to resize the array often with O(N) running time
# as we have to first create a new fixed size array and then shift current arrays
# elements to the new array

# Implementation using dynamic array assumes the allocation of huge array at the
# beginning itself. This comes at the cost of memory wastage due to large size but
# we don't have to resize the array now. Insertion at the end, thus becomes O(1)

# Case 2 : Adding items at any arbitrary position with a given index
# The worst case would be to insert an item at the beginning, in which case,
# all the items will have to be shifted by an index of 1, therefore, O(N)
# running time complexity.

# The complexity remains same for both static and dynamic arrays

# Case 3 : Removing LAST item from an array
# Whether static or dynamic, LAST item can be removed from an array in O(1)

# Case 4 : Removing an item from an arbitrary position without a known index
# We typically have to locate the item first using a linear search in O(N)
# and then remove the item in O(1) and then deal with the hole in the array
# by shifting the remaining items in O(N)
# The complexity remains the same for both - static and dynamic array

# Arrays Conclusion:
# ------------------

# Manipulating the last item (insertion and removal) takes O(1) running time
# Manipulating an arbitrary item (insertion and removal) takes O(N) running time

# Arrays Advantages:
# ------------------

# We can use random access in O(1)
# Best to use arrays when we want to manipulate the last items in a data structure
# or when we want to access items with known indexes

# Arrays Disadvantages:
# ---------------------

# We have to know the number of items we want to store
# at compile time, so it is not a dynamic data structure

# Since, it is not a dynamic data structure, we always have to resize it in O(N) in case it is full

# Usually, we cannot store items with different types in an array - in Python, we can

# Arrays in Python:
# -----------------

# There are no real arrays in Python because everything is an object

# Numpy is a library exclusively used to handle the arrays (50x faster run times)

# Numpy is the best library when speed and numerical methods are crucial

# Numpy is written in Python but the most crucial operations are in C, C++

# Everything is an object in Python

# The usual LIST stores references to the integer objects or to the so called array objects
# Every reference is 8 bytes in size, where as in other programming languages, it's 4 bytes
# This is why storing a lot of items in a list has huge memory complexity

# Numpy arrays are stored in a continuous block in the memory - items are right next to each other

# Linked List:
# ------------

# Another data structure and the goal remains the same - to store data
# efficiently so that insertion and removal operations are fast

# Arrays have a huge disadvantage of being left with holes in the data after insertion
# and deletion operations at arbitrary location that are to be taken care of by shifting

# The above problem can be solved using a Linked List because we have
# access to the first node(head) of the list and other items can be
# accessed starting with this node. Also, the last node always points to NULL.

# Structure of a Linked List:
# ---------------------------

# Every node of a linked list has two parts to it : 1) data 2) reference to the next node

# This is why linked list need more memory than an array of the same size

# If we see, this is the reason, there are never any holes in a linked list

# As a result, there is never a need to shift the items (iteration is carried out using reference)

# As the nodes are NOT STORED NEXT TO EACH OTHER in the memory, there is NO RANDOM INDEXING

# Linked List gives us more flexibility to implement more complex data structures and ADTs like stacks and queues

# Finding an arbitrary item in a linked list STILL has O(N) running time

# Remember that we always have access to the first node of a linked list

# Remember that last item of a linked list always points to NULL

# Linked List Operations:
# -----------------------

# Manipulating first item(Insertion or Removal) in O(1) time

# Manipulating arbitrary items(Insertion or Removal) in O(N) time

# Inserting or removing an item from/at an arbitrary location in the list takes O(N)
# time as we always need to perform a linear search first and that takes O(N) time

# Linked List Advantages:
# -----------------------

# Linked lists are dynamic data structures as they can
# acquire memory at run-time by inserting new nodes

# There is no need to resize the data structure in case of linked list

# We can grow the size ORGANICALLY - not a problem if we
# don't know the size of the linked list at compile time

# Manipulating the first item is fast - O(1)

# Can store different sized items where as typically
# arrays assume the items have the exact same size

# Linked lists are dynamic data structures where
# as arrays are static data structures

# Arrays vs Linked Lists Comparison:
# ---------------------------------

# 1) Dynamic and Static Data Structures :

# Arrays are static data structures - we have to know the size
# of the arrays in advance (or we have to resize it - think of
# hash maps)

# Linked Lists are dynamic data structures - they can grow
# organically based on the references (no resizing needed)

# 2) Random Access (Random Indexing)

# Items in an array are located right next to each other in the main memory(RAM)
# This is why we can use indices. (NOT TRUE IN PYTHON THOUGH as WE USE LIST FOR
# ONE-DIMENSIONAL ARRAY, AND NUMPY FOR HIGHER DIMENSIONS)

# There is no random access in a linked list data structure

# 3) Manipulating the first item

# Shift several items (all the items in worst-case) when manipulating
# the first (or any arbitrary except the last) items in arrays

# Linked lists are dynamic data structures - so we just
# have to update the references around the head node

# 4) Manipulating the last item

# There can not be holes in the data structure when manipulating the last items in arrays

# Linked Lists have access to the first node (head node) exclusively
# so in this case we have to traverse the whole list in O(N) running time

# 5) Memory Management

# Arrays do not need any extra memory

# Linked Lists on the other hand do need extra memory as they store references (pointers)

# IMPORTANT NOTE COMMON TO BOTH ARRAYS AND LINKED LISTS:

# Searching for an arbitrary item (or removing an arbitrary item) takes
# O(N) linear running time for both data structures. This is true for both
# insertion and removal operations at arbitrary locations in linked list and arrays

# Operation                 Linked List                     Array
# Search                        O(N)                         O(1) - KNOWN INDEX
# Insert at the start           O(1)                         O(N)
# Insert at the end             O(N)                         O(1)
# Waste Space                   O(N)-because of references   0 - because of no additional memory like references
# (Memory Complexity)

# Practical Real World Applications of Linked Lists

# Low Level Memory Management - malloc() and free() in C

# Applications tab in Windows showing a minimized screen for all currently running applications

# Windows Photoviewer (link between previous and current photograph)

# Blockchain (each node stores data and two hash values - previous and current hash)

#
