# Pomysły na hackathon — przegląd (do zimnej oceny)

Hackathon: Warsaw Open Data, 42 Warsaw, 17–18.10, 24h, 18k PLN, zespół 3 + agenci AI. Wymóg: min. 1 zbiór z dane.um.warszawa.pl. Jury: miasto, ministerstwo cyfryzacji, biznes.

Kryteria oceny (wspólne, rozstrzygniemy po spłynięciu wszystkich propozycji):
- Fit z jury miejskim (użyteczność dla mieszkańca)
- Siła wykorzystania otwartych danych (nie fasada)
- Demo w 5 minut (jury klika samo)
- Realny scope na 24h (z gotowym .md i agentami)
- Potencjał po hackathonie (czy żyje dalej)

---

## Pomysł 1: Warsaw Terror (gra)

Gra terenowa bez wychodzenia z domu. 1 zmiennokształtny (strzyga / rusałka / bruxa) vs 4 łowców Zakonu św. Ezekiela. Mapa 2D Warszawy z żywymi pojazdami ZTM. Zmiennokształtny poluje jeżdżąc komunikacją, ładuje energię żerem (100→0% / 24h), rośnie w siłę; przeżyje 7 dni = wygrywa. Zakon trianguluje gniazdo po śladach, auto-battler w stylu Żultopii. Dwie formy ruchu łowców: auto (szybko, zero poszlak) vs ZTM (wolniej, poszlaki + spotkania). Demo: symulacja ~15 min z narratorem na ekranie, 5 graczy startuje razem.

Za:
- Najbardziej oryginalne, zapada w pamięć; zero konkurencji w tej niszy.
- Mocne użycie live danych ZTM (pozycje pojazdów jako mechanika, nie tło).
- Folklor słowiański jako wrapper kulturowy.
- Pokazuje kunszt techniczny (symulacja, balans, auto-battler).

Przeciw:
- Słaby fit z jury miejskim: gra o "polowaniu na ofiary" vs urzędnicy nagradzający użyteczność. Wymaga mocnego re-skinu (anomalie zamiast ofiar).
- Demo wymaga 5 ogarniętych graczy i tłumaczenia zasad — wysokie ryzyko, że jury nie załapie w 5 minut.
- Największy scope: 2 frakcje, 3 klasy, ekonomia energii, walki, plotki, triangulacja. Nawet z agentami najłatwiej o niedowiezione demo.
- Balans (energia, snowball, AFK-camping) nierozwiązany na papierze.
- Zależność od live API ZTM na sali (limity, pad WiFi) — obowiązkowy fallback.

## Pomysł 2: Tribes-web (eventy miejskie + mikro-eventy)

Slim webowa wersja Tribes: mapa Warszawy, dwie warstwy — oficjalne eventy z otwartego zbioru miasta (import z dane.um.warszawa.pl) + userowe mikro-eventy ("ktoś chętny na X"). Znajdowanie ludzi do pójścia na eventy, zakładanie własnych, dołączanie, czat. Stack: Vite + Leaflet + Firebase. Patryk ma działający pierwowzór (Expo, ~5–10h pracy), przepisanie web od zera z gotowym .md.

Za:
- Najlepszy fit z hasłem hackathonu i jury: civic-tech, realny problem (puste eventy, samotność w mieście).
- Dane miasta jako content, nie dekoracja — mapa żyje od sekundy 1.
- Demo trywialne: szukaj → filtruj → dołącz → załóż. Jury klika samo.
- Najmniejsze ryzyko techniczne: przepis znany, schemat danych istnieje, Leaflet darmowy.
- Żyje po hackathonie bez zmian.

Przeciw:
- Mało "wow": apek eventowych są dziesiątki, trzeba się wyróżnić (matching po zainteresowaniach, warstwa społecznościowa, jakość importu).
- Wartość zależy od jakości zbioru miasta — jeśli brak geo/czasu, trzeba geocoding + normalizację (AI) przed eventem.
- Ryzyko "kolejny CRUD": bez 1–2 mocnych mechanik (np. dopasowanie ekipy, smart powiadomienia) wygląda generycznie.
- Konkurencja na sali prawdopodobnie robi podobne rzeczy.

## Pomysł 3: (czeka na opis)

Miejsce na pomysł partnera / trzeci pomysł Patryka. Dopisz: 5 zdań opisu + jakie dane miasta używa + jak wygląda demo w 5 minut. Ocena zimno po spłynięciu, tymi samymi kryteriami co wyżej.
