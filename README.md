# System ekspercki do rozpoznawania chorób

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Sprawozdanie](#sprawozdanie)
   - [Cele i wymagania](#cele-i-wymagania)
   - [Wykorzystane narzędzia](#wykorzystane-narzędzia)
   - [Zobrazowanie działania aplikacji](#zobrazowanie-działania-aplikacji)
   - [Podsumowanie ](#podsumowanie)
3. [Dokumentacja techniczna](#dokumentacja-techniczna)
   - [Instalacja](#instalacja)
   - [Uruchomienie aplikacji](#uruchomienie-aplikacji)
   - [Analiza kodu wraz z opisem](#analiza-kodu-wraz-z-opisem)

# Wprowadzenie

Projekt ten to system ekspertowy umożliwiający rozpoznanie choroby na bazie odpowiedzi użytkownika na zadane pytania odnoszące się do powszechnych objawów chorobowych. Projekt jest stworzony z wykorzystaniem języka Python oraz biblioteki Experta, która bazuje na dedykowanym programie do systemów eksperckich jakim jest Clips.

# Sprawozdanie

## Cele i wymagania

1.  Program powinien zawierać zdefiniowaną listę objawów, która może być w łatwy sposób rozbudowywana.
2.  System, początkowo powinien mieć zdefiniowane kilka chorób (reguł), które będą odpowiednio nazwane i będą miały przypisane obawy.
3.  Objawy chorób będą podzielone na dwa rodzaje:
    - obowiązkowe - takie które muszą wystąpić, aby choroba została potwierdzona,
    - opcjonalne - takie które mogą wystąpić, ale nie muszą.
4.  Aplikacja będzie działała w wersji konsolowej - użytkownik będzie komunikował się przy użyciu wyświetlanego tekstu i wprowadzanych danych z użyciem klawiatury.
5.  Program powinien działać w pętli, aż użytkownik wpisze polecenie do zakończenia programu - po wyświetleniu diagnozy, powinna istnieć możliwość przeprowadzenia kolejnego wywiadu.
6.  System powinien informować użytkownika, że jego diagnoza lub jej brak, nie jest w 100% prawidłowy i stan zdrowia powinien być skonsultowany z lekarzem.

## Wykorzystane narzędzia

1. [Język programowania Python](https://www.python.org/)
   Python to język programowania wysokiego poziomu ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek standardowych, którego ideą przewodnią jest czytelność i klarowność kodu źródłowego. Jego składnia cechuje się przejrzystością i zwięzłością.
2. [Biblioteka Experta](https://experta.readthedocs.io/en/latest/introduction.html)
   Experta to Pythonowa alternatywa dla programu [CLIPS](https://www.clipsrules.net/), który jest dedykowany do tworzenia systemów eksperckich. Składa się z zestawu faktów z zestawem reguł do tych faktów i wykonywania pewnych działań na podstawie pasujące reguły, aby rozwiązać określony problem.

## Zobrazowanie działania aplikacji

1. Widok po uruchomieniu systemu.

Aplikacja ukazuje powitalne zdanie, które określa, do czego została stworzona i w jaki sposób będzie odbywał się proces zbierania informacji.

<img src="https://github.com/Majkel97/Expert-system-Diagnosis-of-diseases/blob/main/img/docs/zobrazowanie_1.png?raw=true"  width="800px" height="auto">

2. Widok zbierania informacji od użytkownika z walidacją wprowadzanych danych.

Aplikacja iteruje po wszystkich zdefiniowanych symptomach i zbiera odpowiedzi od użytkownika. Pacjent może wprowadzić tylko odpowiedzi "**tak**" lub "**nie**" (bez znaczenia, jaką zastosuje wielkość znaków). W przypadku wprowadzenia błędnej odpowiedzi, program poprosi użytkownika o podanie poprawnej.

<img src="https://github.com/Majkel97/Expert-system-Diagnosis-of-diseases/blob/main/img/docs/zobrazowanie_2.png?raw=true"  width="800px" height="auto">

3. Widok zdiagnozowanej choroby / chorób po dokonaniu analizy wprowadzanych danych.

Po przeanalizowaniu wszystkich odpowiedzi, jeżeli system rozpozna jakąś chorobę, jej nazwa zostanie wyświetlona na ekranie. Ponadto zostanie przedstawiony komunikat, że program nie jest idealny i wszystkie zdiagnozowane choroby należy skonsultować z realnym lekarze. Na koniec wyświetlane jest pytanie, czy osoba chce użyć programu raz jeszcze.

<img src="https://github.com/Majkel97/Expert-system-Diagnosis-of-diseases/blob/main/img/docs/zobrazowanie_3.png?raw=true"  width="800px" height="auto">

4. Widok z informacją o braku rozpoznania choroby po dokonaniu analizy wprowadzanych danych.

Po przeanalizowaniu wszystkich odpowiedzi, jeżeli system nie rozpozna żadnej choroby, zostanie wyświetlony komunikat przedstawiony na poniższym zdjęciu. Ponadto wyświetlane jest pytanie, czy osoba chce użyć programu raz jeszcze.

<img src="https://github.com/Majkel97/Expert-system-Diagnosis-of-diseases/blob/main/img/docs/zobrazowanie_4.png?raw=true"  width="800px" height="auto">

## Podsumowanie

Projekt został wykonany zgodnie z założeniami zawartymi na początku dokumentu w rozdziale [Cele i wymagania](#cele-i-wymagania). Aplikacja na bazie potwierdzania pytań o objawy chorobowe, przedstawia użytkownikowi potencjale choroby, na jakie może cierpieć.

Projekt stanowi dobrą bazę do rozbudowania aplikacji o kolejne funkcjonalności, bazę znanych symptomów czy reguły definiujące choroby, które system będzie umiał rozpoznać.

# Dokumentacja techniczna

## Instalacja

1. Pobierz repozytorium z kodem i otwórz folder z projektem przy użyciu dowolnego IDE (na przykład Visual Studio Code).

2. Utwórz wirtualne środowisko i aktywuj je.

```bash
# Utworzenie środkowiska wirtualnego
python -m venv /path/to/new/virtual/environment
# Aktywacja środkowiska wirtualnego
.\env\Scripts\activate
```

3. Używając menedżera pakietów [pip](https://pip.pypa.io/en/stable/), zainstaluj wymagane biblioteki.

```bash
pip install -r requirements.txt
```

## Uruchomienie aplikacji

1. Aktywuj środowisko wirtualne.

```bash
# Aktywacja środkowiska wirtualnego
.\env\Scripts\activate
```

2. Przejdź do folderu, który zawiera plik main.py.
3. Uruchom aplikację używając poniższego polecenia :

```bash
python3 main.py
```

## Analiza kodu wraz z opisem

1. Definicja zmiennej tablicowej **SYMPTOMS**, która definiuje objawy chorobowe, które potrafi rozpoznać system ekspertowy.

```python
# Defined symptom list
SYMPTOMS = [
    "gorączka",
    "ból głowy",
    "ból mięśni",
    "dreszcze",
    "katar",
    "kaszel",
    "duszności",
    "osłabienie",
    "ból w klatce piersiowej",
    "częste oddawanie moczu",
    "niegasnące pragnienie",
    "utrata masy ciała",
    "powolne gojenie się ran",
    "częste infekcje",
    "podwyższone ciśnienie",
    "zawroty głowy",
    "kłopoty z widzeniem",
    "uczucie ucisku",
    "ból promieniujący do ramienia",
    "zasłabnięcia",
    "przewlekły kaszel",
    "świsty podczas oddychania",
    "częste infekcje górnych dróg oddechowych",
    "urazy złamania kości",
    "utrata wysokości",
    "zgarbiona postawa",
    "ból stawów",
    "obrzęk stawów",
    "silny ból głowy",
    "nadwrażlisość na światło, dźwiek lub zapach",
    "nudności",
    "wymioty",
    "zmęczenie",
    "krwioplucie",
]
```

2. Definicja klas do reprezentacji symptomów oraz chorób.

Kod definiuje klasę o nazwie **Symptom**, która dziedziczy z klasy **Fact**. Klasa może być używana do przechowywania i przedstawiania informacji o symptomach choroby jako obiektów w aplikacji.

```python
class Symptom(Fact):
    """
    A class representing a symptom object that inherits from the Fact class.
    This class can be used to store and represent information about symptoms
    as objects in an application. It contains no additional methods or attributes
    other than those present in its parent Fact class.
    """
    pass
```

Kod definiuje klasę o nazwie **Disease**, która dziedziczy z klasy **Fact**. Klasa może być używana do przechowywania i przedstawiania informacji o chorobach jako obiektów w aplikacji.

```python
class Disease(Fact):
    """
    A class representing a disease object that inherits from the Fact class.
    This class can be used to store and represent information about diseases
    as objects in an application. It contains no additional methods or attributes
    other than those present in its parent Fact class.
    """
    pass
```

3.  Definicja systemu eksperckiego zbudowanego na rolach i faktach.

Podany kod definiuje klasę o nazwie **DiagnosisEngine**, która dziedziczy z klasy **KnowledgeEngine**. Klasa ta reprezentuje system ekspercki, który wykorzystuje wnioskowanie oparte na regułach do diagnozowania chorób na podstawie przedstawionych objawów.

W przykładowym kodzie przedstawiono dwie metody, **diagnoza_grypa** i **diagnoza_rak_pluc**. Metody te określają warunki lub przesłanki, które muszą być spełnione, aby można było zdiagnozować określoną chorobę. Używając logiki w postaci operatorów **AND**, **OR** i **NOT** wraz z obiektami **Symptom**, zostały określone, czy pacjent może cierpieć na określoną chorobę.

Operator **AND** oznacza, że wszystkie warunki muszą być spełnione, aby choroba została zdiagnozowana, podczas gdy **OR** oznacza, że przynajmniej jeden warunek musi być spełniony. Operator **NOT** neguje warunek.

Ogólnie rzecz biorąc, ta klasa służy jako szablon do tworzenia dalszych funkcji silnika diagnostycznego, które mogą zawierać dodatkowe reguły dotyczące innych chorób. Ponadto **DiagnosisEngine** można rozszerzyć, aby obsługiwał bardziej złożone choroby lub kombinacje objawów.

```python
class DiagnosisEngine(KnowledgeEngine):
    """
    A class representing an expert system that uses rule-based reasoning to diagnose diseases based on
    the presented symptoms.

    This class inherits from the KnowledgeEngine class and contains multiple rules for different diseases.

    Methods:
    Multiple methods containing inference rules for diagnosing different diseases.
    """

    @Rule(
        AND(
            Symptom(name="gorączka"),
            Symptom(name="ból głowy"),
            Symptom(name="ból mięśni"),
            OR(Symptom(name="dreszcze"), NOT(Symptom(name="dreszcze"))),
            OR(Symptom(name="katar"), NOT(Symptom(name="katar"))),
            OR(Symptom(name="kaszel"), NOT(Symptom(name="kaszel"))),
        )
    )
    def diagnoza_grypa(self):
        self.declare(Disease(name="Grypę"))

	 ...

	 @Rule(
        AND(
            Symptom(name="kaszel"),
            Symptom(name="ból w klatce piersiowej"),
            OR(Symptom(name="zmęczenie"), NOT(Symptom(name="zmęczenie"))),
            OR(Symptom(name="duszności"), NOT(Symptom(name="duszności"))),
            OR(Symptom(name="krwioplucie"), NOT(Symptom(name="krwioplucie"))),
        )
    )
    def diagnoza_rak_pluc(self):
        self.declare(Disease(name="Raka płuc"))

```

4. Opis głównej pętli aplikacji do interakcji z uzytkownikiem oraz wyśiwetlania daignozy.

Program działa w nieskończonej pętli while, dzięki czemu użytkownik może wielokrotnie uruchamiać program, jeśli sobie tego życzy. Za każdym razem, gdy przechodzi pętlę, tworzona jest nowa instancja klasy **DiagnosisEngine**, konsola jest czyszczona, a następnie użytkownik jest proszony o udzielenie odpowiedzi na pytania dotyczące objawów.

W zagnieżdżonej pętli for i while każdy objaw na predefiniowanej liście o nazwie SYMPTOMS jest sprawdzany z użytkownikiem przez przeglądanie każdego elementu na liście w celu potwierdzenia, czy symptom jest obecny, czy nie. Jeśli użytkownik potwierdzi, że ma dany objaw, symptom jest deklarowany przy pomocy metody .declare() instancji obiektu DiagnosisEngine. Jeśli użytkownik zaprzeczy obecności symptomu, zagnieżdżona pętla zakończy działanie dla tego symptomu. Jeśli odpowiedź nie jest prawidłowa (tj. ani „TAK”, ani „NIE”), monit będzie się powtarzał, aż do otrzymania prawidłowej odpowiedzi.
Po określeniu wszystkich symptomów wywoływana jest metoda .run() instancji mechanizmu wnioskowania, aby aktywować określone wcześniej reguły deklaratywne i wyciągnąć wnioski.

Wszystkie zdiagnozowane choroby są przechowywane na liście o nazwie zdiagnozowane_choroby. W przypadku wykrycia jakiejkolwiek choroby jest ona drukowana jako ostateczna diagnoza wraz z komunikatem przypominającym użytkownikowi, że nie zastępuje porady lekarza. Jeśli nie zostanie zdiagnozowana żadna choroba, zostanie wyświetlony komunikat, że nie znaleziono pasującej choroby, a użytkownik powinien skonsultować się z lekarzem, aby uzyskać więcej informacji.

Program monituje również użytkownika o ponowne uruchomienie procesu i czyści konsolę na kolejną rundę, jeśli zdecyduje się to zrobić.

```python
while True:
    # Create an instance of the DiagnosisEngine class
    engine = DiagnosisEngine()

    # Reset the instance of the DiagnosisEngine class
    engine.reset()

    print(
        f"\nCześć, jestem Twoim wirutalnym asystentem i na podstawie podanych przez Ciebie objawów postaram się określić na jaką chorobę cierpisz.\n\nOdpowiedz proszę na następujące pytania:\n"
    )

    # Iterate through each symptom in the SYMPTOMS list
    for item in SYMPTOMS:
        # Keep looping until the user answers with "TAK" or "NIE"
        while True:
            confirmed_symptom = input(
                f"Czy występuje/ą u Ciebie takie objawy jak {item}? (TAK / NIE): "
            )
            # If user answers "TAK", declare the symptom using the Declare function of the engine.
            if confirmed_symptom.lower() == "tak":
                engine.declare(
                    Symptom(name=item),
                )
                break
            # If user answers "NIE", exit the loop for the current symptom
            elif confirmed_symptom.lower() == "nie":
                break
            # If user answers anything else, prompt them to enter a valid response
            else:
                print(f"Wprowadzono nie poprawną odpowiedź! Wpisz TAK lub NIE.")

    engine.run()

    # Loop over all facts in the engine and appends any diagnosed diseases to a list.
    diagnosed_diseases = []
    for disease in engine.facts.values():
        if isinstance(disease, Disease):
            diagnosed_diseases.append(disease["name"])

    # Check if any disease has been confirmed and print diagnosis
    if diagnosed_diseases:
        print(
            f"\nNa bazie informacji które posiadam, wprowadzone przez Ciebie objawy mogą oznaczać że cierpisz na:"
        )
        for item in diagnosed_diseases:
            print(f"- {item}")
        print(
            f"\nPamiętaj, że nie znam Twojej historii medycznej oraz nie mogłem przeprowadzić badania osobiście. Aby potwierdzić diagnozę skontaktuj się z Twoim lekarzem."
        )
    else:
        print(
            f"\nZgodnie z informajami które posiadam, Twoje objawy nie stwierdzją żadnej ze znanych mi chorób. W celu dokładniejszej diagnozy skontaktuj się z Twoim lekarzem."
        )

    # Ask the user if they want to use the system again
    retry = input(f"\nCzy chcesz użyć systemu raz jeszcze? (Wpiz TAK): ")

    # If the user wants to retry, clear the console and continue with the loop
    if retry.lower() == "tak":
        cls = lambda: os.system("cls")
        cls()
        continue
    # If the user does not want to retry, end program
    else:
        break
```
