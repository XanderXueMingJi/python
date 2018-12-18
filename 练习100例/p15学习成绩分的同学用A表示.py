# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

num = int(input('请输入同学的分数'))
arr = [90, 60, 0]
show = ['A', 'B', 'C']
for i in arr:
    if(num >= i):
        print(show[arr.index(i)])
        # print(i)
        # print('i:',arr.index(i))
        break




