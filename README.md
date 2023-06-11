# Wtyczka QGIS
## Opis
Wtyczka do programu QGIS została stworzona w celu obliczania różnicy wysokości oraz pola powierzchni pomiędzy wskazanymi przez użytkownika punktami. Umożliwia także rysowanie poligonu między wskazanymi punktami oraz wgrywanie plików ze współrzędnymi w formacie txt lub csv. Funkcje zostały przydzielone do 2 odrębnych zakładek w oknie wtyczki: 
- związane z obliczeniami (zakładka 1. Wysokość i pole powierzchni)
- związane z wgrywaniem pliku (zakładka 2. Wgraj plik)

## Funkcjonalność wtyczki
**Zakładka 1. Wysokość i pole powierzchni**

<br>
<br>

```mermaid
  graph TD;
      A[Wysokość i pole powierzchni]-->B[obliczenie różnicy wysokości];
      A --> C[obliczenie pola powierzchni]
      C --> E[podanie wyniku w różnych jednostkach]
      C --> F[rysowanie poliognu] 
      A --> D[podanie na pasku informacyjnym tekstu wynikowego]
```
<br>
<br>

**Zakładka 2. Wgraj plik**

<br>
<br>

```mermaid
  graph TD;
      A[Wgraj plik]--> B[wgranie pliku ze współrzędnymi]
      B --> C[wskazanie układu współrzędncyh dla wgrywanego pliku]
      A --> D[Dodanie warstwy tymczasowej z danymi z pliku]
      D --> E[Dodanie atrybutu area dla utworzonej warstwy] 
      
```
<br>
<br>

## Opis funkcji w poszczególnych zakładkach
### Zakładka 1. Wysokość i pole powierzchni

Wygląd okna po weściu w zakładkę:

<img src="zdj_md/wtyczka_1.PNG"  width="40%" height="40%">

**By obliczyć różnicę wysokości między punktami należy:**
-  wybrać dwa punkty z aktywnej warstwy w QGIS, używając w tym celu narzędzia "zaznacz obiekty" z panelu QGIS
-  wybrać w oknie wtyczki, w polu "Wybierz warstwę" warstwę, w której znajdują się zaznaczone wcześniej punkty
-  w polu "Oblicz" wybrać "Różnica wysokości"
-  Wcisnąć przycisk "Oblicz"

**Wynik**

Wynik pojawi się jednocześnie w polu "Wynik", a także na pasku informacyjnym interfejsu QGIS. W przypadku gdy użytkownik wybierze inną liczbę punktów niż dwa, w polu "Błędy" pojawi się informacja o nieprawidłowej liczbie wybranych punktów.

Efekt wyznaczania różnicy wysokości:
<img src="zdj_md/wtyczka_wys.PNG"  width="80%" height="80%">


**By obliczyć pole powierzchni należy:**

-  wybrać co najmniej 3 punkty z aktywnej warstwy w QGIS, używając w tym celu narzędzia "zaznacz obiekty" z panelu QGIS
-  wybrać w oknie wtyczki, w polu "Wybierz warstwę" warstwę, w której znajdują się zaznaczone wcześniej punkty
-  w polu "Oblicz" wybrać "Powierzchnia" (pojawi się opcja "Narysuj poligon", a w polu "Wynik" wybór jednostki wyświetlanego wyniku)
-  w polu "Wynik" wybrać jednostkę, wybierając spośród "m2", "a" lub "ha"
-  w polu "Oblicz" można wybrać opcję "Narysuj poligon". Należy wówczas pamiętać, że układ współrzędnych bieżącego projektu w QGIS musi być zgodny z układem współrzędnych, do którego należą zaznaczone punkty
-  Wcisnąć przycisk "Oblicz"

**Wynik** 

