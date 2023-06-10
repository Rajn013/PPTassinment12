#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Answer 1 .

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddleNode(head):
    if not head or not head.next:
        return None

    slow = fast = head
    prev = None

    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    prev.next = slow.next

    return head


# In[16]:


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

head = deleteMiddleNode(head)

current  = head
while current:
    print(current.val, end =" ")
    current = current.next


# In[17]:


head = ListNode(2)
head.next = ListNode(4)
head.next.next = ListNode(6)
head.next.next.next = ListNode(7)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(1)

head = deleteMiddleNode(head)

current  = head
while current:
    print(current.val, end =" ")
    current = current.next


# In[18]:


#Answer2.

def hasLoop(head):
    visited = set()
    
    current = head
    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
        
    return False


# In[19]:


head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = head.next 

has_loop = hasLoop(head)
print(has_loop)


# In[20]:


head = ListNode(1)
head.next = ListNode(8)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

has_loop = hasLoop(head)
print(has_loop)


# In[60]:


#Answer 3.

def NthFromEnd(head, n):
    slow = fast = head

    for _ in range(n):
        if fast is None:
            return -1
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    return slow.next.val if slow.next else -1


# In[67]:


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = ListNode(9)

n = 2
nth_from_end = NthFromEnd(head, n)
print(nth_from_end)


# In[65]:


head2 = ListNode(10)
head2.next = ListNode(5)
head2.next.next = ListNode(100)
head2.next.next.next = ListNode(5)

n2 = 5
nth_from_end2 = NthFromEnd(head2, n2)
print(nth_from_end2)


# In[98]:


#Answer 4.


def palindrome(head):
    if not head or not head.next:
        return True
    
    slow = head
    fast = head
    while fast and fast.next:
        slow  = slow.next
        fast = fast.next.next
        
    per = None
    curr = slow
    while curr:
        next = curr.next
        curr.next = per
        pre = curr
        curr = next
        
        
    left = head
    right = pre
    while  right :
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
        
    return True


# In[99]:


head1 = ListNode('R')
head1.next = ListNode('A')
head1.next.next = ListNode('D')
head1.next.next.next = ListNode('A')
head1.next.next.next.next = ListNode('R')

print(palindrome(head1))  


# In[100]:


head2 = ListNode('c')
head2.next = ListNode('o')
head2.next.next = ListNode('D')
head2.next.next.next = ListNode('E')

print(palindrome(head2))


# In[102]:


#Answer 5.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
def rLoop(head):
    if head is None or head.next is None:
        return
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if slow != fast:
        return
    
    slow = head
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next
        
    fast.next = None
    


# In[110]:


head = Node(1)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = head.next

rLoop(head)

temp = head
while temp:
    print(temp.val, end = " ")
    temp = temp.next


# In[111]:


head = Node(1)
head.next = Node(8)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = head.next

rLoop(head)
print(head.val)


# In[113]:


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = head

rLoop(head)
print(head.val)


# In[116]:


#Answer 6.


def SkipDelete(head, m, n):
    if m == 0:
        return None
    
    curr = head
    while curr:
        for _ in range(m-1):
            if curr is None:
                return head
            curr = curr.next
            
        if curr is None:
            return head
        
        next = curr.next
        for _ in range(n):
            if next is None:
                break
            next = next.next
            
    return head


# In[117]:


def LinkedList(head):
    curr = head
    while curr:
        print(curr.val, end= " ")
        curr = curr.next
    print()


# In[120]:


head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(5)
head1.next.next.next.next.next = Node(6)
head1.next.next.next.next.next.next = Node(7)
head1.next.next.next.next.next.next.next = Node(8)

M1 = 2
N1 = 2

print("Linked List:")
LinkedList(head1)

new_head1 = SkipDelete(head1, M1, N1)

print("{M1},{N1}")
LinkedList(new_head1)


# In[124]:


head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(5)
head1.next.next.next.next.next = Node(6)
head1.next.next.next.next.next.next = Node(7)
head1.next.next.next.next.next.next.next = Node(8)

M1 = 2
N1 = 2

print("Linked List:")
LinkedList(head1)

new_head1 = SkipDelete(head1 , M1, N1)
print("{M1}{N1}")
LinkedList(new_head1)


# In[ ]:


head3 = Node(1)
head3.next = Node(2)
head3.next.next = Node(3)
head3.next.next.next = Node(4)
head3.next.next.next.next = Node(5)
head3.next.next.next.next.next = Node(6)
head3.next.next.next.next.next.next = Node(7)
head3.next.next.next.next.next.next.next = Node(8)
head3.next.next.next.next.next.next.next.next = Node(9)
head3.next.next.next.next.next.next.next.next.next = Node(10)

M3 = 1
N3 = 1

print("Linked List:")
LinkedList(head3)

new_head3 = SkipDelete(head3, M3, N3)

print("{M3},{N3}")
LinkedList(new_head3)


# In[ ]:


#Answer 7.

def Merge(first, Second):
    if first is None:
        return second
    if second in None:
        return first
    
    firsts = first
    seconds = second
    
    while firsts and seconds:
        first_next = firsts.next
        second_next = seconds.next
        
        firsts.next = seconds
        seconds.next = seconds
    
    second = seconds
    
    return first


# In[ ]:


def LinkedList(head):
    curr = head
    while curr:
        print(curr.val, end= " ")
        curr = curr.next
    print()
    
    
first = Node(5)
first.next = Node(7)
first.next.next = Node(17)
first.next.next.next = Node(13)
first.next.next.next.next = Node(11)

second = Node(12)
second.next = Node(10)
second.next.next = Node(2)
second.next.next.next = Node(4)
second.next.next.next.next = Node(6)

print("first Linked list:")
LinkedList(first)

print("second Linked list:")
LinkedList(second)

merges = merge(first, second)

print("Linked list:")
LinkedList(merges)

print("second linked list marged:")
LinkedList(second)


# In[ ]:


#Answer 8.

def Circular(head):
    if head is None:
        return False
    
    slow = head
    fast = head.next
    
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
        
    return False


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = head
print(Circular(head)
      
      
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print(Circular(head))
      


# In[ ]:




