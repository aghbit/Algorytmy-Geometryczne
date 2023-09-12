# Algorytmy-Geometryczne

## Instalacja

Najpierw sklonuj repozytorium, na przykład za pomocą:
```
git clone https://github.com/aghbit/Algorytmy-Geometryczne.git ./Algorytmy-Geometryczne
```

Następnie uruchom:

```
cd Algorytmy-Geometryczne
python3 setup.py sdist
python3 -m pip install -e .
```

w wypadku błędów podczas uruchamiania komend pythonowych (tzn "python3 ... ") spróbuj uruchomić je przy uzyciu komendy
python (a nie python3)
tzn.:
```
cd Algorytmy-Geometryczne
python setup.py sdist
python -m pip install -e .
```
jeśli to nic nie dało i masz taki błąd typu:
```
Traceback (most recent call last):
  File "C:\Users\Julek\Algorytmy-Geometryczne\setup.py", line 1, in <module>
    from setuptools import setup
ModuleNotFoundError: No module named 'setuptools'
```
no to krótka piłka, musisz ten pakiet zainstalować, bo 'setuptools' jest niesbędne do zsetupowania naszego repo
więc wklejasz sobie:
```angular2html
pip install setuptools
```
jak Ci ta komenda nie zadziała i będzie krzyczał, że nie masz pipa to próbuj:
```angular2html
pip3 install setuptools
```
jak to nie zadziała to odpal sobie terminal / power shella / cmd jako administrator i wtedy próbuj odpalać te dwie powyższe komendy,
wtedy już powinno widzieć pipa. Jak dalej nie widzi, to nwm, szukaj w necie jak to ogarnąć.
<br><br>a teraz tak, jak już Ci widzi pipa, ale still coś nie działa to pip może coś podpowiadać. na przykład:
```
[notice] A new release of pip is available: 23.1.2 -> 23.2.1
[notice] To update, run: D:\Prywatne\jul\anaconda\python.exe -m pip install --upgrade pip
```
no to proszę, przeklejasz tę komendę i masz zupdatowanego pipa, wtedy jeszcze raz robisz pip install 
<br> <br>
no słuchaj nadal coś nie działa, nadal mi wyskakuje że nie ma modułu a pip mówi, że moduł jest. Tzn pip mówi, że requirement6 jest already satisified, a plik pythonowy, że ModuleNotFounderror.
<br>pip:
```angular2html
Requirement already satisfied: setuptools in d:\prywatne\jul\anaconda\lib\site-packages (63.4.1)
```
setup.py:
```angular2html
Traceback (most recent call last):
  File "C:\Users\Julek\Algorytmy-Geometryczne\setup.py", line 1, in <module>
    from setuptools import setup
ModuleNotFoundError: No module named 'setuptools'
```
<br>To może znaczyć, że pip instaluje Ci paczki do jednego interpretera (na moich przykładach do tego w folderze anaconda)
a innym interpreterem uruchamiasz ten plik gdy w terminalu wywołujesz komendę 'python setup.py sdist'
<br><br>To jak zrobić, żeby interpreter którym uruchamiasz skrypty widział te paczki? musisz dać do nich ścieżkę w pliku w którym masz probelm
<br> Czyli w moim przykładowym przypadku, setup.py nie widzi paczek które są w folderze "d:\prywatne\jul\anaconda\lib\site-packages"

no więc w pliku setup.py dodamy ścieżkę do tych modułów, zrobisz to tak:

```angular2html
import sys
sys.path.append("d:\\prywatne\\jul\\anaconda\\lib\\site-packages")
from setuptools import setup
```
musisz dodać ścieżkę przy użyciu biblioteki sys. A jak nie działa to nwm, jak to mówi powiedzenie:
<br>"U mnie działa, patrzyłeś na stacku?"
## Używanie narzędzi do wizualizacji