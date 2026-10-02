# Warsaw Terror (nazwa robocza)

Gra terenowa bez wychodzenia z domu. 5 graczy, 1 sesja na żywo / Discord, start w tym samym momencie. Przeglądarka, mapa 2D Warszawy z żywymi liniami ZTM.

## Strony

1 zmiennokształtny (do wyboru: strzyga, rusalka, bruxa — istoty ze słowiańszczyzny) kontra 4 łowców z Zakonu św. Ezekiela.

Zmiennokształtny zakłada gniazdo obok przystanku i poluje, jeżdżąc komunikacją miejską. Musi żerować, żeby ładować pasek energii (100 → 0% w 24h gry, 1 ofiara = +50%). Energia napędza wszystko: ruch, moce specjalne, przeniesienie gniazda. Im dłużej żyje, tym silniejszy. Przeżyje 7 dni gry = wygrywa.

Zakon poluje w 4-osobowej grupie. Za każdego wyeliminowanego zmiennokształtnego dostaje pieniądze na lepszy ekwipunek. Łowcy poruszają się na dwa sposoby: samochodem (klik na mapie, dojazd po określonym czasie, zero poszlak) albo komunikacją miejską (wolniej, ale to daje poszlaki i szansę spotkania zmiennokształtnego). Walki w stylu auto-battlera (jak Żultopia / Pokemony): gracz decyduje o ruchu i starciu, samej walki nie kontroluje. Solo łowca nigdy nie ma szans; im silniejszy zmiennokształtny, tym więcej ludzi i lepszy sprzęt potrzeba.

## Core loop

Żerowanie na tych samych stacjach/liniach wyczerpuje teren (brak ofiar) i zostawia ślady. Zakon trianguluje gniazdo na podstawie miejsc polowań: zawężanie od szerokiego obszaru do punktu. Jeśli łowca i zmiennokształtny znajdą się w tym samym pojeździe, łowca może wywołać walkę.

## Moce (roboczo)

- Strzyga: niewidzialność za 50% energii.
- Rusałka: hipnoza ludzi (w tym łowców, żeby uciec) za 75% energii.
- Bruxa: przeniesienie gniazda za 25% (normalnie 75%).

## Demo na hackathon (to budujemy)

Pełna symulacja z lektorem-komunikatami: gra sama tłumaczy na ekranie co się dzieje, żeby jury łapało zasady bez wykładu. Skrócony czas (tydzień w ~15 minut), 5 graczy startuje razem, zmiennokształtny musi szybko zaatakować, żeby od razu pojawiły się sygnały do polowania.

Dane: pozycje autobusów/tramwajów z dane.um.warszawa.pl (api.um.warszawa.pl), cache na własnym backendzie, fallback do statycznego GTFS + symulacji gdy API padnie.

Język dla jury: żer = anomalie / wysysanie energii miejskiej, nie gore. Folklor + edukacja o mieście, zero "jedzenia ofiar".

---

## Problemy do rozważenia

Poniżej lista rzeczy, które trzeba domknąć przed / w trakcie hackathonu (24h, 3 osoby).

### 1. Tryb demo vs kampania
Pełny tydzień nie istnieje w demo. Potrzebny przełącznik czasu x100 od dnia 1 (flaga DEMO_SPEED). Bez tego jury nie zobaczy loopa żer → ślad → triangulacja → walka. Kto i kiedy przełącza tempo, czy tempo jest stałe przez całe demo.

### 2. Matematyka energii
100 → 0% w 24h + 1 ofiara = +50% oznacza śmierć przy 1 ofierze/dobę (trzeba 2). Do ustalenia przed kodem: tempo spadku, wartość ofiary, koszty mocy i przeniesienia gniazda w tych samych jednostkach. Rozjazd tutaj rozwala balans obu stron naraz.

### 3. Wymuszony start
5 graczy startuje razem, ale co jeśli zmiennokształtny nie atakuje? Demo umiera w 2 minuty. Potrzebny przymus: pierwszy atak w oknie N minut albo głód startowy (np. start od 40% energii). Plus skryptowane pierwsze poszlaki, niezależne od gracza.

