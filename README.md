# Matrix-Calculator
一个自用的简单的矩阵计算器。



### 前言

这是一个非常简单的矩阵计算器，它目前仅支持以下功能：

* 矩阵的简单运算
* 求行列式的值
* 求向量组的秩和它的极大线性无关组
* 求解线性方程组

并且它很辣鸡地只支持有理数域上的计算。

~~功能也许会随着我的高代学习进度增加~~

目前还处于0.0.1.beta版，无法保证所有功能都能正常使用，也无法保证在非法操作时能输出恰当的错误信息。

请不要试图卡bug！这个程序想要正常运行就已经用尽全力了！

### 用法

#### 展示已有矩阵内容

使用

```
：show name
```

来展示已有矩阵。

#### 手动输入矩阵

使用 

```
:read name
```

来手动输入一个矩阵，并在输入结束后以end作为结束符。

#### 求行列式的值

若a是一个行列式，使用

```
:value a
```

可以求该行列式的值;

##### Demo:

![value](https://github.com/TyrionZ/Matrix-Calculator/blob/master/DemoPics/value.png)

#### 求向量组的秩和极大线性无关组

使用

```
:rank a
```

可以求出a的秩和它的行向量组的一个极大线性无关组。

##### Demo:

![rank](https://github.com/TyrionZ/Matrix-Calculator/blob/master/DemoPics/rank.png)



#### 求解线性方程组

使用

```
:solve a
```

可以求出以增广矩阵为a的线性方程组的通解。

![solve](https://github.com/TyrionZ/Matrix-Calculator/blob/master/DemoPics/solve.png)

##### Demo:

#### 矩阵的简单运算

使用

```
c = a + b
c = a - b
c = a * b
```

实现矩阵的加减法和乘法。

使用

```
c = a / b
```

将两个矩阵左右拼接。

使用

```
c = a % b
```

将两个矩阵上下拼接。

使用

```
c = a -t
```

求a的转置。

使用

```
c = a -g
```

求使用简单行变换将a消成上阶梯形矩阵的结果。

##### Demo:

![+1](https://github.com/TyrionZ/Matrix-Calculator/blob/master/DemoPics/+1.png)

接上图

![+2](https://github.com/TyrionZ/Matrix-Calculator/blob/master/DemoPics/rank.png)



