# Week 3-4

[toc]

# Lec6: Iteration ( 1/29 )



# Lec7: Recursion ( 1/31 )

# Lec8: Tree Recursion ( 2/2 )

## Order of Recursive calls

### The cascade function

### Inverse Cascade Function

```python
# Inverse Cascade
#---version1 from 404
def shrink(n):
	if(n >= 10):
		n = n // 10
	print(n)
	if(n >= 10):
		shrink(n)

def grow(n):
	if(n >= 10):
		n = n // 10
		grow(n)
		print(n)

def inverse_cascade(n):
	grow(n)
	print(n)
	shrink(n)
#---version2 using high-order function
#这个版本不知道为什么在命令行里面会报错, 在python tutor和PyCharm里面都没问题
def inverse_cascade(n):
	grow(n)
	print(n)
	shrink(n)

def f_then_g(f, g, n):
	if n:
		f(n)
		g(n)

grow = lambda n: f_then_g(grow,print,n//10)
shrink = lambda n: f_then_g(print,shrink,n//10)

```

## Tree Recursion

Tree-shaped processes arise whenever executing the body of a recursive function makes more than one call to that function.

```python
def fib(n):
	"""
	tree recursive version of computing fibonacci sequence
	>>> fib(35)
	9227465
	"""
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)
```

For now, this process is highly repetitive; fib is called on the same argument multiple times.

### Example: Counting Partitions



# Lec9: Function Example ( 2/5 )

# Lec10: Data Abstraction ( 2/9 )