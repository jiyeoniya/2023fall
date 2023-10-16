# 第二周作业实验报告

## 第一题

#### 运行结果：

![](https://github.com/jiyeoniya/2023fall/blob/main/week2/resultPic2/prob1.png "")

#### 题目思路：

现有一个正整数7.拆分方法有..
- 1 + 1 + 1 + 1 + 1 + 1 + 1 = 7
- 2 + 2 + 3 = 7
- 3 + 3 + 1 = 7  ...等

现在面临的问题是怎么拆封才能让他们的乘积最大化？
 
我们目前可以知道的是，如果想要乘积最大化的条件是尽可能的避开1，因为任何数乘以1 都不会发生改变
两个数的间隔尽可能小 （比如7 拆分成2 + 5 和 3 + 4 。明显间隔小的3、4乘积最大）

举例

对于1、2、3拆分后的结果乘积总比原来的数小

对于4，因为要避开1，所以只能 拆分为2 + 2 。且 2 * 2 = 2 + 2

对于5，只能拆分成2 + 3 ，乘积为6

对于6，拆分为3 + 3 的乘积要大于 2 + 2 + 2

对于7，拆分 4 + 3 的乘积最大(2 + 2 + 3)

对于8，拆分 3 + 3 + 2 的乘积大于 4 + 4

对于9，3 + 3 + 3的乘积最大

对于10，2 + 3 + 2 + 3 的乘积大于5 + 5

通过上面的规律我们不难发现，如果想要乘积最大化，需要尽可能的多拆分3，其次是2。 不能出现1

## 第二题

#### 运行结果：

![](https://github.com/jiyeoniya/2023fall/blob/main/week2/resultPic2/prob2.png "")

#### 题目思路：

基本的python计算，指数级增长非常宏大。

## 第三题

#### 运行结果：

![](https://github.com/jiyeoniya/2023fall/blob/main/week2/resultPic2/prob3.png "")

#### 题目思路：

在第一步，人只能先带羊过去，因为羊与狼、菜均不能同时在岸上，随后延伸出来的只有在第二步带狼或带菜两种可能性，故总共有两种解决方案。

## 第四题

#### 运行结果：

![](https://github.com/jiyeoniya/2023fall/blob/main/week2/resultPic2/prob4.png "")

#### 题目思路：

基本的python计算。

## 第五题

#### 运行结果：

![](https://github.com/jiyeoniya/2023fall/blob/main/week2/resultPic2/prob5.png "")

#### 题目思路：

基本的python计算，参考教科书第61页的内容。

## 第六题

#### 运行结果：

![](https://github.com/jiyeoniya/2023fall/blob/main/week2/resultPic2/prob6.png "")

#### 题目思路：

基本的python计算，参考教科书第64页的内容。

## 第七题

#### 运行结果：

![](https://github.com/jiyeoniya/2023fall/blob/main/week2/resultPic2/prob7.png "")

#### 题目思路：

基本的python计算，参考教科书第65页的内容。

## 第八题

#### 运行结果：

![](https://github.com/jiyeoniya/2023fall/blob/main/week2/resultPic2/prob8.png "")

#### 题目思路：

基本的python计算，参考教科书第56-59页的内容。

## 第九题

#### 运行结果：

![](https://github.com/jiyeoniya/2023fall/blob/main/week2/resultPic2/prob9.png "")

#### 题目思路：

运用python的计算，参考教科书第65页的内容。
