# Balonowy radar

**12th CASSINI Hackathon, Warszawa, 27–29.11.2026**
**Wyzwanie: Challenge 3, Countering transnational crime and terrorism with space data**

Dokument trzyma się formatu z `12th_cassini_hackathon_idea_research_prompt_for_llms.md` (6 sekcji), a na końcu ma plan pracy na 48h, scenariusz demo i listę rzeczy do sprawdzenia od razu.

---

## 1. Pitch w jednym zdaniu i wyzwanie

Przewidujemy, dokąd polecą balony przemytnicze z Białorusi. Kontrola ruchu lotniczego dostaje konkretne okno zamknięcia zamiast wielogodzinnego paraliżu lotniska, a Straż Graniczna dostaje elipsę lądowania i patrol z nawigacją odporną na spoofing.

**Challenge 3:** przemyt transgraniczny, który władze Litwy nazywają atakiem hybrydowym.

**Problem w liczbach:**
- Lotnisko w Wilnie było przez balony zamknięte nawet na 11 godzin, a jedna noc zamknięć dotknęła ponad 1 700 pasażerów.
- Straż Graniczna (Podlaski Oddział) potwierdza, że Polska też kilkakrotnie miała balony nadlatujące z Białorusi.
- Zjawisko trwa nadal (ograniczenia nad lotniskiem w Wilnie we wrześniu 2026).
- Dziś lotnisko dowiaduje się o balonie, gdy ten jest już na radarze, i zamyka ruch zachowawczo na długo.

**Zdanie do pitchu:**
> Copernicus mówi, dokąd poleci balon. Galileo mówi patrolowi, że jego GPS nie kłamie. EGNOS gwarantuje, że miejsce znalezienia przemytu obroni się w sądzie.

---

## 2. Dane i sygnały EU Space: dokładny pipeline

### Copernicus: silnik prognozy i teren

| Dane | Skąd | Do czego |
|---|---|---|
| **Wiatr na poziomach ciśnienia** (u, v, wysokość geopotencjalna), ERA5 | Copernicus Climate Data Store (`cdsapi`) | Odtwarzanie prawdziwych incydentów z Wilna i kalibracja modelu. ERA5 ma kilka dni opóźnienia, więc **nie** nadaje się na żywo. |
| **Prognoza wiatru na żywo** | Prognozy CAMS global (Atmosphere Data Store), **do sprawdzenia, czy mają potrzebne pola wiatru na poziomach** | Prognoza trasy w trakcie demo. Fallback: otwarte dane ECMWF. **Uwaga:** to nie jest formalnie Copernicus, więc trzeba to uczciwie powiedzieć jury. |
| **Pokrycie terenu**: CORINE Land Cover i/lub Tree Cover Density | Copernicus Land Monitoring Service | Podział elipsy lądowania na las, pole, wodę i zabudowę. Las mocno zmienia sposób szukania, więc patrol dostaje informację, gdzie realnie szukać. |

**Co liczy pipeline:**
1. Wejście: punkt i czas wykrycia balonu (produkcyjnie z radaru operatora, na demo z doniesień o incydentach albo ze startu sondy).
2. **Monte Carlo:** kilkaset wariantów lotu z losowaną wysokością lotu, tempem wznoszenia i niepewnością czasu startu. Każdy wariant dryfuje z wiatrem interpolowanym w czasie i przestrzeni.
3. Wynik: **stożek prawdopodobieństwa trasy** i **elipsa lądowania** (np. 50% i 90%), a nie jedna linia.
4. **Przecięcie z korytarzami podejścia i odlotu lotniska**, czyli przedłużona oś pasa ok. 10 NM i do kilku tysięcy stóp. Współrzędne pasów z otwartych danych (OurAirports, OpenAIP).
5. **Alert:** prawdopodobieństwo konfliktu, przewidywany czas wejścia i zalecane okno zamknięcia.

### Galileo: OSNMA dla patrolu w strefie zakłóceń

