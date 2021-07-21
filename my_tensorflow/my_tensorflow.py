# -*- coding: UTF-8 -*-
import tensorflow as tf

# 当直接运行包含main函数的程序时，main函数才会被执行
def main():
    print("你好!我是一个TensorFlow示例...")
if __name__ == '__main__':
    main()    

# 定义一个随机数（标量）
random_float = tf.random.uniform(shape=())

# 定义一个有2个元素的零向量
zero_vector = tf.zeros(shape=(2))

# 定义两个2×2的常量矩阵
A = tf.constant([[1., 2.], [3., 4.]])
B = tf.constant([[5., 6.], [7., 8.]])

# 查看矩阵A的形状、类型和值
print("A.shape:", A.shape)      # 输出(2, 2)，即矩阵的长和宽均为2
print("A.dtype:", A.dtype)      # 输出<dtype: 'float32'>
print("A.numpy:", A.numpy())    # 输出[[1. 2.]#[3. 4.]]

C = tf.add(A, B)    # 计算矩阵A和B的和
D = tf.matmul(A, B)  # 计算矩阵A和B的乘积
print("C:", C)
print("D:", D)
