#!/usr/bin/env python
# coding: utf-8

# In[2]:


str(3.14)


# In[8]:


my_list1 = [10,10.1,'python',True]
my_list1


# In[10]:


type(my_list1)


# In[13]:


my_list1 = list([1,2,3])
my_list1


# In[15]:


my_tuple1=(10,10,1,'python',True)
my_tuple1


# In[17]:


type(my_tuple1)


# In[20]:


my_tuple1 = tuple([1,2,3])
my_tuple1


# In[22]:


my_list1[0]


# In[24]:


my_list1[-1]


# In[26]:


my_tuple1[0]


# In[28]:


my_tuple1[-2]


# In[31]:


my_tuple1[2]


# In[34]:


vip_names=['Newton','Euler','Gauss']
vip_names[0]


# In[36]:


vip_names[0] = 'Kepler'
vip_names


# In[38]:


vip_names = ('Newton','Euler','Gauss')
vip_names[0]


# In[39]:


vip_names[0] = 'Kepler'


# In[40]:


my_list1 = [10,20,30,40,50]
my_list1


# In[42]:


my_list1[0]


# my_list1[:]

# In[43]:


my_list1[:]


# In[44]:


my_list1[0:4:1]


# In[45]:


my_list1[1:4:2]


# In[46]:


my_list1[0:5]


# In[50]:


my_list1[2:-1]


# In[51]:


my_list1[-1::-1]


# In[52]:


my_list1[-1:2:-1]


# In[54]:


my_list2 = [[1,2,3,4,5],[20]]
my_list2


# In[55]:


my_list3=[[1,2,3],[4,5,6]]
my_list3


# In[56]:


my_list4 = [[1,2,3],
           [4,5,6]]
my_list4


# In[57]:


my_list4[0]


# In[61]:


my_list4[0][-1::-1]


# In[62]:


my_list4[1][2]


# 

# In[63]:


my_list5 = [[1,2,[100,200,300]],[4,5,6]]
my_list5


# In[64]:


my_list5[0][2][0::2]


# In[65]:


my_list1


# In[66]:


my_list2 = [100,200,300]


# In[67]:


my_list1+my_list2


# In[70]:


my_list1=[[10,20],[30,40]]
my_list2 = [50,60]


# In[71]:


my_list1+my_list2


# In[72]:


my_list1-my_list2


# In[73]:


my_list1*2


# In[74]:


my_list1*my_list2


# In[82]:


old_list = [20,30,40,50]
new_list = old_list
old_list[0] = 100
new_list


# 

# In[83]:


new_list[3] = 500
old_list


# In[84]:


new_list = old_list.copy()
old_list[2]=300
new_list


# In[87]:


num_list1 = [1,2,3]
num_list2 = [4,5,6]
num_list1.extend(num_list2)
num_list1


# In[89]:


num_list1 += num_list2
num_list1


# In[90]:


vip_names


# In[91]:


vip_names = list(vip_names)


# In[92]:


vip_names


# In[93]:


vip_names.append('Kepler')


# In[94]:


vip_names


# In[95]:


vip_names.remove('Gauss')
vip_names


# In[96]:


vip_names.pop(0)
vip_names


# In[98]:


vip_names.clear()
vip_names


# In[99]:


vip_names.insert(0,'Newton')
vip_names


# In[100]:


vip_names[0]= 'Euler'


# In[101]:


vip_names.insert(40,'Gauss')
vip_names


# In[102]:


vip_names.index('Euler')


# In[103]:


vip_names.count('Gauss')


# In[104]:


vip_names.count('Newton')


# In[105]:


vip_names.insert(1,'Newton')
vip_names


# In[106]:


vip_names.sort()


# In[107]:


vip_names


# In[109]:


numberalpha = [3,4,'d','f',True,'Euler']
numberalpha.sort()
numberalpha


# In[112]:


mixed = [0,-1,False,5,1,True]
mixed.sort()
mixed


# In[113]:


vip_names.reverse()


# In[114]:


vip_names


# In[115]:


data = [['Asia',24],['Europe',25],['Africa',34]]
data.sort()
data


# In[116]:


my_set1 = {1,20,30}
my_set2 = {10,'Lychee',True}


# In[117]:


my_set1


# In[118]:


my_set1[0]


# In[119]:


my_set3 = {10,20,30,40,20,30}
my_set3


# In[123]:


my_set4 = set(vip_names)


# In[124]:


my_set4


# In[126]:


my_set3.add(40)
my_set3


# In[127]:


my_set3.update([30,50])
my_set3


# In[129]:


my_set3.discard(30)
my_set3


# 

# In[130]:


my_set3.remove(30)


# In[132]:


my_set3.discard(30)
my_set3


# In[133]:


my_set3 | my_set4


# In[134]:


my_set5 = {10,20,50,60,70}
my_set3.union(my_set5)


# In[135]:


my_set3 & my_set5


# In[136]:


my_set3 - my_set5


# In[137]:


my_set3.difference(my_set5)


# In[138]:


my_set3^my_set5


# In[139]:


my_set3.symmetric_difference(my_set5)


# In[141]:


m = {40}
m.issubset(my_set3)


# In[142]:


my_set3.issuperset(m)


# In[143]:


A = frozenset([10,20,30,40,50])
B = frozenset([0,40,50,30,80])
A


# In[144]:


A | B


# In[145]:


A & my_set3


# In[146]:


vip_names


# In[147]:


'Newton' in vip_names


# In[148]:


All = set(vip_names)
D1 = set(['Newton'])
D2 = set(['Euler','Gauss'])
D3 = set(['Newton','Jaemin'])
D1.issubset(All)


# In[149]:


All - D1 & D2


# In[151]:


All - (D1 | D2)


# In[152]:


D3.issubset(All)


# In[153]:


my_list4[0:2][0]


# In[154]:


my_list4[0:1][0]


# In[ ]:




