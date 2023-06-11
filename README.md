# Wtyczka QGIS
## Opis
Wtyczka została stworzona w celu obliczania wysokości pomiędzy dwoma punktami oraz pola powierzchni pomiędzy punktami. Została w niej dodana możliwość wgrywania plików txt lub csv do odpowiednich układów współrzędnych. Wtyczka umożliwia również przeliczanie pola powierzchni w różnych jednostakch powierzchni oraz narysowanie poligonu na warstwie tymczasowej.

**Funkcjonalność wtyczki**
```mermaid
  graph TD;
      A[Funkcjonalnościwtyczki]-->B[obliczenie różnicy wysokości];
      A --> C[podanie na pasku informacyjnym tekstu wynikowego]
      A --> D[obliczenie pole powierzchni]
      D --> E[Podanie wyniku w różnych jednostkach]
      D --> F[Możliwość narysowania poliognu] 
```
\
\
\
```mermaid
  graph TD;
      A[Funkcjonalności wtyczki]--> B[Wskazanie układu współrzędncyh dla wgrywanego pliku]
      B --> D[Dodanie warstwy tymczasowej z danymi z pliku]
      D --> C[Dodanie atrybutu area dla utworzonej warstwy] 
```

–wybór dwóch punktów z aktywnej warstwy oraz obliczenie różnicy wysokości\
–podanie na pasku informacyjnym interfejsu QGIS tekstu wynikowego\
–wybór minimum trzech punktów z warstwy\
–obliczenie pole powierzchni na podstawie współrzędnych zaznaczonychpunktów metodą Gaussa\
–monit w przypadku zaznaczenia zbyt małej liczby punktów do wykonaniaobliczeń
–Wskazanie w jakim układzie współrzędnych będzie plik do wgrania: 1992czy 2000 (+ strefa)\
Wybranie i otwarcie pliku tekstowego .txt lub .csv,\
∗Wgranie zawartości pliku do pamięci podręcznej aplikacji - umiejscowieniew tabeli (QTableWidget),∗Dodanie warstwy w odpowiednim układzie odniesienia (EPSG) do bieżą-cego projektu QGIS,–na podstawie zaznaczonych punktów do obliczenia pola powierzchni, narysujpoligon, dodaj go do nowej warstwy projektu i sprawdź atrybutgeometry().area()dla porównania,1
–czyszczenie konsoli wynikowej i zaznaczenia obiektów na żądanie użytkownika,–wybór opcji czy pole powierzchni ma być wyświetlane w m2czy w arach czyw ha i wyświetlenie wyniku obliczenia zgodnie z wyborem użytkownika.


