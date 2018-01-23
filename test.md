Teorijski deo
---

Dati sto konciznije odgvore u formi prosto prosirenih recenica na svako od sledecih pitanja.

01. Sta je to JSON? JavaScript Object Notation
02. Sta je to XML? extensible markap language 
03. Sta je to URL? Uniform Resource Locator, sluzi za lociranje nekog sadrzaja na internetu
04. Sta je to HTTP? The Hypertext Transfer Protocol, predstavlja nacin preno;enja informacija na webu
05. Sta je to RESTful API? programski interfejs 
06. Koje HTTP metode imamo? Get i post
07. Sta je to DNS? Domain Name System
08. Sta je to private IP? IP adresa koja je rezervisana za internu upotrebu 
09. Sta je to AJAX? Asynchronous JavaScript skup tehnika koje se koriste za kreiranje asinhronih web aplikacija
10. Sta je to TCP/IP? Transmission Control Protocol/Internet Protocol, skup protokola koji se koristi da medjusobno poveze racunare na internetu 
11. Sta je to kes memorija? hardverska ili softverska komponenta koja cuva podatke kako bi njihovo naknadno pozivanje bilo brze 
12. Koja je razlika izmedju klase i objekta? klasa je skup objekata, ona im odredjuje atribute i opisuje njihovo ponasanje. Objekat je clan instance klasa

Backend
---

1. U `models.py` fajlu implementirati `Comment` model (klasu) u Python-u koja sadrzi atribute:
- `text`: sam komentar, i
- `date`: datum komentara u formatu `YYYY-MM-DD`
"Override"-ovati `__repr__` metod.

2. U `models.py` fajlu definisati `COMMENTS` varijablu koja sadrzi niz od 3 elementa koji su tipa `Comment`. 

3. U `app.py` fajlu napraviti Flask applikaciju koja ima `index` "view" funkciju koja handle-uje `/` route. Funkcija bi trebalo da vraca HTML string koji u `body`-ju sadrzi heading "Welcome!".

4. U `app.py` dodati `comments` "view" funkciju koja handle-uje `/comments` route. Funkcija bi trebalo da vraca HTML koji u `body`-ju sadrzi tabelu komentara. Koristiti Flask template.

5.  U `app.py` dodati `api_comments` "view" funkciju koja handle-uje `/api/v1.0/comments` route. Funkcija bi trebalo da vraca JSON reprezentaciju `COMMENTS` niza.

Frontend
---

U `home.html` fajlu imlementirati jednostavnu klijent aplikaciju kojom moze da testira prethodno implementirani API end point. Koristiti `form` i `iframe`.

Algoritmi
---

Napisati i JavaScript i Python funkciju koja predstavlja resenje sledeceg zadataka:

Write a program that prints the numbers from 1 to 100. But for multiples of three print `Fizz` instead of the number and for the multiples of five print `Buzz`. For numbers which are multiples of both three and five print `FizzBuzz`.

Uputstvo
---

Resenja i odgovore predati u okviru GitHub repozitorijuma.
