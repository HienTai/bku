#!/usr/bin/python
# -*- coding: utf8 -*-

#kiểu số nguyên (Intergers)
a=4
print(a)

#kiểu dữ liệu của a
print(type(a))

#kiểu dữ liệu
b="4 là số nguyên"
print(b)

#kiểu dữ liệu của b
print(type(b))

#kiểu số thực
c= 9.9
print(c)

#kiểu dữ liệu của c
print(type(c))

#Python chỉ xét xấp xỉ 15 chữ số thập phân sau dấu "."
#muốn lấy toàn bộ >15 cs thập phân dùng kiểu "decimal"
#Lấy toàn bộ nội dung decimal
from decimal import*

#lấy tối đa 30 cs phần nguyên và phần thập phân Decimal (phải thuộc)
getcontext().prec = 30
#hàm trên ko xài cx đc, nếu ko thì nó lấy vô số lần (mặc định 30)

print(Decimal(10)/Decimal(3))

#Nếu print(10/3) thì nó vẫn là 15 chữ số
#Bắt buộc để D in hoa

#Hàm phân số (Fraction)
from fractions import*
#f viết thường

h= Fraction(6,9)
print(h)
print(type(h))

#Kiểu số phức
#Complex(<phần thực>, <phần ảo>)
t= complex(2,5)
print(t)
print(t.real)
print(t.imag)

#Các phép toán dữ liệu số
#+ - * /
#Ngoài ra 
# // thương lấy phần nguyên
# % thương lấy phần dư
# ** luỹ thừa

#cách add thư viện nhanh hơn
# import <tên thư viện>
# <tên thư viện>.<tên hàm>