Wynik obliczonego pola powierzchni w wybranej jednostce pojawi się jednocześnie w polu "Wynik", a także na pasku informacyjnym interfejsu QGIS. Dodatkowo, w przypadku wyboru opcji "Narysuj poligon", do projektu dodana zostanie warstwa tymczasowa "Poligon". W przypadku, gdy użytkownik wybierze mniej punktów niż trzy, w polu "Błędy" pojawi się informacja o nieprawidłowej liczbie wybranych punktów. 

Efekt wyznaczania pola powierzchni wraz z rysowaniem poligonu:

<img src="zdj_md/wtyczka_pow.PNG"  width="80%" height="80%">

**By wyczyścić konsolę wynikową i zaznaczenie obiektów należy:**
- wybrać w oknie wtyczki, w polu "Wybierz warstwę" warstwę, w której znajdują się zaznaczone punkty
- Wcisnąć przycisk "Wyczyść" 
  
**Wynik** 

Wartość obliczonego pola powierzchni bądź różnicy wysokości w polu "Wynik" zniknie. Odznaczą się również wszystkie punkty i obiekty zaznaczone w bieżącym projekcie.

### Zakładka 2. Wgraj plik

Wygląd okna po wejściu w zakładkę:

<img src="zdj_md/wtyczka_plik.PNG"  width="40%" height="40%">

**Przykładowy wygląd pliku wgrywanego do programu**

Współrzędne (X, Y, Z) we wstawianym pliku muszą mieć część dziesiętną po kropce i być oddzielone od siebie średnikami:

```bash
5540883.974;7501304.251;100.125
5544653.338;7501989.823;125.152
5548638.675;7501690.090;111.458
5551573.724;7501718.971;145.215
5555466.448;7501509.210;154.133
5558803.270;7501885.332;101.458
5540977.765;7503683.699;105.125
5544932.500;7503979.439;111.254
5547867.289;7503678.933;132.988
5551852.878;7503845.129;124.254
5555467.513;7503693.592;123.899
5558495.534;7504068.584;168.154
5540887.496;7506282.309;147.154
```
**By wgrać plik należy**

-  w polu "Podaj źródło pliku" wskazać ścieżkę do pliku z danymi wektorowymi do wgrania. Plik musi być w formacie .txt lub .csv
-  w polu "Wybierz układ współrzędnych dla pliku" wybrać układ w którym znajdują się współrzędne we wgrywanym pliku. Należy wybrać między układem PL-1992 a PL-2000 (po wyborze układu PL-2000 pojawi się pole "strefy" oraz zdjęcie z zasięgiem poszczególnych stref)
-  W przypadku wyboru układu PL-2000 wybrać strefę, w którym znajdują się wstawiane punkty, wybierając spośród: "5", "6", "7" i "8"
-  W polu "Zdefiniuj nazwę warstwy" wpisać nazwę warstwy, do której po wstawieniu będą należeć punkty o współrzędnych zdefiniowanych w pliku
-  Wcisnąć przycisk "Dodaj warstwę"

**Wynik**

Do pamięci podręcznej aplikacji wgrane zostaną współrzędne (wartości współrzędnych poszczególnych punktów będą widoczne w tabeli atrybutów). Do bieżącego projektu wgrana zostanie warstwa tymczasowa o zdefiniowanej przez użytkownika nazwie, w wybranym przez niego układzie odniesienia EPSG (jednym z poniższych):
-  PL-1992 (EPSG:2180) 
-  PL-2000 strefa 5 (EPSG:2176) 
-  PL-2000 strefa 6 (EPSG:2177) 
-  PL-2000 strefa 7 (EPSG:2178) 
-  PL-2000 strefa 8 (EPSG:2179)\\

Wygląd okna wtyczki przy wgrywaniu pliku ze współrzędnymi w układzie PL-2000 w strefie 6. Punkty z wgrywanego pliku będą należeć do warstwy o nazwie "pl_2000_6" i wstawią się w układzie EPSG: 2177 :

<img src="zdj_md/wtyczka_wgrany.PNG"  width="40%" height="40%">

## Nieprawidłowe działanie programu

W niektórych przypadkach program niepoprawnie oblicza pole powierzchni metodą Gaussa

