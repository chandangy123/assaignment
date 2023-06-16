#!/usr/bin/env python
# coding: utf-8

# ###  1. What exactly is []?

# it exactly means a empty list i,e.. 
# gyc=[]
# which is highly used when we want to take input of list of numbers
# for example.

# In[1]:


gyc=[]
w=int(input('enter the length of list'))
for i in range(w):
    e=input('enter the numbers')
    gyc.append(e)
    
print(gyc)


# ### 2. In a list of values stored in a variable called spam, how would you assign the value &#39;hello&#39; as the
# third value? (Assume [2, 4, 6, 8, 10] are in spam.)

# In[2]:


spam=[2,4,6,8,10]
spam[2]='hello'
print(spam)


# # Let&#39;s pretend the spam includes the list [&#39;a&#39;, &#39;b&#39;, &#39;c&#39;, &#39;d&#39;] for the next three queries.
# 

# ### 3. 3. What is the value of spam[int(int(&#39;3&#39; * 2) / 11)]?

# In[3]:


spam=['a','b','c','d']


# In[4]:


spam[int('3'*2/11)]


# In[5]:


#because it treated '3' as a string and it cannot multiply string with integer 2 , therefore the correct operation is


# In[6]:


spam[int(3*2/11)]


# ### 4. What is the value of spam[-1]?

# In[7]:


spam[-1]


# ### 5. What is the value of spam[:2]?

# In[8]:


spam[:2]


# # Let&#39;s pretend bacon has the list [3.14, &#39;cat,&#39; 11, &#39;cat,&#39; True] for the next three questions.

# In[9]:


bacon=[3.14,'cat',11,'cat',True]


# ### 6. What is the value of bacon.index(&#39;cat&#39;)?

# In[10]:


bacon.index('cat')


# ### 7. How does bacon.append(99) change the look of the list value in bacon?

# In[11]:


bacon.append(99)


# In[12]:


bacon


# In[13]:


# this append function usually add the defined value at the end of the list


# ### 8. How does bacon.remove(&#39;cat&#39;) change the look of the list in bacon?

# In[14]:


bacon.remove('cat')


# In[15]:


bacon


# In[16]:


# remove function usually remove the defined value, but here we can see that the cat which is removed is of lower indexing.


# ### 9. What are the list concatenation and list replication operators?

# In[17]:


#list concatenation is used to merge two list, operator used is '+' between list
abc=[2,4,6,8,10]
mno=[1,3,5,7,9]
con_lst=abc+mno
print(con_lst)


# In[18]:


# replication means replicating the existed list with certain number of times,operator used is *, for example
xyz=[1,3,5,7,9]
repli=xyz*2
repli


# In[19]:


dc=xyz*5
dc


# ### 10. What is difference between the list methods append() and insert()?

# append() usually add the value to the end of the list and take only one argument,
# but insert() method usually insert value to the perticularly mentioned position and take two arguments

# In[20]:


# for eaxpmle:
gyc=[1,2,3,4,5,6]
gyc.append('chandan')
gyc


# In[21]:


gyc.insert(2,'prajwal')
gyc


# ### 11. What are the two methods for removing items from a list?

# remove() and pop() are the two methods used to remove the items in the list
# for example

# In[22]:


gyc.pop()


# In[23]:


#pop usually remove last element it we dont specify the index
#we can see here the removed element and remaining list is


# In[24]:


gyc


# In[25]:


gyc.pop(2)


# In[26]:


#here i specified the perticula index 2, it will removed the 2nd indexed value


# In[27]:


gyc


# In[28]:


#Now the remove used to directly specify the value which we want to remove


# In[29]:


gyc.remove(5)


# In[30]:


gyc


# In[31]:


#here we can see that, what evere value we specified that is removed


# ### 12. Describe how list values and string values are identical.

# #list and string both are the data types in python.
# #string is a part of list.
# #list may have integer, string, float values, and string having only characters.
# #list are mutable, but strings are not mutable, and individaul elements in list is immutable.
# #both list and string supports the length that indicates the number of elements that contain.
# #both support indexing and slicing

# ### 13. What&#39;s the difference between tuples and lists?

# #mutability: lists are mutable and tuples are immutable.
# #syntax used: list will be defined inside the [] and tuple is defined inside ().
# #operators: list support some methods and operators i,e. remove(), pop(), insert(), append(), indexing and slicing, 
# but tupples do not support these methods and operators.
# #memory: since the tuples are immutable, generally more memory-efficient than lists but  Lists, being mutable, require additional memory allocation to handle potential modifications.
# #time: tuple require less time and list require more time.

# ### 14. How do you type a tuple value that only contains the integer 42?

# In[32]:


tuple=(42,)


# #Without the presence of comma, Python would interpret the parentheses as regular parentheses rather than indicating a tuple.

# ### 15. How do you get a list value&#39;s tuple form? How do you get a tuple value&#39;s list form?

# In[33]:


#to convert  tuple to list we need to use the method list()
gyc=(1,2,3,4,5,6,7,8,9)


# In[34]:


tom = list(gyc)
print(tom)


# In[ ]:


#to convert list to tuple we need to use the method tuple()
my_list = [1, 2, 3]
my = tuple(my_list)

print(my)


# ### 16. Variables that &quot;contain&quot; list values are not necessarily lists themselves. Instead, what do they  contain?

# In[35]:


# variables that "contain" list values in Python actually contain references to the list objects stored in memory, 
# allowing us to work with and manipulate the lists through those variables.


# In[36]:


mno = [1, 2, 3]
another_mno = mno
another_mno.append(4)

print(mno)      
print(another_mno) 


# we can see here both are of same list, if we change variables in one list reflects changes in referenced list also.

# ### 17. How do you distinguish between copy.copy() and copy.deepcopy()?

# the functions copy() and deepcopy() are used to create copies of objects.they differ in how they handle object references and nested objects.

# copy.copy() creates a shallow copy of an elements.It creates a new object and then copies 
# the references to the nested objects of the original object. However, if the nested objects are mutable,
# any modifications made to them will affect both the original object and the copied object.
# 

# In[40]:


cat = [1, [2, 3]]
new = copy.copy(cat)

new[1].append(4)

print(cat) 
print(new)


# In[ ]:


copy.deepcopy() function creates a deep copy of an elements. It creates a completely independent copy of the object 
and all its nested objects. Modifying the nested objects in the copied object will not affect the original object


# In[41]:


dog = [1, [2, 3]]
new_dog = copy.deepcopy(dog)

new_dog[1].append(4)

print(dog) 
print(new_dog) 


# In[ ]:




