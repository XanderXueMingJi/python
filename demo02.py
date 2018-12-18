import os

# 文件I/O

# str = input() #读取键盘输入

# print(str)

# 打开和关闭文件

# fo = open("demo02.txt", "w")  #写
fo = open("demo02.txt", "r+")  # 读

print(fo)

# fo.write('''
# We only have to combine these ancient science fiction movies to understand.

# How the themes of paleontology become popular

# If the leaders of the science fiction films on the space subject are likely
# to be "Star Wars" and "Star Trek" series, the paleontological science fiction
# films have only the top of the Jurassic Park and the Jurassic world series.

# Since the release of the first Jurassic Park in 1993, the 4 Jurassic Park
# films have met the "resurrection of dinosaurs" by dinosaurs all over the
#  world, and have deeply affected the real life. Even a dinosaur - era parcel
#  of amber with insects, or a fossil dinosaur egg with an unidentified paste
#  inside, could lead to the popularity of the media, because it was believed
#  that it could be the "key" for the dinosaurs to come back to the earth.

# In 1985, the United States proposed the "human genome project". After
#  mastering nuclear technology and space flight and landing alien stars,
# the United States began to use the most advanced biological and chemical
# results at that time, trying to draw out.
#  ''')

str = fo.read(50)

print('读取的字符串是:', str)

# 查找当前位置
position = fo.tell()

print('当前文件(指针)位置:', position)

# 把指针再次重新定位到文件开头
position = fo.seek(0, 0)
str = fo.read(10)
print('重新读取字符串:', str)

# 重命名和删除文件 需要导入os模块

# text8.text 要预先创建好

# os.rename("text8.text", "text5.text") #重命名

# os.remove("text5.text") #删除

# 目录

# os.mkdir('demo') #创建目录

# chdir()方法     可以用chdir()方法来改变当前的目录。chdir()方法需要的一个参数是你想设成当前目录的目录名称。  我先不做!!!

print(os.getcwd())  # 显示当前的工作目录地址。  C:\Users\Administrator\Desktop\python

# rmdir()方法  删除目录，目录名称以参数传递。 我先不做!!!

# 关闭打开的文件
fo.close()
