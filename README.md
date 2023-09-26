# Algorytmy-Geometryczne

## Instalacja

Najpierw sklonuj repozytorium, na przykład za pomocą:
```
git clone https://github.com/aghbit/Algorytmy-Geometryczne.git
```

Następnie uruchom:

```
cd Algorytmy-Geometryczne
Algorytmy-Geometryczne$ python3 setup.py sdist
Algorytmy-Geometryczne$ python3 -m pip install -e .
```
Żeby móc uruchomić notebook musisz stworzyć środowisko condy:
```
Algorytmy-Geometryczne$ conda create --name bit-alg python=3.9
Algorytmy-Geometryczne$ conda activate bit-alg
```
I wtedy możesz uruchomić serwer jupytera:
```
Algorytmy-Geometryczne$ jupyter notebook
```
Po uruchomieniu go wystarczy wejść na localhost:8888 (wpisz to w przeglądarkę)

<br>
W celu uniknięcia błędów wziązanych ze ścieżkami do różnych wersji interpreterów pythona
sugerujemy korzystanie z Linuxa, a na Windowsie zainstalowanie WSL-a i właśnie w nim uruchamianie wszystkich komend

## Przewodnik po wizualizacji
Inicjalizowanie klasy służącej do wizualizacji
```python
vis = Visualizer()
```

Dodawanie tytułu
```python
vis.add_title('Jakiś Tytuł')
```
Dodawanie siatki
```python
vis.add_grid()
```

Dodawanie pojedynczych figur geometrycznych
```python
vis = Visualizer()

# dodawanie tytułu
vis.add_title('Tytuł')

# dodawanie siatki
vis.add_grid()

# punkt = (x, y)
point = (3, 7)

# odcinek = ((x1, y1), (x2, y2))
line_segment = ((-1, 5), (0, 3))

# wielokąt [(x1, y1), (x2, y2), ..., (xn, yn)]
polygon = [(1, 2), (2, 5), (4, 5), (4, 2), (2, 1)]

# koło = (x, y, radius)
circle = (0, 7, 1)

# prosta = ((x1, y1), (x2, y2))
line = ((0, 2), (1, 5))

# półprosta = ((x1, y1), (x2, y2))
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

Zapisywanie wykresu
```python
vis.save(filename='plot')
```

Zapisywanie gifa
```python
vis.save_gif(filename='plot', interval=300)
```

Czyszczeine danych klasy
```python
vis.clear()
```

Dodawanie wielu figur
```python
vis = Visualizer()

# punkt = (x, y)
points = []
for i in range(-5, 6):
    points.append((i, i**2))

# odcinek = ((x1, y1), (x2, y2))
line_segments = []
for i in range(1, 6):
    line_segments.append(((-i, i**2 - 1), (i, i**2 + 1)))

# wielokąt [(x1, y1), (x2, y2), ..., (xn, yn)]
polygons = [
    [(-14, -3), (-13, 0), (-11, 0), (-11, -3), (-13, -4)],
    [(-9, -10), (-6, -10), (-10, -6)],
    [(-10, -11), (-10, -15), (-15, -10), (-11, -10)]
]

# okrąg = (x, y, radius)
circles = [
    (-7, 0, 1),
    (-5, 0, 1),
    (-6, -2, 1)
]

# prosta = ((x1, y1), (x2, y2))
lines = [
    ((-3, 0), (-2, -3)),
    ((-3, 2), (-2, -2)),
    ((-3, 4), (-2, 1))
]

# półprosta = ((x1, y1), (x2, y2))
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

Usuwanie figur geometrycznych
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

## Struktura repozytorium
Całe repozytorium składa się z sześciu folderów:
<li>lab1</li>
<li>lab2</li>
<li>lab3</li>
<li>lab4</li>
<li>tests</li>
<li>visualizer </li>

#### lab1-4
Tutaj znajdują się przygotowane notebooki które musisz wypełnic. Każdy folder odpowiada jednemu laboratorium
#### tests
Kod który wykonuje testy w poszczególnych notebookach znajduje się w plikach test1.py, test2.py, test3.py, test4.py.
Z kolei w folderach test2_tests, test3_tests, test4_tests można znaleźć pliki wejściowe i wyjściowe na podstawie których testowane są algorytmy, 
które są do napisania w ramach poszczególnych laboratoriów.

#### visualizer
Jest to katalog w którym zaimplementowane jest narzędzie graficzne. Opis korzystania z narzędzia graficznego znajduje 
się w README (jeden paragraf wyżej) oraz warto zapoznać się z plikiem [demo.ipynb](https://github.com/aghbit/Algorytmy-Geometryczne/blob/master/bitalg/visualizer/demo.ipynb)
w którym pokazane jest zastosowanie narzędzia graficznego już w samym notebooku


