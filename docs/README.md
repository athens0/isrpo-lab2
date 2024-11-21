# Common
## Info
A Python library for calculating areas and perimeters of geometric shapes like triange, circle and others.

Available shapes:
- circle: circle.py
- rectangle: rectangle.py
- square: square.py
- triangle: triangle.py

Import shape you need (for example circle.py) and use area or perimeter methods to get values. Formulas for the each shape are below.

# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Examples
## square.py
```python
import square

a = int(input())
print(square.area(a), square.perimeter(a))
```
### Input
> 3

### Output
> 9 12

## circle.py
```python
import circle

r = int(input())
print(circle.area(r), circle.perimeter(r))
```

### Input
> 3

### Output
> 28.274333882308138 18.84955592153876

## rectangle.py
```python
import rectangle

a = int(input())
b = int(input())
print(rectangle.area(a, b), rectangle.perimeter(a, b))
```

### Input
> 3\
> 4

### Output
> 12 14

## triangle.py
```python
import triangle

a = int(input())
b = int(input())
c = int(input())
h = int(input())
print(triangle.area(a, h), triangle.perimeter(a, b, c))
```

### Input
> 6\
> 8\
> 10\
> 8

### Output
> 24 48

# Tests

There a default tests in each file. unittest module required.

You can launch tests for each file by command:
> python.exe -m unittest "filename"


# Changelog
- 05c27fa (HEAD -> tests) Added tests for each file
- 8ba9aeb L-03: Circle and square added
- d078c8d (origin/main, origin/HEAD, main) L-03: Docs added
- ace71cb added rectangle.py
- 8d14b1f (HEAD -> new_features_467413) added triangle.py and fixed petimeter in rectangle.py
