n = input('so luong phan tu: ')
a = []
tong = 0
for i in range(0,n):
	a.append(input('a[%d] = ' %i))
print'cac phan tu vua nhap'
print a
for i in range(0,n):
	if(a[i] % 2 == 0):
		tong = tong + a[i]
print 'tong cac phan tu chan : ',tong
def sapxep(a):
	a.sort()
	print a

print 'ham sau sap xep',sapxep(a)



	
	
