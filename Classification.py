# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 13:20:35 2019

@author: DarrenSu
"""
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist=input_data.read_data_sets('MNIST_data',one_hot=True)

# =============================================================================
# setting  Conv/NN layer     Weight and Bias value
# =============================================================================
initi_w_b_conv_1= 64
initi_w_b_conv_2= 80
initi_w_b_NN= 1024
# =============================================================================
# test function 
# 
# :input test data (v_xs= image, v_ys label result)
# =============================================================================
def compute_accuracy(v_xs, v_ys):
    global prediction
    #input test image to layer 
    y_pre = sess.run(prediction, feed_dict={xs: v_xs, keep_prob: 1})
    #tf.argmax is to return largest value of the array
    #tf.equal(array1,array2) is compare array1 and array2 value, if value equal return true 
    correct_prediction = tf.equal(tf.argmax(y_pre,1), tf.argmax(v_ys,1))
    #Calculation of recognition rate
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys, keep_prob: 1})
    return result
# =============================================================================
# CNN initial value setting
# =============================================================================
def weight_variable(shape):
    inital= tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(inital)
def bias_variable(shape):
    inital= tf.constant(0.1,shape=shape)
    return tf.Variable(inital)
def conv2d(x,W):
    #strides[1, x_movement, y_movement, 1]
    return tf.nn.conv2d(x,W,strides= [1,1,1,1], padding='SAME')
def max_pool_2x2(x):
    #strides[1, x_movement, y_movement, 1]
    return tf.nn.max_pool(x, ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')


# =============================================================================
# initial input image DATA 
# =============================================================================
#define placeholder to input data 28*28=784
xs= tf.placeholder(tf.float32,[None,784])

#define placeholder to output data 
ys= tf.placeholder(tf.float32,[None,10])

keep_prob= tf.placeholder(tf.float32)

x_image=tf.reshape(xs,[-1,28,28,1])

# =============================================================================
# conv1 layer  
# =============================================================================
W_conv1= weight_variable([5,5,1,initi_w_b_conv_1])#patch 5*5,in size 1, out size 32
b_conv1= bias_variable([initi_w_b_conv_1])

h_conv1= tf.nn.relu(conv2d(x_image,W_conv1)+b_conv1) #output size 28*28*32
h_pool= max_pool_2x2(h_conv1)#output 14*14*32

# =============================================================================
# conv2 layer  
# =============================================================================
W_conv2= weight_variable([5,5,initi_w_b_conv_1,initi_w_b_conv_2])#patch 5*5,in size 32, out size 64
b_conv2= bias_variable([initi_w_b_conv_2])

h_conv2= tf.nn.relu(conv2d(h_pool,W_conv2)+b_conv2) #output size 14*14*64
h_pool2= max_pool_2x2(h_conv2)#output 7*7*64

# =============================================================================
#  func1 layer
# =============================================================================
W_fc1= weight_variable([7*7*initi_w_b_conv_2,initi_w_b_NN])#7*7*64= input data ,1024=output data
b_fc1= bias_variable([initi_w_b_NN])
#[n_samples,7,7,64] ->> [n_samples, 7*7*64]
h_pool2_flat= tf.reshape(h_pool2, [-1,7*7*initi_w_b_conv_2])
h_fc1= tf.nn.relu(tf.matmul(h_pool2_flat,W_fc1)+b_fc1)
h_fc1_drop= tf.nn.dropout(h_fc1, keep_prob)
# =============================================================================
#  func2 layer
# =============================================================================
W_fc2= weight_variable([initi_w_b_NN,10])#1024= input data ,10=output data
b_fc2= bias_variable([10])
#[n_samples,7,7,64] ->> [n_samples, 7*7*64]
prediction= tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2)+ b_fc2 )

# =============================================================================
# #use Cross entropy loss method
# =============================================================================
cross_entropy= tf.reduce_mean(-tf.reduce_sum(ys* tf.log(prediction),
                                             reduction_indices=[1]))

train_step=tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

sess=tf.Session()
sess.run(tf.global_variables_initializer())   
for i in range(1000):

    #include train data from mnist
    batch_xs,batch_ys= mnist.train.next_batch(100)
    sess.run(train_step,feed_dict={xs:batch_xs,ys:batch_ys, keep_prob: 0.5})

#   Learning efficiency
    if i %50==0:
        print("Train round :",i)
#        print(compute_accuracy(
#            mnist.test.images[:1000], mnist.test.labels[:1000]))
print("Train complete")
while True:
    leave=input('Enter "q" to leave =')
    if leave=='q':
        break
    #include test data 
    print(compute_accuracy(mnist.test.images[:1000], mnist.test.labels[:1000]))
