# Algorytmy-Geometryczne

## Uwagi
- Dla osób korzystających z systemu operacyjnego Windows, zalecamy wykorzystanie instalację wszystkiego na WSL, szczególnie przydatne, kiedy już zostały podjęte próby instalacji condy bez standardowych ścieżek instalacji lub kiedy na samym Windowsie coś nie działa
- Czasami zdarza się, że trzeba podmienić ```python3``` na ```python```, jest to zależne od wielu czynników

## Instalacja
Najpierw sklonuj repozytorium będąc w folderze do którego chcesz je sklonować, na przykład za pomocą:
```
git clone https://github.com/aghbit/Algorytmy-Geometryczne.git
```
Pobierz Anacondę, odpal Anaconda Prompt i przejdź do folderu Algorytmy-Geometryczne, tam stwórz środowisko:
```
conda create --name bit-alg python=3.9
conda activate bit-alg
```
Następnie uruchom:

```
python3 setup.py sdist
python3 -m pip install -e .
```
Otwórz Jupyter Notebook z listy programów w Conda Navigator, pamiętaj, żeby na górze zaznaczyć Twoje środowisko (bit-alg). Jeśli nie znajduje modułu bit-alg spróbój zrestartować środowisko i jupytera:
```
conda deactivate
conda activate bit-alg
```


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

Wyświetlanie wykresu
```python
vis.show()
```
![single](https://github.com/aghbit/Algorytmy-Geometryczne/assets/115979017/00361c74-80b7-47db-a5c2-17635c521d4f)

Wyświetlanie gifa
```python
vis.show_gif(interval=300)
```
![single](https://github.com/aghbit/Algorytmy-Geometryczne/assets/115979017/e081a98f-19ae-4810-ab60-533622a2d40d)

Wyrównanie osi 
```python
vis.axis_equal()
```
![plot](https://github.com/aghbit/Algorytmy-Geometryczne/assets/115979017/3a38e6bc-50db-4895-9311-d2eba3d22411)

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
![multiple](https://github.com/aghbit/Algorytmy-Geometryczne/assets/115979017/1601f760-187e-40de-a262-2d9e5b9c8035)

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
![removal](https://github.com/aghbit/Algorytmy-Geometryczne/assets/115979017/026d2e8e-a756-4448-a4b4-55a40b6063dc)

## Struktura repozytorium
Całe repozytorium składa się z sześciu folderów:
<li>lab1</li>
<li>lab2</li>
<li>lab3</li>
<li>lab4</li>
<li>tests</li>
<li>visualizer </li>

#### lab1-4
Tutaj znajdują się przygotowane notebooki, które musisz wypełnic. Każdy katalog odpowiada jednemu laboratorium
#### tests
Kod który wykonuje testy w poszczególnych notebookach znajduje się w plikach ```test1.py```, ```test2.py```, ```test3.py```, ```test4.py```.
Z kolei w folderach test2_tests, test3_tests, test4_tests można znaleźć pliki wejściowe i wyjściowe na podstawie których testowane są algorytmy, 
które są do napisania w ramach poszczególnych laboratoriów.

#### visualizer
Jest to katalog w którym zaimplementowane jest narzędzie graficzne. Opis korzystania z narzędzia graficznego znajduje 
się w README (jeden paragraf wyżej). Dodatkowo warto zapoznać się z plikiem [demo.ipynb](https://github.com/aghbit/Algorytmy-Geometryczne/blob/master/bitalg/visualizer/demo.ipynb)
w którym pokazane jest zastosowanie narzędzia graficznego już w samym notebooku


