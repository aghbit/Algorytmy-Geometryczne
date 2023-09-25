# Algorytmy-Geometryczne

## Instalacja

Najpierw sklonuj repozytorium, na przykład za pomocą:
```
git clone https://github.com/aghbit/Algorytmy-Geometryczne.git
```

Następnie uruchom:

```
cd Algorytmy-Geometryczne
python3 setup.py sdist
python3 -m pip install -e .
```

## Visualizer Tutorial
Initializing Visualizer class
```python
vis = Visualizer()
```

Adding title
```python
vis.add_title('Some title')
```
Adding grid
```python
vis.add_grid()
```

Adding single geometric figures
```python
vis = Visualizer()

# adding title
vis.add_title('Some title')

# adding grid
vis.add_grid()

# point = (x, y)
point = (3, 7)

# line_segment = ((x1, y1), (x2, y2))
line_segment = ((-1, 5), (0, 3))

# polygon [(x1, y1), (x2, y2), ..., (xn, yn)]
polygon = [(1, 2), (2, 5), (4, 5), (4, 2), (2, 1)]

# circle = (x, y, radius)
circle = (0, 7, 1)

# line = ((x1, y1), (x2, y2))
line = ((0, 2), (1, 5))

# half_line = ((x1, y1), (x2, y2))
half_line = ((0, 0), (3, -2))

vis.add_point(point)
vis.add_line_segment(line_segment, color='orange')
vis.add_line(line, color='red')
vis.add_polygon(polygon, alpha=0.7)
vis.add_circle(circle, color='green')
vis.add_half_line(half_line, color='purple')
```

Showing img
```python
vis.show()
```
![single](https://github.com/aghbit/Algorytmy-Geometryczne/assets/115979017/c0b32f64-0622-47ce-9c55-52cb4bfbdb0b)

Showing gif
```python
vis.show_gif(interval=300)
```
![single](https://github.com/aghbit/Algorytmy-Geometryczne/assets/115979017/ff9ac16a-c63b-4a08-8a4f-23e6d92e1a7c)

Saving img
```python
vis.save(filename='plot')
```

Saving gif
```python
vis.save_gif(filename='plot', interval=300)
```

Clearing data
```python
vis.clear()
```

Adding multiple geometric figures
```python
vis = Visualizer()

# point = (x, y)
points = []
for i in range(-5, 6):
    points.append((i, i**2))

# line_segment = ((x1, y1), (x2, y2))
line_segments = []
for i in range(1, 6):
    line_segments.append(((-i, i**2 - 1), (i, i**2 + 1)))

# polygon [(x1, y1), (x2, y2), ..., (xn, yn)]
polygons = [
    [(-14, -3), (-13, 0), (-11, 0), (-11, -3), (-13, -4)],
    [(-9, -10), (-6, -10), (-10, -6)],
    [(-10, -11), (-10, -15), (-15, -10), (-11, -10)]
]

# circle = (x, y, radius)
circles = [
    (-7, 0, 1),
    (-5, 0, 1),
    (-6, -2, 1)
]

# line = ((x1, y1), (x2, y2))
lines = [
    ((-3, 0), (-2, -3)),
    ((-3, 2), (-2, -2)),
    ((-3, 4), (-2, 1))
]

# half_line = ((x1, y1), (x2, y2))
half_lines = [
    ((-15, 10), (-15, 20)),
    ((-15, 10), (-10, 0)),
    ((-15, 10), (-20, 0))
]

vis.add_point(points, color='red')
vis.add_line_segment(line_segments)
vis.add_circle(circles, color='green')
vis.add_line(lines)
vis.add_polygon(polygons)
vis.add_half_line(half_lines, color='purple')
```
![multiple](https://github.com/aghbit/Algorytmy-Geometryczne/assets/115979017/3ec7762e-4003-44ff-95f9-03ee43e24efd)

Removing geometric figures
```python
vis = Visualizer()

points = [
    (0, 0), (1, 0), (1, 1), (0, 1), (-1, 1),
    (-1, 0), (-1, -1), (0, -1), (1, -1)
]

vis.add_point(points)
to_remove = []

for point in points[1:]:
    ls = vis.add_line_segment(((0, 0), point))
    to_remove.append(ls)

for ls in to_remove:
    vis.remove_figure(ls)

vis.show_gif()
```
![removal](https://github.com/aghbit/Algorytmy-Geometryczne/assets/115979017/95c5e2d9-391a-4a03-b2a3-9351f8d5e8ec)
