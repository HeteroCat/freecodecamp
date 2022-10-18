"""
     ／|、
  （ﾟ､ 。７
   |、~ヽ
   じしf_,)ノ
作者：Administrator
时间：2022年10月18日
"""
import numpy as np
try:
    a=eval(input("请输入9位数字的列表："))
    while len(a)!=9:
        print("输入有误,列表必须包含九个数字")
        a=eval(input("请输入9位数字的列表："))
except NameError:
    print("输入有误,列表必须包含九个数字")
    a=eval(input("请输入9位数字的列表："))
    while len(a)!=9:
        print("输入有误,列表必须包含九个数字")
        a=eval(input("请输入9位数字的列表："))

c=np.array(a).reshape(3,3)

dict={
    print('mean:',np.mean(c,axis=0),np.mean(c,axis=1),np.mean(c)),
    print('variance:',np.var(c,axis=0),np.var(c,axis=1),np.var(c)),
    print('standard deviation:',np.std(c,axis=0),np.std(c,axis=1),np.std(c)),
    print('max:',np.max(c,axis=0),np.max(c,axis=1),np.max(c)),
    print('min:',np.min(c,axis=0),np.min(c,axis=1),np.min(c)),
    print('sum:',np.sum(c,axis=0),np.sum(c,axis=1),np.sum(c))
}

dict

