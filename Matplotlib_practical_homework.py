#!/usr/bin/env python
# coding: utf-8

# ### P1. Write a Python code to output the following graphs. (or similar ones). 

# ![Screen%20Shot%202019-01-05%20at%2010.56.36%20AM.png](attachment:Screen%20Shot%202019-01-05%20at%2010.56.36%20AM.png)

# In[12]:


import matplotlib.pyplot as plt
x = [0,50]
y = [0,156]
plt.plot(x, y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("Draw a line")


# ![Screen%20Shot%202019-01-05%20at%2010.58.22%20AM.png](attachment:Screen%20Shot%202019-01-05%20at%2010.58.22%20AM.png)

# In[14]:


x = [1,2,3]
y = [2,4,1]
plt.plot(x, y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("Sample graph!")


# ![Screen%20Shot%202019-01-05%20at%2011.05.37%20AM.png](attachment:Screen%20Shot%202019-01-05%20at%2011.05.37%20AM.png)

# In[21]:


x1 = [10,20,30]
y1 = [20,40,10]

x2=[10,20,30]
y2=[40,10,30]
plt.plot(x1, y1, label = "line 1 width-3", linewidth=3, color='b')
plt.plot(x2, y2, label = "line 2 width-5", linewidth=5, color='r')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("Two or more lines with different widths and colors with suitable legends")
plt.legend()


# ![Screen%20Shot%202019-01-05%20at%2011.04.00%20AM.png](attachment:Screen%20Shot%202019-01-05%20at%2011.04.00%20AM.png)

# In[24]:


plt.plot(x1, y1, label = "line 1- dotted", linestyle='dotted',linewidth=3, color='b')
plt.plot(x2, y2, label = "line 2- dashed", linestyle='dashed', linewidth=5, color='r')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("Plot with two or more lines with different styles")
plt.legend()


# ![Screen%20Shot%202019-01-05%20at%2011.07.01%20AM.png](attachment:Screen%20Shot%202019-01-05%20at%2011.07.01%20AM.png)

# In[37]:


x = [1,4,5,6,7]
y = [2,6,3,6,3]
plt.plot(x, y, linestyle='dashdot',color='r')
plt.scatter(x,y, color='b', s=100)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("Display marker")


# ### P2. Create a file with the following content: 

# ```
# test.txt
# 1 2
# 2 4
# 3 1
# ```

# ### Create the following graph using the data from the file.

# ![Screen%20Shot%202019-01-05%20at%2011.09.40%20AM.png](attachment:Screen%20Shot%202019-01-05%20at%2011.09.40%20AM.png)

# In[56]:


import pandas as pd
d = pd.read_csv('test.txt', header=None, delimiter=' ')
d.columns=['x-axis', 'y-axis']
d


# In[64]:


plt.plot(d['x-axis'], d['y-axis'])
plt.title("Sample graph!")


# ### P3. Get the following graph given:

# ```
# x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
# popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
# ```

# ![image.png](attachment:image.png)

# In[77]:


x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.bar(x, popularity, color='b')
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title("Popularity og Programming Language  \n  Oct 2017")


# #### Make modifications to get the following graph instead

# ![image.png](attachment:image.png)

# In[84]:


x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors=['r', 'k','g','b','yellow','c']
plt.bar(x, popularity, color=colors)


# ### P4. Create the following pie chart.

# ![image.png](attachment:image.png)

# In[116]:


slices=[31.3,24.8,12.4,11.3,10.8,9.4]
languages=['java','Python','PHP','JavaScript','C#','C++']
colors=['b','orange','g','r','m','brown']
plt.pie(slices, labels = languages, colors = colors, startangle = 135, shadow = True, explode = (0.1, 0, 0, 0,0,0), autopct = "%1.1f%%")


# ### P5. Write a Python program to draw a scatter graph taking a random distribution in X and Y and plotted against each other. You should get something like this.

# ![image.png](attachment:image.png)

# In[7]:


help(np.random)


# In[117]:


import numpy as np
import matplotlib.pyplot as plt
x = np.random.randn(150)
y = np.random.randn(150)
plt.scatter(x, y, color='r')
plt.show()


# ### P6. Write a Python code to output the following graph. (or a similar one). 
# ```
# The productivity values for the 3 groups are the following: 
# 
# g1 = [80, 60, 80, 67, 34]
# g2 = [45, 67, 23, 89, 10]
# g3 = [30, 90, 50, 20, 90]
# ```

# ![image.png](attachment:image.png)

# In[174]:


g1 = [80, 60, 80, 67, 34]
g2 = [45, 67, 23, 89, 10]
g3 = [30, 90, 50, 20, 90]
import numpy as np
from pandas import DataFrame
groups=['Group 1','Group 2','Group 3']
wkdays=['M', 'T', 'W', 'Th', 'F']

df=DataFrame(np.array([g1,g2,g3]).T, columns=groups, index=wkdays)
print(df)
df.plot(kind='bar', rot=0)
plt.title('Productivity during the week')
plt.xlabel('Groups')
plt.ylabel('Productivity')


# ### P7. Write a Python code to output the following graph. (or a similar one)
# ```
# Draw 25 dots. Generate random x and y coordinates (integers from 1 to 30), random colors and random sizes (integers from 20 to 500) for the dots.
# ```
# 
# ```
# Նկարեք 25 կետեր. Կետերի համար գեներացրեք պատահական x և y կոորդինատներ (1-ից 30 միջակայքում int տիպի թվեր), պատահական գույներ ու պատահական չափսեր (20-ից 500 միջակայքում int տիպի թվեր)։
# ```

# ![image.png](attachment:image.png)

# In[208]:


x=np.random.randint(1,30,(1,25))
y=np.random.randint(1,30,(1,25))
r = np.random.rand()

color = (r, g, b)
plt.scatter(x,y, c=np.random.rand(1,25), s=np.random.randint(20,500,(1,25)))


# In[209]:


np.random.randint(1,30,(1,25))


# ### P8. Plotly

# ```
# Load the Iris dataset from plotly.express. 
# ```

# In[1]:


get_ipython().system('pip install plotly ')


# In[2]:


import plotly.express as px
import pandas as pd
df = px.data.iris()
df


# ```
# Create a scatter plot of petal_length vs petal_width. Use species as the color and display all the feature values when you hover over a point.
# ```

# In[3]:


fig = px.scatter(df, x="petal_length", y="petal_width", color="species", hover_data=['sepal_width','sepal_length',])
fig.show()


# ```
# Create a histogram having 20 bins using the feature sepal_length. Use species feature as the color. 
# ```

# In[11]:


fig = px.histogram(df, x="sepal_length", color="species", nbins=20)
fig.show()


# ```
# Plot sepal_length and sepal_width features on the same histogram. 
# ```

# In[22]:


fig = px.histogram(df, x=["sepal_length","sepal_width"])
fig.show()


# ```
# Create a heatmap showing the correlation of the columns sepal_width and petal_width.
# ```

# In[62]:


a=df[['sepal_width', 'petal_width']]
fig=px.imshow(a.corr())
fig.show()


# ```
# Create a box plot showing the distribution of the sepal_length feature. 
# ```

# In[63]:


fig = px.box(df, x="sepal_length")
fig.show()


# ```
# (Optional) Did you find any interesting insights regarding the Iris dataset while doing this last exercise? 
# ```

# In[ ]:




