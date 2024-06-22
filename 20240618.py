#%%
from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()

#%%
from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()

#%% 패키지나 모듈이 동일한 폴더에 있지 않은 경우
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))
# %%
