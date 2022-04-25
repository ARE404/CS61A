# Week 1-2

[toc]

# Lec 1: Functions ( 1/17 )

## 1.1: Getting started
{http://composingprograms.com/pages/11-getting-started.html#errors}
> "A language isn't something you learn so much as something you join." ———— Arika Okrent

### Statements & Expressions*
Broadly, computer programs consist of instructions to either
1. Compute some value
2. Carry out some action
Statements typically describe actions. When the Python interpreter executes a statement, it carries out the corresponding action. 
On the other hand, expressions typically describe computations. When Python evaluates an expression, it computes the value of that expression.
### Functions
Functions encapsulate logic that manipulates data.
### Objects 
An object seamlessly bundles together data and the logic that manipulates that data, in a way that manages the complexity of both. 
### Interpreter
Evaluating compound expressions requires a precise procedure that interprets code in a predictable way. A program that implements such a procedure, evaluating compound expressions, is called an interpreter. 
### error
1. Test incrementally
2. Isolate errors: modular design
3. Check your assumptions: precise assumptions
4. Consult others: team work

## 1.2: Elements of programming
{http://composingprograms.com/pages/12-elements-of-programming.html}
> A programming language is more than just a means for instructing a computer to perform tasks. The language also serves as **a framework within which we organize our ideas about computational processes**. Programs serve to **communicate** those ideas among the members of a programming community. Thus, **programs must be written for people to read, and only incidentally for machines to execute**.
> When we describe a language, we should pay particular attention to the means that the language provides for **combining simple ideas to form more complex ideas**. Every powerful language has three such mechanisms:
1. **primitive expressions and statements**, which represent the simplest building blocks that the language provides,
2. means of **combination**, by which compound elements are built from simpler ones
3. means of **abstraction**, by which compound elements can be named and manipulated as units.
In programming, we deal with two kinds of elements: functions and data. (Soon we will discover that they are really not so distinct.) Informally, data is stuff that we want to manipulate, and functions describe the rules for manipulating the data. Thus, any powerful programming language should be able to describe primitive data and primitive functions, as well as have some methods for combining and abstracting both functions and data.

### 1.2.1 expression: infix notation & function notation
### 1.2.2 call expression
infix notation, though can be implement by interpreter, is a mathematical convention.
compared to this form, function notation have three advantages:
1. can take an *arbitrary* number of arguments, no *ambiguity* can rise.
2. can extend in a straightforward way to nested expressions, and there is no limits.
3. avoid complex form.

### 1.2.3 import statement
An import statement **designates** a module name (e.g., operator or math), and then lists the named **attributes** of that module to import (e.g., sqrt). 

### 1.2.5 Evaluating Nested Expressions

The evaluation procedure is **recursive** in nature.
evaluation procedure
expression tree

### 1.2.6 The Non-Pure Print Function

two kinds of function:

1. Pure function: has input and output, no effects beyond returning a value
2. Non-Pure function: can generate side effects

## 

# Lec 2: Names ( 1/19 )

## Names & Assignment & Bindings  

Binding a name to a result of a expression have three different ways:

- Assignment statement can help you defined your own name, binding to the result of an expression, it is also our simplest means of abstraction.

- What import statement actually dose is binding a module function to a specified name, such as "from operator import add" means bind function "add" to the name add.
- Def statement let you create your own function, 

> The possibility of binding names to values and later retrieving those values by name means that the interpreter must maintain some sort of memory that keeps track of the names, values, and bindings. This memory is called an environment.

## Sync Problem

Assignment statement evaluate only once, then the name's value is certain.

Function evaluates every time it be called.

## Environment Diagrams 

Environment is like a memory keeps the binding information between names and values

 - Frames(作用域?)
   **An environment in which an expression is evaluated consists of a sequence of frames**
   Frames includes bindings
 - Global frame   
 - intrinsic name& bound name
   intrinsic name is the only name for one function; bound name is the name stored in frames as a mark for a function/number

## Defining functions

Conpare to assignment, **Functions** are a much more powerful tool for abstraction.

def <function_name>(<format parameter>):
    return <return_expression>
(4 spaces indent must be required ! )

- Function signature & Function body

first line of definition , after def is called function signature, the rest line is called function body.

Function signature is important, it tells us how to structure a local frame every time we call the function, while the body tells us how to do afterwards.

- Execute procedure for def statement
  1. use function signature <name>(<format parameter>) create a function.
  2. set but **not execute** function body
  3. bind <name> to the function in the current frame

## Calling user-defined function

Procedure for calling a user-defined function:

1. Add a local frame, form a new environment 
2. Bind formal parameters to arguments in that frame
3. Execute function body in new environment

## Looking up names in environments

```
An environment is a sequence of frames.
    A name evaluates to the value bound to that name in the earliest frame of the current
    environment in which that name is found.
```

# Lec3: Control ( 1/22 )

## Print and None (None-Pure Function)

```python
>>> print(print(1), print(2))
1
2
None None
```

None is not displayed by the interpreter, but can be displayed by using Print function.

None-Pure function also have return value, but None.

## Mutiple Environments

The Environment is liked a stack of frames.
A name evaluates to the value bound to that name in the earliest frame of the current environment in which that name is found.(How to calculate a name's value)

## Miscellaneous Python features

- 3 different division: 

  Integer division // (3//2=1) don't have remainder

  True division / 

  Mod %

- Return multiple values

- Default parameter

- Docstring testing tool

```
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """

python3 -i test.py //interactive mod
python3 -m doctest test.py  //test docstring cases, nothing returned
python3 -m doctest -v test.py //test and return result
```

## Condition Statement

A statement is is executed to perform a action 

Compound Statement - Clause - suite

## Boolean Context

False value in python: ` false, 0, '', None`

True value in python: Anything else 

## Iteration 

means "repeat"\

## While Statement

```python
i = 0;
while i > 3:
  i = i + 1;
```

# Lec 4: Higher-Order Functions ( 1/24 )

## Iteration Example: Fibonacci sequence

```python
0 1 1 2 3 5 8 13 21 34 55 89
def fib(n):
	"""
	compute the nth fibonacci number
	>>> fib(5)
	5
	>>> fib(11)
	89
	"""
	 
	pred, curr = 0, 1	#0th and 1th fibonacci number
  i = 1							#curr is ith fibonacci number
	while(i < n):
		pred, curr = curr, pred + curr 	
    #this is interesting because we don't need a middle number to store pred
		i = i + 1
	return curr
```

if want to start from 0th, change `pred, curr = 0, 1` to `pred, curr = 1, 0`, and change ` i = 1` to `i = 0`

## Designing functions

How to describe a function: Domain Range Behavior 

- One job at a time
- DRY: Don't repeat yourself
- Define a function generally

## High-Order functions

High-Order functions: A function that takes a function as an argument value or returns a function as a return value

### Generalizing Patterns with Arguments

```python
"""Generalization"""

from math import pi, sqrt

def area(r, shape_constant):
  #DRY
	assert r > 0, "r can't be nagitive"
	return r * r * shape_constant

def area_circle(r):
	return area(r, pi)

def area_square(r):
	return area(r, 1) 

def area_hexagon(r):
	return area(r, 3 * sqrt(3) / 2)
```

### Generalizing Over Computational Processes

1. Pass function as an argument

```python
"""Computational Processes Generalization"""

def summation(n, term):
	"""
	Sum the first N function return value
	>>> sum_naturals(3, cube)
	36
	"""
	total, k = 0, 1
	while k <= n:
		total, k = total + term(k), k + 1
	return total

def cube(k):
	return pow(k, 3)

def whatever(k):
	return 8 / (4 * k - 3) * (4 * k - 1)
```

2. Return a function

```python
"""Computational Processes Generalization"""
def make_adder(n):
	"""return a function that takes one parameter K and return K + N

	>>> add_three = make_adder(3)
	>>> add_three(2)
	5
	>>> make_adder(20)(80)
	100
	"""
	def adder(k):
		return k + n
	return adder
```

### The Purpose of High-Order Functions

- Shows that functions are first-class values
- Express general methods of computation
- Remove repetition(DRY)
- Separate concerns among function(one thing at a time)

## Lambda Expressions

can be used to make quick function

A expression evalutes to a function

```python
>>> square = lambda x:x * x
>>> square

<function <lambda> at 0x102ab31f0>
>>> (lambda x:x + x)(2)
4  
```

! : lambda expression in python can't have statement

### Lambda Expressions Versus Def Statement

Only Def Statement give us a intrinsic name

Def: apple - apple(Func)

Lambda: apple - Func

```python
>>> sum = lambda x:x + x
>>> sum
<function <lambda> at 0x102ab3280>
>>> def sum(x):
...     return x + x
... 
>>> sum
<function sum at 0x102ab3310>
```

# Lec 5: Environments ( 1/26 )

## Environments for High-Order Functions

Previous environment diagrams still work for High-Order Functions.

## Example: Repeat

```python
def repeat(f, x):
	while f(x) != x:
		x = f(x)
	return x

def g(y):
	return (y + 5) // 3

result = repeat(g, 5) #2
```

## Environment for Nested Definitions

The function parent is where the function is defined, it can help us to get frame parent, which can be used for figuring out current environment. 

- Every user-defined function has a parent frame(often global)
- **The parent of a function is the frame in which it was defined**
- Every local frame has a parent frame (often global)
- The parent of a frame is the parent of the function (parent copy)

## How to Draw an Environment Diagram

- When function is defined:
  1. Create function value: func <name> (<formar parameters>) [parent = <parent>] parent is the current frame
  2. Bind name to the function value in the current frame

- When a function is called:
  1. Add a local frame
  2. Copy the parent of the function to the local frame
  3. Bind the <formal parameters> to the arguments in the local frame

## Local Name

```python
>>> 
>>> def f(x, y):
...     return g(x)
... 
>>> def g(a):
...     return a + y
... 
>>> f(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in f
  File "<stdin>", line 2, in g
NameError: name 'y' is not defined
>>> 
```

Since g(a) is defined in global frame, the parent of g frame is also global frame, so it can't find name y, which is defined in f frame.

- The Environment created by calling a top-level function (no def within def) consists of one local frame, followed by the global frame

## Function Composition

```python
def compose1(f, g):
	def h(x):
		return f(g(x))
	return h

def square(x):
	return x * x

def triple(x):
	return 3 * x

def make_adder(n):
	def adder(k):
		return k + n
	return adder
---
>>> squadder = compose1(square, make_adder(2))
>>> squadder(3)
25
>>> compose1(square, make_adder(2))(3)
25
>>> compose1(square, triple)(5)
225
>>> compose1(triple, square)(5)
75
>>> 

```



# Labs & HWs

## Use OK to check homework

```bash
python3 ok --local
```

## Use Python Docstring testing tool

```python
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """

python3 -i test.py //interactive mod
python3 -m doctest test.py  //test docstring cases, nothing returned
python3 -m doctest -v test.py //test and return result
```

