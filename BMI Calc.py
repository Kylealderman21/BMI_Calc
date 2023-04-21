#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator

# In[43]:


import click 

name = input('Enter your name:')

weight = click.prompt('Enter your weight in lbs', type=float)

height = click.prompt('Enter your height in inches', type=float)
    
BMI = (weight * 703) / (height * height)
print('Your BMI is:', BMI)

if BMI > 0:
    if(BMI < 18.5):
        print(name +", you are underweight.")
    elif(BMI <= 24.9):
        print(name +", you are normal weight.")
    elif(BMI <=29.9):
        print(name +", you are overweight.")
    elif(BMI <=34.9):
        print(name +", you are obese.")
    elif(BMI <=39.9):
        print(name +", you are morbidly obese.")
else: 
    print('Enter valid inputs')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




