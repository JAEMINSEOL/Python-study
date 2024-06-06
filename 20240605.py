#%%
import theater_module as th

th.price(3)
th.price_morning(5)

from theater_module import *
price_soldier(3)

from theater_module import price, price_morning
price(5)

from theater_module import price_morning as morning
morning(44)
# %%
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
# %%
from travel.vietnam import VietnamPackage as trip_to
trip_to.detail(1)

#%%
from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()