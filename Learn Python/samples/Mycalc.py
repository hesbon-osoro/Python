from tkinter import*
import math
def act(r):
	global s
	s+=r
	out.configure(text="{}".format(s))
def answer():
	global s
	global s2
	if len(s)>0:
		result=eval(s)
		s=str(result)
		s2=s
		out2.configure(text="{}".format(s))
def _current_answer(q):
	global s
	s=s2
	out.configure(text="{}".format(s))
def clear():
	global s
	if len(s)>0:
		s=""
		out.configure("{}".format(s))
		out2.configure("{}".format(s))
def _backspace():
	global s
	if len(s)>0:
		end=len(s)
		l1=list[s]
		del l1[end]
		s="".join(l1)
		out.configure(text="{}".format(s))
def to_fraction(m):
    'this is added code in this method'
    return math.modf(m)
def	squareroot(l):
	global s
	for i in s:
		if i=="√":
			return True
def square(k):
	global s
	s=s+k
	out.configure(text="{}".format(s))
def raise_to_power(j):
	return math.pow(j,2)
def logarythm(i):
    return math.log10(i)
def naturallog(h):
    return math.log(h)
def sine(g):
    return math.sin(g)
def cosine(f):
    return math.cos(f)
def tangent(e):
    return math.tan(e)
def cube(d):
    return math.pow(d,3)
def cuberoot(c):
    return math.pow(c,(1.0/3))
def combination(a,bg):
    'for demonstration only'
    return float(a)/bg
s=""
out=Label(text="0",bg="teal",font=("verdana",16,"bold"),width=66,height=1)
out2=Label(text="0",bg="purple",font=("verdana",16,"bold"),width=66,height=2)
frame=Frame()
one=Button(frame, text="1",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r="1" : act(r))
two=Button(frame, text="2",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r="2" : act(r))
three=Button(frame, text="3",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r="3" : act(r))
four=Button(frame, text="4",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r="4" : act(r))
five=Button(frame, text="5",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r="5" : act(r))
six=Button(frame, text="6",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r="6" : act(r))
seven=Button(frame, text="7",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r="7" : act(r))
eight=Button(frame, text="8",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=3,command=lambda r="8" : act(r))
nine=Button(frame, text="9",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r="9" : act(r))
zero=Button(frame, text="0",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r="0" : act(r))
decimal=Button(frame, text=".",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r="." : act(r))
asterisk=Button(frame, text="*",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r="*" : act(r))
add=Button(frame, text="+",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r="+" : act(r))
subtract=Button(frame, text="-",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r="-" : act(r))
divide=Button(frame, text="/",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r="/" : act(r))
modulus=Button(frame, text="%",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r="%" : act(r))
bracket1=Button(frame, text="(",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r="(" : act(r))
bracket2=Button(frame, text=")",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r=")" : act(r))
factorial=Button(frame, text="!",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r="!" : actr(r))
ans=Button(frame, text="Ans",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=_current_answer)
equal=Button(frame, text="=",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command= answer)
AC=Button(frame, text="AC",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=clear)
DEL=Button(frame, text="DEL",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=_backspace)
a_bc=Button(frame, text="Ab/c",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r= "f": to_fraction(r))
root=Button(frame, text="√",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r= "√": squareroot(r))
square=Button(frame, text="X^2",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda k=s : square(k))
_raise=Button(frame, text="y^x",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r= "p": raise_to_power(r))
logarithm=Button(frame, text="log",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r= "l": logarythm(r))
_ln=Button(frame, text="ln",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r= "n": naturalLog(r))
sin=Button(frame, text="sin",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r= "s": sine(r))
cos=Button(text="cos",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r= "c": cosine(r))
tan=Button(frame, text="tan",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r= "t": tangent(r))
cube=Button(frame, text="X^3",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r= "r": cube(r))
cuberoot=Button(frame, text="∛",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r= "o": cuberoot(r))
_nCr=Button(frame, text="nCr",font=("consolas",13,"bold"),bg="grey",fg="green",width=25,height=2,command=lambda r= "m": combination(r))
#out.grid(frame, row=0,column=0)

#out2.grid(frame, row=1,column=0)
out.grid(row=0,column=0)
out2.grid(row=1,column=0)

zero.grid(row=8 ,column=0)
decimal.grid(row=8 ,column=1)
ans.grid(row=8 ,column=3)
equal.grid(row=8 ,column=4)
modulus.grid(row=8 ,column=2)

add.grid(row=7 ,column=4)
subtract.grid(row=7 ,column=3)
one.grid(row=7 ,column=0)
two.grid(row=7 ,column=1)
three.grid(row=7 ,column=2)

asterisk.grid(row=6 ,column=3)
divide.grid(row=6 ,column=4)
four.grid(row=6 ,column=0)
five.grid(row=6 ,column=1)
six.grid(row=6 ,column=2)

seven.grid(row=5 ,column=0)
eight.grid(row=5 ,column=1)
nine.grid(row=5 ,column=2)
AC.grid(row=5 ,column=4)
DEL.grid(row=5 ,column=3)

bracket1.grid(row=4 ,column=4)
bracket2.grid(row=4 ,column=3)
a_bc.grid(row=4 ,column=2)
root.grid(row=4 ,column=1)
square.grid(row=4 ,column=0)

_raise.grid(row=3 ,column=4)
logarithm.grid(row=3 ,column=3)
_ln.grid(row=3 ,column=2)
sin.grid(row=3 ,column=1)
cos.grid(row=3 ,column=0)

tan.grid(row=2 ,column=4)
cube.grid(row=2 ,column=3)
cuberoot.grid(row=2 ,column=2)
_nCr.grid(row=2 ,column=1)
factorial.grid(row=2 ,column=0)

mainloop()