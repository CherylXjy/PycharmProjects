#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
def my_abs(x):
    if x>= 0:
        return x
    else:
        return -x

print my_abs(18)
print '%.2f' % (math.pi/6)

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print x, y

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
nums=[1,2,3]
print "here %d" % calc(*nums)
print "\n"

def person(name, age, **kw):
    print 'name: ', name, 'age: ', age, 'other: ', kw
person('Michael',30)
person('Bob',36, city='Beijing')
person('Adam',45,gender='M',job='Engineer')
print "\n"
#with one star *kw
#person('Bob',36, 'Beijing')


kw={'city':'Beijing','job':'Engineer'}
person('Jack',24,city=kw['city'],job=kw['job'])
print "\n"


def func(a,b,c=0, *args, **kw):
    print 'a =',a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
func(1,2)
func(1,2,c=3)
func(1,2,3,'a','b')
func(1,2,3,'a','b',x=99)
print "\n"

print "calculate factorial"
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print fact(5)

def fact(n):
    return fact_iter(n,1)

def fact_iter(num, product):
    if num==1:
        return product
    return fact_iter(num-1, num*product)

print fact(5)
print

#while loop
print "while loop"
L=[]
n=1
while n<=99:
    L.append(n)
    n=n+2
print L

#切片 前十个数L[:10], 后十个数L[-10:]
#前十个数每两个取一个, L[:10:2]
#所有数,每5个取一个
L=range(100)
print L[:10]
print L[::5]
L1 = L[:]
print L1

#迭代
print
print "iteration"
d={'a':1,'b':2,'c':3}
for key in d:
    print key

print
from collections import Iterable
print isinstance('abc', Iterable)
print isinstance(123, Iterable)

#迭代,循环
print
for i,k in enumerate([1,2,3]):
    print i,k
for i in enumerate([1,2,3]):
    print i
print
for i, value in enumerate(['A', 'B', 'C']):
    print i, value
print
for i, j in enumerate([(1,1),(2,3),(4,5)]):
    print i, j
print
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y

#列表生成式
print
print range(1,11)
print [x*x for x in range(1,11)]
#二层迭代
print [m+n for m in 'ABC' for n in 'DEF']
import os
print [temp for temp in os.listdir('.')]
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.iteritems():
    print k,v

def rotate_left3(nums):
  i=nums[0]
  nums.pop(0)
  nums.append(i)
  return nums
nums=[1,2,3]
print rotate_left3(nums)

print

#filter
def not_empty(s):
    return s and s.strip()
print filter(not_empty, ['A', '', 'B', None, 'C', '  '])

#倒序排序
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted([36, 5, 12, 9, 21], reversed_cmp)

#ignore case
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print  sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
print sorted(['bob', 'about', 'Zoo', 'Credit'])


#装饰器
print
def now():
    print '2016-06-27'
f=now
f()
print now.__name__
print f.__name__
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
#decorator
@log
def now():
    print '2016-06-27'
now()
#the same as now=log(now)

print
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print "%s %s():" % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
@log("execute")
def now():
    print '2016-06-27'
now()
print
now = log('execute')(now)
now()
print now.__name__

#decorator
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

#base 参数
int('12345', base=8)
int2=functools.partial(int, base=2) #偏函数
print int2('1000000')
#the same as
kw={ 'base':2}
int('10010', **kw)

max2= functools.partial(max,10)
print max2(5,6,7) #args=(10,5,6,7) max(*args)

import signal
interval=1.0
ticks=0
def alarm_handler(signo, frame):
    global ticks
    print "Alarm", ticks
    ticks=ticks+110
    signal.alarm(interval)
signal.signal(signal.SIGALRM, alarm_handler)
signal.alarm(interval)


#error handling
import os, errno
try:
    os.execlp("foo")
except OSError as e:
    if e.errno==errno.ENOENT:
        print "not found"
    elif e.errno==errno.ENOEXEC:
        print "not executable"
    else:
        pass
