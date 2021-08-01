#!/usr/bin/env python
# coding: utf-8

# NAME: Chembeti Munijayanth 
# Rollno:19MIM10025
# Campus: VITBHOPAL

# # Assignment - 09
# 

# In[5]:


import cv2
import sys
import numpy as np


# In[71]:


cap = cv2.VideoCapture("video.mp4")  
if (cap.isOpened()== False): 
  print("Error opening video  file")
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    frame=cv2.line(frame,(1,1),(1259,1259),(155,255,120),5)
    frame=cv2.rectangle(frame,(1,1),(200,200),(0,255,255),9)
    frame = cv2.circle(frame,(600, 300),100,(255,255,255),3)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
      break
  else: 
    break
cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