- Balony lądują przy granicy z Białorusią, a tam GNSS bywa zagłuszany i podrabiany. Patrol szuka towaru dokładnie tam, gdzie nawigacji nie można ufać.
- **Ścieżka A (preferowana):** telefon z Androidem zapisuje surowe pomiary i komunikaty nawigacyjne Galileo I/NAV (GnssLogger albo `GnssNavigationMessage`), backend weryfikuje podpisy OSNMA biblioteką **OSNMAlib**.
- **Ścieżka B (fallback):** jeśli telefony nie wypuszczają komunikatów Galileo, weryfikacja OSNMA na prawdziwych nagranych danych referencyjnych. Mówimy to jury wprost.
- Wynik dla patrolu: **„pozycja uwierzytelniona”** albo **„uwaga: sygnał nieuwierzytelniony, nie ufaj mapie”**.

### EGNOS: granica błędu pozycji

- Telefony nie stosują EGNOS same z siebie, więc pozycję z EGNOS liczymy **na serwerze**: surowe pomiary z telefonu plus komunikaty EGNOS z archiwum ESA (EGNOS Message Server) albo z EDAS, przetworzone w RTKLIB w trybie SBAS.
- Wynik: pozycja z deklarowaną granicą błędu (protection level). Do czego służy:
  - miejsce znalezienia towaru zapisane z gwarantowaną dokładnością, czyli dowód do sprawy;
  - powiększenie elipsy szukania, gdy jakość pozycji spada.
- Bonus do narracji: EGNOS to system lotniczy (podejścia LPV), więc pasuje do historii o lotniskach.

### Walidacja na żywo (nie EU Space, ale prawdziwe dane)

- Sondy meteorologiczne IMGW (m.in. Legionowo) startują co 12 godzin, a ich pozycje są publicznie dostępne na żywo w otwartej sieci **SondeHub**.
- Używamy ich do sprawdzenia, czy prognoza wiatru i model dryfu działają: przewidziana trasa obok prawdziwej.

---

## 3. Dlaczego to nie jest duplikat

- **Nie wpada w żadną zakazaną kategorię z pliku z wytycznymi.** To nie heatmapa zagłuszania, nie dashboard zmian z Sentinel-2, nie tracker dark vessels i nie ogólna „platforma kryzysowa”.
- **Wynikiem jest decyzja, nie mapa:** okno zamknięcia dla kontroli ruchu i zgłoszenie z elipsą dla patrolu, wysyłane automatycznie (webhook, Telegram albo mail).
- **Łączymy nieoczywiste warstwy:** wiatr z Copernicusa, pokrycie terenu z CLMS, procedury podejścia lotnisk, otwarte dane sond, uwierzytelniony sygnał Galileo i EGNOS.
- **Uczciwie o konkurencji:** predyktory lotu balonów już istnieją (SondeHub, NOAA HYSPLIT). Nie konkurujemy z nimi kalkulatorem trasy. Nasza wartość to **warstwa zagrożenia**: konflikt z ruchem lotniczym, niepewność dla nieznanego balonu, elipsa dla patrolu z OSNMA i EGNOS.

---

## 4. Kupiec i model biznesowy

| Klient | Za co płaci | Dlaczego teraz |
|---|---|---|
| **Służby żeglugi powietrznej** (Oro Navigacija na Litwie, LGS na Łotwie, PAŻP w Polsce) | Krótsze, celowane zamknięcia zamiast wielogodzinnych | Powtarzające się zamknięcia w Wilnie, problem rośnie w regionie |
| **Lotniska** (Wilno, Kowno, Ryga, wschodnia Polska) | Mniej przekierowanych lotów i mniej odszkodowań dla pasażerów | Każda godzina zamknięcia to realne koszty |
| **Straże graniczne** (SG, VSAT) | Elipsa lądowania i patrol z nawigacją odporną na spoofing, więcej przejętego towaru | Ataki hybrydowe na wschodniej flance |

**Model przychodu (hipoteza do weryfikacji):** abonament SaaS za lotnisko albo sektor przestrzeni powietrznej, licencja dla straży granicznej za region.

**Skalowanie:** ten sam silnik działa dla każdego zagrożenia, które unosi wiatr: chmury chemiczne po pożarach, dym, dryfujące obiekty. Pitchujemy go jako **ochronę przestrzeni powietrznej przed zagrożeniami hybrydowymi**, a balony jako pierwszy przypadek użycia.

**Ramowanie dla polskiego jury:** problem wschodniej flanki UE, nie tylko Wilna. Otwieramy od potwierdzenia przez SG, że balony były też w Polsce.

---

## 5. Zakres prototypu na 48h

### Komponenty

