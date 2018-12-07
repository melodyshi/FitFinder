#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")
get_ipython().system('sudo pip3 install -U statsmodels')
get_ipython().system('sudo pip3 install pdfkit')
import pdfkit


# In[4]:


pdfkit.from_url('http://www.stern.nyu.edu', 'out.pdf')


# In[8]:


pdfkit.from_url('https://drive.google.com/file/d/1IdrvTC4IqJ4Wn4GIgOWWncHhSstUoTrL/view?usp=sharing', 'bwf.pdf')
pdfkit.from_url('http://www.100pushups.com/your-first-pushup/', '100p1.pdf')
pdfkit.from_url('http://www.100pushups.com/foundation-training-plan/', '100p2.pdf')
pdfkit.from_url('http://www.100pushups.com/intermediate-training-plan/', '100p3.pdf')
pdfkit.from_url('http://www.100pushups.com/advanced-training-plan/', '100p4.pdf')
pdfkit.from_url('http://www.trickstutorials.com/content/flx3.php', 'flexibility1.pdf')
pdfkit.from_url('https://phrakture.github.io/starting-stretching.html', 'flexibility2.pdf')


# In[1]:


get_ipython().system("curl -L 'https://www.dropbox.com/s/us4yj3usf76teu2/sts.pdf?dl=0' -o flexibility3.pdf")
get_ipython().system("curl -L 'http://biggerfasterstronger.com/home/Download-pdfs-2014/BFS-25-Agility-Drills.pdf' -o conditioning1.pdf")
get_ipython().system("curl -L 'http://www.biggerfasterstronger.com/uploads/Dot%20Drill%20Info.pdf' -o conditioning2.pdf")
get_ipython().system("curl -L 'http://theparkministries.org/images/pdfs/Couch-to-5k.pdf' -o c25k.pdf")
get_ipython().system("curl -L 'https://mayoclinichealthsystem.org/-/media/national-files/documents/hometown-health/foam-rolling-basics-handout.pdf?la=en&hash=3EA9036B45718C2696DAECACC1BBA2195FA5DF3E' -o foamroll.pdf")
get_ipython().system("curl -L 'https://www.changeinseconds.com/yoga-morning-routine/' -o morningyoga.pdf")
get_ipython().system("curl -L 'https://uhs.berkeley.edu/sites/default/files/wellness-resistancebandexercises.pdf' -o resistence.pdf")
get_ipython().system("curl -L 'https://mymission.lamission.edu/userdata/ruyssc/docs/Stretch-An-Ullustrated-Step-By-Step-Guide-To-Yoga-Postures.pdf' -o yoga.pdf")


# In[ ]:




