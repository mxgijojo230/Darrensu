# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:30:25 2019

@author: DarrenSu
"""
#need use tensorflow model

#import numpy as np
import tensorflow as tf
import numpy as np

#create data
x_data=np.random.rand(100).astype(np.float32)
y_data=x_data*0.1+0.3



#create model
Weights=tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases=tf.Variable(tf.zeros([1]))

y=Weights*x_data+biases


#calculate loss
loss= tf.reduce_mean(tf.square(y-y_data))


optimizer= tf.train.GradientDescentOptimizer(0.07)
train= optimizer.minimize(loss)

#initial variables
init= tf.global_variables_initializer()

sess= tf.Session()
sess.run(init)

for step in range(201):
    sess.run(train)
    if step%20 ==0:
        print(step, sess.run(Weights),sess.run(biases))