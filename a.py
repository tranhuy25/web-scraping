
# biến một hàm thành method trong class
# class Kter:                 
#     def __init__(self, ho, ten):
#         self.ho = ho
#         self.ten = ten

#     @property
#     def ho_va_ten(self):
#         return '{} {}'.format(self.ho, self.ten)

#     @property
#     def email(self):
#         return self.ho + '_' + self.ten + '@kteam.com'
    
# Kter_A = Kter("tran", "Long Dep Trai")

# print(Kter_A.ho)
# print(Kter_A.ten)
# print(Kter_A.email)
# print(Kter_A.ho_va_ten)

# Kter_A.ho = "Nguyen"
# Kter_A.ten = "van A"

# print(Kter_A.ho)
# print(Kter_A.ten)
# print(Kter_A.email)
# print(Kter_A.ho_va_ten)

#---------------------------------------------------------------------------

# from matplotlib import pyplot as plt 

# # x-axis values 
# x = [5, 2, 9, 4, 7] 

# # Y-axis values 
# y = [10, 5, 8, 4, 2] 

# plt.scatter(x, y) 
# # Function to plot 

# plt.plot(x, y) 

# # function to show the plot 

# plt.show()

#---------------------------------------------------------------------------
def change(n):
    n*=2
a=1000

change(a)  # a ở đây  chỉ là tham số hình thức vì hàm trên kia không trả về gì 
print(a)

def giai_Thua(n):
    res=1 
    for i in range (1,n+1):     #range là lấy  [......)
        res*=i
    return res
print(giai_Thua(3))

#---------------------------------------------------------------------------
#số fibonacci : 0 , 1 ,1,2,3,5,8,13  Fn = Fn-1 +Fn-2
#concep : kiểm tra một số có phải là số fibo , in ra số finbo thứ n , hoặc in ra số finbo đầu tiên 
# python xử lý được số nguyên lớn hơn c hay c++ /java (0<=N<=9.10^18)

#---------------------------------------------------------------------------

import numpy as np

X0 = np.array([[2], [7], [9], [3], [10], [6], [1], [8]])
ones = np.ones_like(X0)

# Nối 2 vector/ma trận theo chiều dọc

X = np.concatenate((X0, ones), axis=1)

Y = np.array([[13], [35], [41], [19], [45], [28], [10], [55]])

print(X)
# print(Y)

# API np.linalg.inv() dùng để tính ma trận nghịch đảo

theta = np.linalg.inv(X.T.dot(X)).dot(X.T.dot(Y))