### 4. Symulacja z narratorem
Kolejka komunikatów tłumaczących ekran (event log + toasty). Pytania: kto pisze teksty (1 osoba, przed hackathonem), czy narrator blokuje akcje, czy tylko komentuje, jak to wygląda po polsku i czy w ogóle po angielsku dla części jury.

### 5. Win condition
"Przeżyj 7 dni" brzmi prosto, ale co z AFK-camperem? Gniazdo bez żeru powinno więdnąć i świecić (sygnał dla zakonu). Zakon bez akcji powinien tracić fundusze / morale. Inaczej optymalna strategia to nie grać.

### 6. Triangulacja jako UI
Trzy poziomy precyzji (linia → rejon przystanków → konkretne gniazdo), fałszywe echa, koszt skanu (czas/energia/pieniądze). Ile skanów na minutę, żeby nie było spamu.

### 7. Ruch: samochód vs komunikacja
Zakon autem: klik → dojazd po czasie, zero poszlak. Komunikacją: wolniej, ale zbiera poszlaki + może spotkać cel. Do ustalenia liczby: czas dojazdu autem vs czas przejazdu ZTM na tym samym odcinku — auto musi być wyraźnie szybsze, inaczej nikt go nie użyje, a ma być wyborem taktycznym. Zmiennokształtny: czy też może autem, czy tylko ZTM?

### 8. Walka auto-battler
Skład 1v1 + boty-sojusznicy w demo (pełne 4v1 na żywo trudne do zgrania). Do ustalenia: próg siły (ilu łowców + jaki sprzęt na dany poziom mocy), czy walka w pojeździe różni się od walki na przystanku, co się dzieje z przegranym łowcą (śmierć / szpital / respawn).

### 9. Poszlaki i plotki (mięso detektywistyczne)
Trzy źródła: twarde (dane ZTM: ta linia była aktywna o X), miękkie (NPC na przystankach: plotki), społeczne (zgłoszenia). Do wymyślenia: 5–10 konkretnych typów poszlak, wagi, czas życia, fałszywe tropy stawiane przez moce (strzyga). Bez tego zakon patrzy w mapę i czeka.

### 10. Wyczerpywanie terenu
Polowanie w jednym miejscu = mniej ofiar + głośniejszy sygnał. Do ustalenia: po ilu żerach rejon się wyczerpuje, jak szybko się odnawia, czy gracz widzi licznik (tak — inaczej frustracja).

### 11. Snowball i balans późnej gry
Silny zmiennokształtny wymaga N łowców z drogim sprzętem — nowi/średni łowcy są bezużyteczni pod koniec. Potrzebna gumka: cap mocy, rosnący koszt utrzymania, wyższa nagroda za silny cel. Inaczej druga połowa tygodnia jest przesądzona.

### 12. Scope na 24h w 3 osoby
Mapa Leaflet + live ZTM + 2 frakcje + 3 klasy + walki + plotki to za dużo. Propozycja MVP: 2 linie, 1 klasa zmiennokształtnego, zakon 1 gracz + boty, 1 typ walki na liczbach, 1 ekran triangulacji. Reszta na slajd roadmap. Podział na 3 lane od godziny 0.

### 13. API miasta: klucz, limity, fallback
api.um.warszawa.pl: wyrobić klucz przed hackathonem, sprawdzić czy metro/SKM/KM są w tym samym feedzie (prawdopodobnie nie — tylko autobusy/tramwaje). Cache na backendzie (nigdy z przeglądarki prosto), fallback GTFS-statyczny + symulowane pozycje. Atrybucja danych na ekranie — jury miejskie to sprawdza.

### 14. Język dla jury z rady miasta
Zero gore i "jedzenia ludzi" w pitchu. Ofiary = incydenty / anomalie energetyczne. Podkreślić: folklor, otwarte dane, edukacja o komunikacji, bezpieczeństwo. Nazwa Warsaw Terror prawdopodobnie do zmiany przed prezentacją.

### 15. Kwestie techniczne demo
Przeglądarka + projektor na sali: wydajność mapy (limit markerów), polling (co ile sekund), co się dzieje przy padzie WiFi, plan B: nagranie przejścia + seed symulacji, żeby demo było powtarzalne. Seed = ten sam przebieg za każdym razem, jeśli jury poprosi o powtórkę.
