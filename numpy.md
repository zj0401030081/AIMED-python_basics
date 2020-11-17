# 数据科学必备-numpy


## 前面的总结

我们前面已经学过了python 的基础知识，完成了实验楼的挑战，但总觉得python还有点东西没学完。我觉得还缺点什么，我觉得基础语法还应该再了解一下这两个内容，当然只了解一下皮毛就行，基本的概念，比如如何定义一个函数，传递参数；列表的基本操作等。然后我们实际操作中再去强化即可。

- python  列表 http://c.biancheng.net/python/list_tuple_dict/
- python  函数 http://c.biancheng.net/view/2247.html

## 以后的学习计划

我们可以基本按照AI MOOC这个网站的方式
https://mooc.ai-xlab.com
1. python基础 包含 ```numpy pandas matplotlib```

2. 机器学习基础（主要是常见[机器学习算法](https://www.jianshu.com/p/ac66b2d6400c)，大部分我们会以后以实战方式一一实现）
   - 线性回归算法 Linear Regression
   - 支持向量机算法 (Support Vector Machine,SVM)
   - 最近邻居/k-近邻算法 (K-Nearest Neighbors,KNN)
   - 逻辑回归算法 Logistic Regression
   - 决策树算法 Decision Tree
   - k-平均算法 K-Means
   - 随机森林算法 Random Forest
   - 朴素贝叶斯算法 Naive Bayes
   - 降维算法 Dimensional Reduction
   - 梯度增强算法 Gradient Boosting
3. 深度学习（神经网络）
4. 综合实战

## jupyter notebook

接下来，我们还要不断使用这个*jupyter notebook*来完成我们的每一次任务。
之前已经介绍了如何用VS Code中整合*jupyter notebook*，大部分同学已经顺利搭建了。
那么原生的*jupyter notebook*究竟什么样？其实我们也可以不用VS Code来启动*jupyter notebook*。
打开你的命令行，输入```jupyter-notebook```，如果你已经安装了，就会顺利启动，接着新建，就能敲代码了。如果提示没有这个命令，你只需要输入
> pip install jupyter

安装好了，然后再启动```jupyter-notebook```。
你究竟如何使用*jupyter notebook*， 这个随意！

##  numpy pandas matplotlib

```numpy pandas matplotlib``` 这三个工具，是python数据科学必须掌握的。
请使用 ```pip list```命令，看看你是否安装了这3个包，如果没有安装，请先安装。

这次必须要安装numpy，如果你之前的作业完成了，你的本地numpy应该是已经安装了。如果你在*jupyter notebook* 输入 这个代码块
``` python
import numpy as np
```
没有报错的话，就是安装成功，可以用了。
对了，```import numpy as np```这个意思是啥，请你们看看 http://c.biancheng.net/view/2397.html
这一句的意思就是导入numpy模块，并重新命名为np。

## numpy

```numpy``` (Numerical Python的简称) 是 Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。它是后面pandas和matplotlib的基础，也是一切数据分析的基础。
推荐两个教程，第二个$《跟着孙兴华学习Numpy基础》$ 是我更加推荐的。

- 【机器学习基础库】Numpy数据计算从入门到实战 https://www.bilibili.com/video/BV1U7411x76j
- 《跟着孙兴华学习Numpy基础》python Numpy 教程 https://www.bilibili.com/video/BV1R64y1u7zX?p=3

这两个教程，看任意一个即可，记得，用你的*jupyter notebook*不停敲代码来体会```numpy``` 的各种

## 科赛（和鲸）Amazing
我突然找到了一个可以在线敲代码的网站，免去搭建任何环境，在线玩就行：
科赛（和鲸）https://www.kesci.com/
这将是我们未来经常光顾的网站了，我们可以在线完成基于python和R的数据分析。同时，我们还可以参加上面的挑战赛。我希望，未来有一天智能医学社可以在上面赢得奖金！
下面，不停的在上面敲代码吧。不过，里面的服务器环境，每个月只有20 h，但我觉得足够了！
[【镇站之宝】科赛优质教程&项目集锦](https://www.kesci.com/mw/project/5e72e367c59d610036225bc0)
之后的```pandas``` 和 ```matplotlib```也是在里面玩！加油！越来越有趣了！

## 最后的作业

1. 实现视频教程 https://www.bilibili.com/video/BV1U7411x76j?p=6P6
numpy实现数组中满足条件个数的计算，```请用numpy实现```
2. 考虑两个形状分别为(8,3) 和(2,2)的数组A和B. 如何在数组A中找到满足包含B中元素的行？(不考虑B中每行元素顺序)？*(提示: np.where)*
3. 提交作业
    - 将两个作业放到同一个jupyter notebook分别作为2个代码块，提交到
 https://github.com/hao203/AIMED-python_basics.git

    - 首先gitclone 将项目克隆到本地
将你的ipynb命名为 ```姓名```.ipynb   并存放在numpy文件夹，然后```commit``` ，```push```
