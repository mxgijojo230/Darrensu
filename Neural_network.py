# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:51:17 2019

@author: DarrenSu
"""

import numpy as np
from add_layer import add_layer as al
import tensorflow as tf

import matplotlib.pyplot as plt

#create test data
# [:,np.newaxis]為列轉換成行[300,]->[300,1]
x_data= np.linspace(-1,1,300)[:,np.newaxis]
#add noise
noise= np.random.normal(0,0.05,x_data.shape).astype(np.float32)
#y_data=np.square( np.linspace(-1,1,300)[:,np.newaxis])+noise
#np.square = arr**2
y_data=np.square(x_data)-0.5+noise

#create tf.placeholder()
with tf.name_scope('inputs'):
    xs= tf.placeholder(tf.float32,[None,1],name='x_in')
    ys= tf.placeholder(tf.float32,[None,1],name='y_in')

#plot input data
fig= plt.figure()
#add plot
ax=fig.add_subplot(1,1,1)
ax.scatter(x_data,y_data)

plt.ion()
plt.show()

#use relu activation method
l1= al(xs,1,10,activation_function=tf.nn.relu)

l2= al(l1,10,5,activation_function=tf.nn.relu)

result= al(l2,5,1,activation_function=None)


#calculate loss value
with tf.name_scope('Loss'):
    loss= tf.reduce_mean( tf.reduce_sum( tf.square(ys-result),
                                    axis= 1,name='sum'),name= 'mean')
    tf.summary.scalar('Loss',loss)
    
with tf.name_scope('Train'):
    train_step= tf.train.GradientDescentOptimizer(0.05).minimize(loss)


inti= tf.global_variables_initializer()
with tf.Session() as sess:
    writer=tf.summary.FileWriter('logs/',sess.graph)
    merged=tf.summary.merge_all()
    #merged =tf.summary.merge([lossw,lossw])
    sess.run(inti)
    for i in range(1000):
        sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
        if i %50 ==0:        
            #display histogram
            rs = sess.run(merged,feed_dict={xs:x_data,ys:y_data})
            writer.add_summary(rs, i)
            try:
                #remove frist lines if presence
                ax.lines.remove(lines[0])
            except Exception:
                pass
            #create train line
            plot_value= sess.run(result,feed_dict={xs:x_data,ys:y_data})
            lines=ax.plot(x_data,plot_value, 'r-', lw=5)
            
            #pause 0.1 sec
            plt.pause(0.1)
            




                
