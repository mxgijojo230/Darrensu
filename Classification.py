# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 13:20:35 2019

@author: DarrenSu
"""
import tensorflow as tf
from add_layer import add_layer as al 
from tensorflow.examples.tutorials.mnist import input_data
mnist=input_data.read_data_sets('MNIST_data',one_hot=True)

#test function 
#input test data (v_xs= image, v_ys label result)
def compute_accuracy(v_xs, v_ys):
    global prediction
    #input test image to layer 
    y_pre = sess.run(prediction, feed_dict={xs: v_xs})
    #tf.argmax is to return largest value of the array
    #tf.equal(array1,array2) is compare array1 and array2 value, if value equal return true 
    correct_prediction = tf.equal(tf.argmax(y_pre,1), tf.argmax(v_ys,1))
    #Calculation of recognition rate
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
    return result

#define placeholder to input data 28*28=784
xs= tf.placeholder(tf.float32,[None,784])

#define placeholder to output data 
ys= tf.placeholder(tf.float32,[None,10])

#activation_function= softmax (for classification )
prediction= al(xs,784,10,activation_function= tf.nn.softmax)

#use Cross entropy loss method
cross_entropy= tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),
                                             reduction_indices=[1]))
train_step=tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess=tf.Session()
sess.run(tf.global_variables_initializer())   
for i in range(1000):

    batch_xs,batch_ys= mnist.train.next_batch(100)
    sess.run(train_step,feed_dict={xs:batch_xs,ys:batch_ys})

#   Learning efficiency
#    if i %50==0:
#        print(compute_accuracy(mnist.test.images,mnist.test.labels))

while True:
    leave=input('Enter "q" to leave =')
    if leave=='q':
        break
    print(compute_accuracy(mnist.test.images,mnist.test.labels))
            