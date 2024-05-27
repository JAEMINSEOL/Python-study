#%%
weather = input('Weather?:')
if weather == 'rain':
    print('prepare umb.')
elif weather == 'dust':
    print('prepare mask')
else:
    print('go out w/o anything')



# %%
temp = int(input('temperature?: '))

if 30<=temp:
    print('too hot')
elif 10<=temp & temp<30:
    print('fine')
elif 0<=temp < 10:
    print('prepare coat')
else:
    print('too cold')
# %%
