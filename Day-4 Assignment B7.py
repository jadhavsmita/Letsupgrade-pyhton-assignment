#!/usr/bin/env python
# coding: utf-8

# In[4]:


for num in range(1042000,702648265):
    order=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
    break
    if num==sum:
            print(sum)
            