1. **Silnik prognozy (Python):** pobieranie wiatru (`cdsapi`, `xarray`), interpolacja, Monte Carlo, elipsy.
2. **Warstwa zagrożenia:** korytarze podejścia, przecięcia, logika alertu, webhook.
3. **Walidacja na sondzie:** pobieranie lotu z SondeHub i porównanie przewidziany vs prawdziwy (błąd w km).
4. **Odtworzenie incydentu z Wilna:** ERA5 dla daty incydentu i oś czasu „tu byłby alarm”.
5. **Apka patrolu:** prosty widok web z elipsą, pokryciem terenu i statusem pozycji (OSNMA i EGNOS) z backendu.
6. **Backend GNSS:** wczytanie logów z GnssLogger, OSNMAlib, RTKLIB z danymi EGNOS.
7. **Front:** mapa (MapLibre albo Leaflet), panel alertów.

**Fresh Code Rule:** korzystamy z otwartych bibliotek (`xarray`, `cdsapi`, OSNMAlib, RTKLIB, biblioteki map), ale **nie forkujemy gotowego predyktora lotu**. Silnik dryfu, Monte Carlo i warstwę zagrożenia piszemy sami w trakcie weekendu.

### Podział na 2 osoby

| Osoba A: prognoza i zagrożenie | Osoba B: GNSS, patrol i pitch |
|---|---|
| Dane Copernicus (ERA5, CAMS, CLMS) | Test telefonów i logi GnssLogger |
| Silnik dryfu i Monte Carlo | OSNMAlib, czyli weryfikacja OSNMA |
| Korytarze lotniska i alerty | RTKLIB z EGNOS, czyli granica błędu |
| Walidacja na SondeHub | Widok patrolu i webhook |
| Odtworzenie incydentu z Wilna | Slajdy, scenariusz demo, nagranie zapasowe |

### Harmonogram

- **Piątek wieczór i noc:** checklista z sekcji 8, pobranie danych, szkielet silnika dryfu, pierwsze logi z telefonów przy oknie.
- **Sobota do 13:00:** Monte Carlo i elipsy, OSNMA na danych, pierwsza mapa.
- **Sobota 13:00:** **próba generalna na sondzie z Legionowa** (start o 12 UTC): przewidujemy lot i sprawdzamy po wylądowaniu.
- **Sobota popołudnie i noc:** korytarze lotniska, alert i webhook, EGNOS w RTKLIB, odtworzenie incydentu z Wilna, pokrycie terenu.
- **Niedziela do 12:00:** dopracowanie front-endu, nagranie zapasowe demo (na wypadek awarii internetu albo braku sondy).
- **Niedziela 13:00:** start sondy, uruchamiamy prognozę na żywo.
- **Niedziela 15:00:** deadline zgłoszeń. **15:05:** pitch z prawdziwą sondą na ekranie.

---

## 6. Największe ryzyka i pytania jury

| Atak jurora | Obrona |
|---|---|
| „Skąd wiecie, na jakiej wysokości leci balon przemytniczy?” | Nie wiemy i tego nie udajemy. Dlatego liczymy Monte Carlo po wysokościach i pokazujemy stożek prawdopodobieństwa, a nie linię. Z każdym przejętym balonem model się kalibruje. |
| „Sonda to nie balon przemytniczy” | Racja: sonda pęka na ok. 30 km, balon przemytniczy leci niżej. Sonda waliduje prognozę wiatru i model dryfu, a nie wysokość lotu przemytu. Mówimy to sami w pitchu. |
| „Skąd macie wykrycia z radaru?” | Nie mamy. Produkcyjnie wejściem jest radar operatora, a na demo doniesienia o incydentach i start sondy. |
| „Predyktory balonów już istnieją” | Tak (SondeHub, HYSPLIT). Nasza wartość to warstwa zagrożenia: konflikt z podejściami lotniska, elipsa dla patrolu, OSNMA i EGNOS. |
| „Galileo to tu tylko nawigacja” (jury z ChipCraft) | Nie: OSNMA działa w strefie, gdzie GNSS jest podrabiany, a EGNOS daje granicę błędu jako dowód. Pokazujemy prawdziwą weryfikację. |
| „Prognoza CAMS albo ECMWF to nie Sentinel” | Copernicus to nie tylko Sentinele. Wiatr to serwis Copernicus (C3S, CAMS), a pokrycie terenu to CLMS. Jeśli prognoza na żywo idzie z otwartych danych ECMWF, mówimy to wprost. |
| „Rynek jest za mały” | Mały, ale bardzo drogi problem z konkretnym budżetem. Silnik skaluje się na każde zagrożenie unoszone przez wiatr. |

