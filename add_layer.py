# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:25:12 2019

@author: DarrenSu
"""

import tensorflow as tf

def add_layer(inputs,in_size,out_size,activation_function=None):
    
    with tf.name_scope('layer'):
        with tf.name_scope('Weights'):
            Weights= tf.Variable(tf.random_normal([in_size,out_size]),name= 'W')
            tf.summary.histogram(' ',Weights)
        with tf.name_scope('biases'):    
            biases= tf.Variable(tf.zeros([1,out_size])+0.1)
            tf.summary.histogram(' ',biases)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b= tf.matmul(inputs,Weights)+biases
            tf.summary.histogram(' ',Wx_plus_b)
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)          
            tf.summary.histogram('outputs',outputs)           
        return outputs

