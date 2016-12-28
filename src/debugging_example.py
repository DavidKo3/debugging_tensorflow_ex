    
#-*- coding: utf-8 -*-

# 예제1: 1 부터 3 까지 증가
# 예제2: 구구단

import tensorflow as tf

def one2three_1():
    state = tf.Variable(1)
    one = tf.constant(1)
    
    with tf.Session() as sess:
        sess.run(tf.initalize_all_variables())
        
        for _ in range(3):
            print(sess.run(state))
            state = tf.add(state, one)
            
            
def one2_three_2():
    state = tf.Variable(0)
    one = tf.constrant(1)
    value = tf.add(state, one)
    update = tf.assign(state, value)
    
    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())
        
        for _ in range(3):
            print(sess.run(update))


def table99_1(which):
    level = tf.constant(which)
    state = tf.Variable(1)
    
    with tf.Session() as sess:
        sess.run(tf.initialize_all_variable())
        
        for i in range(1, 10):
            left, rite = sess.run(level), sess.run(state)
            state = tf.add(state, 1)
            
            print('{} X {} = {:2}'.format(left, rite, left*rite))
    
def table99_2(which):
    # update 를 처리하면 연계된 모든 Tensor 객체도 함께 처리 됨
    print("Sdf")    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    