# MyWAT

### End pointy:
POST:
```
/api/
	/post-sendMessage/ przeslanie plików, wiadomosci
		{nazwa_projektu,nazwa przedmiotu ,lista plików}
	/post-chat/ (na razie nie)
		/uid/
	/post-projectName/ dodanie np. SEMESTER
    {Nazwa}
    /post-przedmiotName/ dodanie np. WdA
    {Nazwa, NazwaProjektu}
	/post-user-id/ 
GET:
/api/
	/get-files/
		{NazwaPrzedmiotu, NazwaProjektu}
        //lista Notatek
	/get-messege/
		{NazwaPrzedmiotu, NazwaProjektu}
        //lista Notatek (tylko tekstowe)
	/get-all-projects-id/
        //lista Przedmotów
	/get-project-id/
	/get-user-id/
```
### Baza danych(Mongodb PyMongo):

/BD/

Wiadmosc:
	'nazwa_projektu': nazwa_projektu,
	'nazwa_przedmiotu': nazwa_przedmiotu,
	'Notatka': Notatka
	
Notatka:
- ID
- Nazwa użytkownika
- data
- Content
- format

Użykownik (na razie bez):
- ID Użytkownika
- nazwa użytkonika

### Aplikacja:
- Indeksuje i kataloguje informacje dotyczące materiałów edukacyjnych,
przydatnych linków oraz tutoriali powiązanych z konkretnymi przedmiotami i sekcjami na uczelni. 

- Użytkownicy mogą dodawać i oceniać materiały, a także przeglądać rekomendacje na podstawie swoich zainteresowań.

- Aplikacja społecznościowa dla studentów, umożliwiająca tworzenie grup tematycznych oraz znajdowanie innych studentów o podobnych zainteresowaniach poprzez interaktywną mapkę.


### Komedy przydatne
```


```
PeanutFromPoland check