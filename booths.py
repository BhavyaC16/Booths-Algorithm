from math import pow
import sys
##########helper functions#############
def getSigned(num):  #signed representation convert number to 2s complement
	bi=binary(abs(num))
	if num==0:
		sign=''
	elif num<0:
		sign='1'
		bi=gettwos(bi)
	else:
		sign='0'
	bi=sign+bi
	return bi

def binary(x): #decimal to binary
	bi=''
	if x==0:
		bi='0'
	while(x>0):
		bi=(str(x%2))+bi
		x=x//2
	return bi

def pad(x,y):
	if len(x)<len(y):
		for i in range(len(y)-len(x)):
			x=x[0]+x
	else:
		for i in range(len(x)-len(y)):
			y=y[0]+y
	return x,y

def getDecimal(bi):    #2s complement binary to decimal 
	if len(bi)==1 and bi=='0':
		return 0
	if bi[0]=='0':
		sign=1
		bi=bi[1:]
	else:
		sign=-1
		bi=bi[1:]
		bi=gettwos(bi)
	ans=0
	for p in range(0,len(bi)):
		i=len(bi)-p-1
		ans=ans+(int(bi[i])*int(pow(2,p)))
	return sign*ans
	
def getIndex(x,i):   #helper for addition
	if i<-len(x):
		return 0
	else:
		return int(x[i])
def add(x,y):     #binary addition
	ans=''
	i=-1
	c=0
	while(i>=-len(x) or i>=-len(y)):
		if getIndex(x,i)+getIndex(y,i)+c==3:
			c=1
			ans='1'+ans
		elif getIndex(x,i)+getIndex(y,i)+c==2:
			c=1
			ans='0'+ans
		elif getIndex(x,i)+getIndex(y,i)+c==1:
			c=0
			ans='1'+ans
		else:
			c=0
			ans='0'+ans
		i-=1
	return ans
def flip(x):    #flip the bit
	if x=='1':
		return '0'
	return '1'
def gettwos(bi):  #return 2s complement (irrespective of positive and negative)
	twos=''
	for i in bi:
		twos=twos+flip(i)
	twos=add(twos,'1')
	return twos

def rightShift(a,beg):
	a=beg+a
	remove=a[-1]
	a=a[:-1]
	return (a,remove)

def leftShift(a,end):
	a=a+end
	remove=a[0]
	a=a[1:]
	return (a,remove)

#########main###########
print("Enter 2 numbers: ")
x=int(input("x: "))
y=int(input("y: "))
#if not(-1000<=x<=1000 and -1000<=y<=1000):
	#print("Input out of range")
	#sys.exit()

signedX=getSigned(x)
signedY=getSigned(y)
signedX,signedY=pad(signedX,signedY)
print("Binary Two's complement: x="+signedX+" y="+signedY)

##########booths multiplication########
print("\nApplying Booths Multiplication: "+str(x)+"x"+str(y))
m=signedX
q=signedY
negm=gettwos(m)
n=len(signedX)
a='0'*n
q0='0'
while(n>0):
	q1=q[-1]
	if q1+q0=='01':
		a=add(a,m)
	if q1+q0=='10':
		a=add(a,negm)
	a,remove=rightShift(a,a[0])
	q,remove=rightShift(q,remove)
	q0=remove
	n=n-1
ans=a+q
print("Decimal:",getDecimal(ans))
print("Binary (Two's complement):",ans)

##########booths division##########
print("\nApplying Booths Division: "+str(x)+"/"+str(y))
if y==0:
	print("y=0 Therefore division is not defined")
	sys.exit()

div_q = binary(abs(x))
div_m = binary(abs(y))
if(len(div_m)>len(div_q)):
	n = len(div_m)
	div_q = '0'*(len(div_m)-len(div_q)) + div_q
else:
	n = len(div_q)
	div_m = '0'*(len(div_q)-len(div_m)) + div_m

div_a = '0'*n
div_negm = gettwos('0'+div_m)
while(n>0):
	if(div_a[0]=='1'):
		div_q,remove=leftShift(div_q, '0')
		div_a,remove=leftShift(div_a, remove)
		div_a = add(div_a, div_m)
	else:
		div_q,remove=leftShift(div_q, '0')
		div_a,remove=leftShift(div_a, remove)
		div_a = add(div_a, div_negm)
	if(div_a[0]=='1'):
		div_q = div_q[0:-1]+'0'
	else:
		div_q = div_q[0:-1]+'1'
	n-=1
if(div_a[0]=='1'):
	div_a = add(div_a,div_m)
quotient = '0'+div_q
remainder = '0'+div_a

if(x*y<0):
	quotient = gettwos(quotient)
if(x<0):
	remainder = gettwos(remainder)

print("Quotient:", getDecimal(quotient))
print("Remainder:", getDecimal(remainder))
print("Binary Quotient:", quotient)
print("Binary Remainder:", remainder)