**Ryzyka techniczne:**
1. Telefony mogą nie wypuszczać komunikatów nawigacyjnych Galileo. Wtedy przechodzimy na ścieżkę B dla OSNMA.
2. Dostęp do danych EGNOS (EDAS wymaga rejestracji, archiwum ESA trzeba sprawdzić).
3. Brak sygnału GNSS w budynku. Logi zbieramy przy oknie albo przed budynkiem.
4. Sonda może nie wystartować albo zniknąć z SondeHub. Mamy wtedy nagranie z soboty i odtworzenie incydentu z Wilna.

---

## 7. Scenariusz pitchu (3 min)

1. **Hook (15 s):** „Lotnisko w Wilnie zamknięte na 11 godzin. Przez balony z papierosami.” Zdjęcie albo nagłówek.
2. **Problem (30 s):** atak hybrydowy, Polska też ma balony, dziś reakcja przychodzi dopiero po wykryciu przez radar.
3. **Demo na żywo (75 s):**
   - mapa: sonda wystartowała dziś o 13:00 z Legionowa, nasza prognoza obok prawdziwej pozycji na żywo;
   - odtworzenie incydentu z Wilna: „tu poszedłby alert, zamknięcie na 40 minut zamiast 11 godzin”;
   - widok patrolu: elipsa z lasem i polem, status OSNMA, pozycja z granicą błędu z EGNOS.
4. **Trzy technologie w jednym zdaniu (15 s):** zdanie z sekcji 1.
5. **Biznes (30 s):** służby żeglugi powietrznej, lotniska, straże graniczne, abonament, skalowanie na zagrożenia hybrydowe.
6. **Zamknięcie (15 s):** „Balony już latają. My mówimy, dokąd.”

---

## 8. Do sprawdzenia od razu (piątek wieczór)

- [ ] **SondeHub:** czy widać dzisiejsze loty sond z Legionowa i o której startują (oczekiwane 00 i 12 UTC).
- [ ] **CAMS:** czy prognozy mają pola wiatru na poziomach ciśnienia. Jeśli nie, decyzja o fallbacku (ECMWF open data) i jak to komunikujemy.
- [ ] **Konto w Copernicus CDS/ADS** i klucz API (`cdsapi`).
- [ ] **GnssLogger:** czy telefony zapisują surowe pomiary i komunikaty nawigacyjne Galileo (test przy oknie).
- [ ] **EGNOS:** dostęp do archiwum komunikatów (EGNOS Message Server albo EDAS, w tym rejestracja).
- [ ] **OSNMAlib i RTKLIB:** instalacja i uruchomienie na przykładowych danych.
- [ ] **Incydenty z Wilna:** daty i godziny (np. zamknięcie 30.11.2025 i noc z kilkoma zamknięciami) do odtworzenia na ERA5.

---

## Źródła

- CASSINI Hackathon Poland: https://www.cassini.eu/hackathons/poland
- Straż Graniczna o balonach w Polsce (Rzeczpospolita): https://www.rp.pl/przestepczosc/art43218011-balony-z-papierosami-nad-litwa-przemytnicy-czy-sluzby-putina-i-lukaszenki
- 11 godzin zamknięcia lotniska w Wilnie (XYZ/PAP): https://xyz.pl/?p=143149
- Ponad 1 700 pasażerów jednej nocy (LRT): https://www.lrt.lt/pl/wiadomosci/1261/2820064/vitkauskas-o-balonach-najbardziej-intensywna-noc-w-tym-roku-odkryto-8-balonow
- Litwa o ataku hybrydowym (Eska): https://www.eska.pl/wiadomosci/przez-balony-z-bialorusi-lotnisko-w-wilnie-zostalo-zamkniete-litwa-mowi-o-ataku-hybrydowym-aa-skru-6D5d-FJtt.html
- Ograniczenia nad Wilnem, wrzesień 2026 (LRT): https://www.lrt.lt/pl/wiadomosci/1261/3060042/balony-przemytnicze-nad-wilnem-wprowadzono-ograniczenia-nad-wilenskim-lotniskiem
