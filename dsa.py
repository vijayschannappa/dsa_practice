#linked list implementation
class node:
    def __init__(self,datavalue = None):
        self.datavalue = datavalue
        self.nextvalue = None
class slinkedlist:
    def __init__(self):
        self.headvalue = None

class slinkedlist_print:
    def __init__(self):
        self.headvalue = None
    def printlist(self):
        printval = self.headvalue
        while printval is None:
            print(printval.datavalue)
            printval = printval.nextvalue

#create linked list of first k numbers

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
def createsll(k):
    if k == 0:
        return None
    temp = node(1)
    head = temp
    for i in range(2,k+1):
        temp.next = node(i)
        temp = temp.next
    return head
    
#given the head, print the data values in the linked list
def printdata(head):
    if not head:
        print('no data')
    while head!=None:
        print(head.data)
        head = head.next

#insert data before first node
def insertData(head,data):
    temp = node(data)
    if head == None:
        return temp
    temp.nextaddr = head
    head = temp
    return head

#insert data at last node

def insertLast(head, data):
    last = node(data)
    temp = head
    if head == None:
        return last
    while head.nextaddr!=None:
        head = head.nextaddr
    head.nextaddr = last
    return head

#delete first node
def deleteFirstNode(head):
    if head == None:
        return head
    head = head.nextaddr
    return head

#implement stack in python

class stack:
    def __init__(self):
        self.mem = []
        self.size = 0
        self.top = -1
    
    def push(self,data):
        self.top +=1
        self.mem.append(data)
        self.size+=1
    
    def pop(self):
        if self.pop == -1:
            print('no data')
            return None
        else:
            self.mem.pop(self.top)
            self.top -= 1
            self.size -= 1

    def topst(self):
        if self.top == -1:
            print('stack empty')
            return None
        else:
            return self.mem(self.top)
    
    def printstack(self):
        print(self.mem)
    
    def getsize(self):
        print(f'size of the stack is {len(self.mem)}')


#Binary trees in python

class Node:
    def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    

        

#binary trees

class Node:
    def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
# Insert Node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
# Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
# Inorder traversal
# Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res
    
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.PrintTree()
print(root.inorderTraversal(root))      
print(root.PreorderTraversal(root))
print(root.PostorderTraversal(root))



#Given an array arr[] of length N ≥ 2.
#Remove an element from the given array such that the GCD of the array after removing it is maximized.


import math as mt

def MaxGCD(a, n):
    Prefix=[0 for i in range(n + 2)]
    Suffix=[0 for i in range(n + 2)]
    Prefix[1] = a[0]
    Suffix[n] = a[n - 1]
    for i in range(2,n+1):
        Prefix[i] = mt.gcd(Prefix[i - 1], a[i - 1])
    for i in range(n-1,0,-1):
        Suffix[i] =mt.gcd(Suffix[i + 1], a[i - 1])  
    ans = max(Suffix[2], Prefix[n - 1])
    for i in range(2,n):
        ans = max(ans, mt.gcd(Prefix[i - 1], Suffix[i + 1]))
    return ans

a=[14, 17, 28, 70]
n = len(a)
 
print(MaxGCD(a, n))


def sieveOfErat(n):
    prms = [True for i in range(n+1)]
    p = 2
    while (p*p <=n):
        if prms[p] == True:
            for i in range(p*p,n+1,p):
                prms[i] = False
        p+=1
    
    for i in range(2,n+1):
        if prms[i]:
            print(i)


def lpf(n) :
    least_prime = [0 for i in range(n + 1)]
    least_prime[1] = 1
    for i in range(2, n + 1) :
        if (least_prime[i] == 0) :
            # marking the prime number
            # as its own lpf
            least_prime[i] = i
            # mark it as a divisor for all its
            # multiples if not already marked
            for j in range(i * i, n + 1, i) :
                if (least_prime[j] == 0) :
                    least_prime[j] = i
     
    for i in range(1, n + 1) :
        print("Least Prime factor of "
              ,i , ": " , least_prime[i] )
















#Find the Prime Numbers in a Given Interval in Python

# Method 1: Using inner loop Range as [2, number-1].
# Method 2: Using inner loop Range as [2, number/2].
# Method 3: Using inner loop Range as [2, sqrt(number)].


def first_methdod():
    low, high = 2, 10
    primes = []
    for i in range(low, high + 1):
        flag = 0
        if i < 2:
            continue
        if i == 2:
            primes.append(2)
            continue
        for x in range(2, i):
            if i % x == 0:
                flag = 1
                break
        if flag == 0:
            primes.append(i)



def second_method():
    low, high = 2, 10
    primes = []

    for num in range(low, high + 1):
        flag = 0
        if num < 2:
            flag = 1   
        if num % 2 == 0:
            continue
        if num == 2:
            primes.append(2)
            continue
        iter = 2

        while iter < int(num / 2):
            if num % iter == 0:
                flag = 1
                break
            iter += 1

        # sqrt method
        while iter < int(pow(num,0.5)):
            if num % iter == 0:
                flag = 1
                break
            iter += 1

    if flag == 0:
        primes.append(num)

    print(primes)


#prime-factors-of-range-of-numbers


#Given an array arr[] containing GCD of every possible pair of elements of another array.
#The task is to find the original numbers which are used to calculate the GCD array.
#For example, if original numbers are {4, 6, 8} then the given array will be {4, 2, 4, 2, 6, 2, 4, 2, 8}.
#STEPS:

# Sort the array in decreasing order.
# Highest element will always be one of the original numbers. Keep that number and remove it from the array.
# Compute GCD of the element taken in the previous step with the current element starting from the greatest and discard the GCD value from the given array.
from math import sqrt, gcd
def findNumbers(arr, n):
    # Sort array in decreasing order
    arr.sort(reverse = True)
    #length of the frequency list should be equal to the greates element in the given gcd array to
    # store the frequency of all gcd elements.
    freq = [0 for i in range(arr[0] + 1)]
    # Count frequency of each element
    for i in range(n):
        freq[arr[i]] += 1
    # Size of the resultant array is always equal to root of the size of all elements 
    size = int(sqrt(n))
    brr = [0 for i in range(size)]
    l = 0
    for i in range(n):
        if (freq[arr[i]] > 0):
            print(f'frequency of gcd element {arr[i]} is {freq[arr[i]]}')
            # Store the highest element in the resultant array
            brr[l] = arr[i]
            # Decrement the frequency of that element
            freq[arr[i]] -= 1
            print(f'frequency array {freq}')
            l += 1
            print(f'original elements updated to {brr}')
            for j in range(l):
                if (i != j):
                   print(f'calculating gcd for {arr[i]}, {brr[j]} with i and j values as {i} and {j} respectively')
                   x = gcd(arr[i], brr[j])
                   print(f'gcd is {x}, reducing the count of {freq[x]} by 2')
                   freq[x] -= 2 # two because frequency of gcd elemnt 1 is increased by two times for every pair of element
                else:
                   print(f'ignoring calculating gcd for {arr[i]}, {brr[j]} with i and j values as {i} and {j} respectively')
                   
    print(f'original elements array is {brr}')

arr = [12, 5, 1, 1]
n = len(arr)
findNumbers(arr, n)

                   
 




        







