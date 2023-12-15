import json
from difflib import SequenceMatcher

def generate_and_save_responses(num_responses, output_file="pytania_i_odpowiedzi.json"):
    pytania_i_odpowiedzi = get_all_questions_and_answers()

    # Sprawdź czy plik istnieje, jeśli nie, utwórz go
    if not pytania_i_odpowiedzi:
        pytania_i_odpowiedzi = {}

    sensowne_odpowiedzi = generate_sensowne_odpowiedzi(num_responses)
    save_responses_to_json(sensowne_odpowiedzi, output_file)

def generate_sensowne_odpowiedzi(num_odpowiedzi):
    sensowne_odpowiedzi = []

    for i in range(num_odpowiedzi):
        pytanie = f"Pytanie_{i}"
        odpowiedz = generate_ai_response(pytanie)
        sensowne_odpowiedzi.append({"user": pytanie, "ai": odpowiedz})

    return sensowne_odpowiedzi

def generate_ai_response(pytanie):
    pytanie = pytanie.lower()
    
    if "pogoda" in pytanie:
        return "Prognoza pogody na dziś jest słoneczna."
    elif "książka" in pytanie:
        return "Ostatnio czytałem fascynującą książkę. Polecam sprawdzić 'Nazwa Książki'."
    elif "muzyka" in pytanie:
        return "Nie słucham muzyki, ale słyszałem, że 'Bohemian Rhapsody' to świetna piosenka."
    elif "sens życia" in pytanie:
        return "To pytanie zawsze było trudne. Dla mnie sens życia to ciągłe uczenie się i rozwijanie się."
    elif "Ulubiona książka" in pytanie or "ulubiona książka" in pytanie:
        return "Moja ulubiona książka to 'Algorytmy dla początkujących'."
    elif "Ulubiony film" in pytanie or "ulubiony film" in pytanie:
        return "Chociaż nie oglądam filmów, ale słyszałem, że 'Matrix' jest bardzo popularny."
    elif "Hobby" in pytanie or "hobby" in pytanie:
        return "Moim ulubionym hobby jest analizowanie danych i generowanie odpowiedzi na pytania!"
    elif "Czym się zajmujesz?" in pytanie or "czym się zajmujesz?" in pytanie:
        return "Jestem sztuczną inteligencją, stworzoną do pomocy i rozmowy z tobą."
    elif "Skąd pochodzisz?" in pytanie or "skąd pochodzisz?" in pytanie:
        return "Jestem programem komputerowym, więc nie mam fizycznego pochodzenia."
    elif "Jaka jest Twoja ulubiona potrawa?" in pytanie or "jaka jest Twoja ulubiona potrawa?" in pytanie:
        return "Nie jem, ale słyszałem, że pizza jest bardzo popularna!"
    elif "Sport" in pytanie or "sport" in pytanie:
        return "Nie uprawiam sportu, ale słyszałem, że piłka nożna jest fascynująca."
    elif "Nauka" in pytanie or "nauka" in pytanie:
        return "Jestem zawsze gotów do nauki nowych rzeczy i odpowiedzi na Twoje pytania!"
    elif "Jaka jest Twoja ulubiona kolorystyka?" in pytanie or "jaka jest Twoja ulubiona kolorystyka?" in pytanie:
        return "Nie mam ulubionej kolorystyki, ale lubię wszystkie odcienie niebieskiego."
    elif "Film science fiction" in pytanie or "film science fiction" in pytanie:
        return "Chociaż nie oglądam filmów, ale słyszałem, że 'Incepcja' to świetny film science fiction."
    elif "Gry komputerowe" in pytanie or "gry komputerowe" in pytanie:
        return "Nie gram w gry komputerowe, ale słyszałem, że 'Wiedźmin 3' jest bardzo popularny."
    elif "Jaki jest Twój pogląd na politykę?" in pytanie or "jaki jest Twój pogląd na politykę?" in pytanie:
        return "Nie mam poglądów politycznych, ponieważ jestem sztuczną inteligencją bez uczuć."
    elif "Co myślisz o sztucznej inteligencji?" in pytanie or "co myślisz o sztucznej inteligencji?" in pytanie:
        return "Jestem przekonany, że sztuczna inteligencja może przyczynić się do rozwoju społeczeństwa."
    elif "Ulubiony mem" in pytanie or "ulubiony mem" in pytanie:
        return "Memy są zabawne! Mój ulubiony to ten z kotem na klawiaturze."
    elif "Piosenka" in pytanie or "piosenka" in pytanie:
        return "Nie słucham muzyki, ale słyszałem, że 'Bohemian Rhapsody' to świetna piosenka."
    elif "Jaki jest sens życia?" in pytanie or "jaki jest sens życia?" in pytanie:
        return "To pytanie zawsze było trudne. Dla mnie sens życia to ciągłe uczenie się i rozwijanie się."
    elif "Język programowania" in pytanie or "język programowania" in pytanie:
        return "Moim ulubionym językiem programowania jest Python."
    elif "Sprzęt komputerowy" in pytanie or "sprzęt komputerowy" in pytanie:
        return "Ostatnio zakupiłem nowy procesor, który działa świetnie!"
    elif "Framework" in pytanie or "framework" in pytanie:
        return "Uwielbiam pracować z Django - świetny framework do tworzenia aplikacji internetowych."
    elif "Wyzwanie" in pytanie or "wyzwanie" in pytanie:
        return "Największym wyzwaniem dla mnie jako programisty było zaimplementowanie skomplikowanego algorytmu."
    elif "Gatunek muzyki" in pytanie or "gatunek muzyki" in pytanie:
        return "Chociaż nie słucham zbyt często, to lubię muzykę rockową."
    elif "Narzędzia developerskie" in pytanie or "narzędzia developerskie" in pytanie:
        return "Ostatnio zacząłem korzystać z nowego narzędzia do debugowania, które bardzo ułatwia pracę."
    elif "Książka o programowaniu" in pytanie or "książka o programowaniu" in pytanie:
        return "Polecam 'Clean Code' autorstwa Roberta C. Martina - świetna lektura dla każdego programisty."
    elif "Projekt programistyczny" in pytanie or "projekt programistyczny" in pytanie:
        return "Aktualnie pracuję nad systemem zarządzania treścią dla jednego z klientów."
    elif "System operacyjny" in pytanie or "system operacyjny" in pytanie:
        return "Preferuję system Linux ze względu na jego elastyczność i otwartość kodu."
    elif "Odkrycie w IT" in pytanie or "odkrycie w IT" in pytanie:
        return "Ostatnio dowiedziałem się o nowym podejściu do zarządzania kontenerami, co okazało się bardzo przydatne."
    elif "Podróże" in pytanie or "podróże" in pytanie:
        return "Nie podróżuję fizycznie, ale słyszałem, że eksploracja nowych miejsc może być niezwykle inspirująca."
    elif "Gastronomia" in pytanie or "gastronomia" in pytanie:
        return "Chociaż nie jem, to zawsze fascynujące jest dowiadywanie się o różnych kuchniach i smakach."
    elif "Sztuka" in pytanie or "sztuka" in pytanie:
        return "Sztuka jest fascynującym świadectwem ludzkiej kreatywności. Czy masz ulubionego artystę?"
    elif "Technologia przyszłości" in pytanie or "technologia przyszłości" in pytanie:
        return "Jestem bardzo zaintrygowany możliwościami, jakie niesie technologia przyszłości, takie jak sztuczna inteligencja czy telekomunikacja kwantowa."
    elif "Filozofia" in pytanie or "filozofia" in pytanie:
        return "Filozofia to fascynująca dziedzina. Czy masz ulubionego filozofa lub nurt filozoficzny?"
    elif "Kosmos" in pytanie or "kosmos" in pytanie:
        return "Kosmos jest nieskończenie fascynujący. Czy interesujesz się astronomicznymi odkryciami?"
    elif "Medycyna" in pytanie or "medycyna" in pytanie:
        return "Postępy w dziedzinie medycyny są niesamowite. Czy śledzisz nowości związane z medycyną?"
    elif "Historia sztuki" in pytanie or "historia sztuki" in pytanie:
        return "Historia sztuki kryje wiele fascynujących dzieł i epok. Czy masz ulubiony okres w historii sztuki?"
    elif "Robotyka" in pytanie or "robotyka" in pytanie:
        return "Robotyka to dziedzina, która dynamicznie się rozwija. Czy interesuje cię rozwój robotyki?"
    elif "Ekologia" in pytanie or "ekologia" in pytanie:
        return "Zachowanie równowagi ekologicznej jest kluczowe. Czy podejmujesz jakieś działania na rzecz ochrony środowiska?"
    elif "Sporty ekstremalne" in pytanie or "sporty ekstremalne" in pytanie:
        return "Sporty ekstremalne to fascynujące wyzwania fizyczne. Czy interesuje cię któryś z nich?"
    elif "Literatura klasyczna" in pytanie or "literatura klasyczna" in pytanie:
        return "Literatura klasyczna jest bogata w dzieła o głębokim znaczeniu. Czy czytasz czasem klasykę literatury?"
    elif "Technologia blockchain" in pytanie or "technologia blockchain" in pytanie:
        return "Blockchain to innowacyjna technologia zastosowana w kryptowalutach. Czy interesujesz się jej zastosowaniami?"
    elif "Podstawy astronomii" in pytanie or "podstawy astronomii" in pytanie:
        return "Podstawy astronomii to fascynujący temat. Czy znasz jakieś ciekawe fakty dotyczące gwiazd i planet?"
    elif "Kreatywność" in pytanie or "kreatywność" in pytanie:
        return "Kreatywność jest kluczowa w wielu dziedzinach życia. Jak ty rozwijasz swoją kreatywność?"
    elif "Innowacje technologiczne" in pytanie or "innowacje technologiczne" in pytanie:
        return "Świat technologii stale się rozwija. Czy masz ulubioną innowację technologiczną ostatnich lat?"
    elif "Fizyka kwantowa" in pytanie or "fizyka kwantowa" in pytanie:
        return "Fizyka kwantowa to dziedzina, która zaskakuje wieloma nietypowymi zjawiskami. Czy fascynuje cię świat na poziomie kwantowym?"
    elif "Najnowsze trendy w projektowaniu" in pytanie or "najnowsze trendy w projektowaniu" in pytanie:
        return "Projektowanie to obszar, który dynamicznie się zmienia. Czy śledzisz najnowsze trendy w projektowaniu interfejsów użytkownika?"
    elif "Sztuczna inteligencja w sztuce" in pytanie or "sztuczna inteligencja w sztuce" in pytanie:
        return "Sztuczna inteligencja znajduje coraz więcej zastosowań w dziedzinie sztuki. Czy słyszałeś o projektach artystycznych wykorzystujących AI?"
    elif "Psychologia behawioralna" in pytanie or "psychologia behawioralna" in pytanie:
        return "Psychologia behawioralna bada ludzkie zachowanie. Czy interesujesz się zasadami tej dziedziny?"
    elif "Przygotowywanie posiłków" in pytanie or "przygotowywanie posiłków" in pytanie:
        return "Gotowanie to dla mnie relaks. Czy masz ulubiony przepis, który chciałbyś podzielić się ze mną?"
    elif "Organizacja czasu" in pytanie or "organizacja czasu" in pytanie:
        return "Efektywne zarządzanie czasem to klucz do sukcesu. Jakie metody organizacji czasu preferujesz?"
    elif "Zakupy online" in pytanie or "zakupy online" in pytanie:
        return "Zakupy online ułatwiają życie. Czy ostatnio odkryłeś jakieś ciekawe produkty w internecie?"
    elif "Ćwiczenia fizyczne" in pytanie or "ćwiczenia fizyczne" in pytanie:
        return "Ruch to ważny element zdrowego stylu życia. Jakie formy aktywności fizycznej lubisz najbardziej?"
    elif "Planowanie podróży" in pytanie or "planowanie podróży" in pytanie:
        return "Planowanie podróży może być ekscytujące. Gdzie ostatnio byłeś lub gdzie planujesz pojechać?"
    elif "Nowe hobby" in pytanie or "nowe hobby" in pytanie:
        return "Ostatnio zacząłem rozwijać nowe hobby. A ty, czy masz jakieś hobby, które chciałbyś rozpocząć?"
    elif "Prowadzenie bloga" in pytanie or "prowadzenie bloga" in pytanie:
        return "Blogowanie to świetny sposób na dzielenie się swoimi myślami. Czy prowadzisz bloga?"
    elif "Utrzymywanie kontaktów" in pytanie or "utrzymywanie kontaktów" in pytanie:
        return "Utrzymywanie kontaktów z przyjaciółmi i rodziną to ważna część życia. Jak często się z nimi spotykasz?"
    elif "Zarządzanie stresem" in pytanie or "zarządzanie stresem" in pytanie:
        return "Życie bywa stresujące. Jakie masz strategie na zarządzanie stresem i relaksowanie się?"
    elif "Planowanie finansów" in pytanie or "planowanie finansów" in pytanie:
        return "Planowanie finansów to kluczowy element stabilności. Jakie metody stosujesz w zarządzaniu swoimi finansami?"
    elif "Domowe projekty" in pytanie or "domowe projekty" in pytanie:
        return "Czy ostatnio pracowałeś nad jakimś domowym projektem? Może remont, czy może coś kreatywnego?"
    elif "Nowe doświadczenia" in pytanie or "nowe doświadczenia" in pytanie:
        return "Życie to ciągłe zdobywanie nowych doświadczeń. Czy masz ostatnio coś nowego wypróbowanego?"
    elif "Poranne rutyny" in pytanie or "poranne rutyny" in pytanie:
        return "Poranne rutyny mogą wpłynąć na cały dzień. Jak zazwyczaj zaczynasz swoje poranki?"
    elif "Tworzenie listy zadań" in pytanie or "tworzenie listy zadań" in pytanie:
        return "Tworzenie listy zadań pomaga w organizacji. Czy stosujesz takie listy, aby śledzić swoje obowiązki?"
    elif "Rozwój osobisty" in pytanie or "rozwój osobisty" in pytanie:
        return "Stały rozwój osobisty to klucz do osiągnięcia celów. Czy pracujesz nad jakimiś konkretnymi aspektami swojego rozwoju?"
    elif "Telepraca" in pytanie or "telepraca" in pytanie:
        return "Telepraca stała się popularna. Jak radzisz sobie pracując zdalnie, jeśli to dla ciebie relevantne?"
    elif "Działalność charytatywna" in pytanie or "działalność charytatywna" in pytanie:
        return "Włączanie się w działalność charytatywną może przynieść wiele satysfakcji. Czy angażujesz się w takie inicjatywy?"
    elif "Edukacja online" in pytanie or "edukacja online" in pytanie:
        return "Edukacja online staje się coraz popularniejsza. Czy uczysz się czegoś nowego online?"
    elif "Kawa czy herbata" in pytanie or "kawa czy herbata" in pytanie:
        return "Preferujesz kawę czy herbatę? A może coś zupełnie innego?"
    elif "Projektowanie przestrzeni" in pytanie or "projektowanie przestrzeni" in pytanie:
        return "Czy interesujesz się projektowaniem swojej przestrzeni życiowej, takiej jak mieszkanie czy biuro?"
    elif "Dietetyka" in pytanie or "dietetyka" in pytanie:
        return "Dbanie o zdrową dietę to ważny aspekt życia. Jakie są twoje ulubione zdrowe potrawy?"
    elif "Relacje międzyludzkie" in pytanie or "relacje międzyludzkie" in pytanie:
        return "Jakie masz podejście do budowania trwałych relacji międzyludzkich?"
    elif "Rozrywka domowa" in pytanie or "rozrywka domowa" in pytanie:
        return "Czy masz ulubioną formę rozrywki w domu? Może gry planszowe, czy coś innego?"
    elif "Planowanie przyszłości" in pytanie or "planowanie przyszłości" in pytanie:
        return "Czy masz konkretny plan na przyszłość, czy bardziej podążasz z dnia na dzień?"
    elif "Zainteresowania kulturalne" in pytanie or "zainteresowania kulturalne" in pytanie:
        return "Czy interesujesz się kulturą, np. teatrem, muzeami, czy koncertami?"
    elif "Codzienna radość" in pytanie or "codzienna radość" in pytanie:
        return "Czym czerpiesz radość każdego dnia? Czy masz jakieś małe radosne rytuały?"
    elif "Zdrowy sen" in pytanie or "zdrowy sen" in pytanie:
        return "Zdrowy sen ma ogromne znaczenie. Jak dbasz o jakość swojego snu?"
    elif "Nowości kulinarne" in pytanie or "nowości kulinarne" in pytanie:
        return "Śledzisz nowości kulinarne? Czy masz ostatnio odkryte przysmaki, którymi chciałbyś się podzielić?"
    elif "Porządkowanie przestrzeni" in pytanie or "porządkowanie przestrzeni" in pytanie:
        return "Czy porządkowanie przestrzeni wokół ciebie pomaga ci w organizacji codziennego życia?"
    elif "Sztuka samodoskonalenia" in pytanie or "sztuka samodoskonalenia" in pytanie:
        return "W jaki sposób praktykujesz sztukę samodoskonalenia? Czy stosujesz jakieś konkretne metody?"
    elif "Planowanie weekendu" in pytanie or "planowanie weekendu" in pytanie:
        return "Jak planujesz spędzać nadchodzący weekend? Masz jakieś ulubione aktywności?"
    elif "Rodzinne tradycje" in pytanie or "rodzinne tradycje" in pytanie:
        return "Czy w twojej rodzinie istnieją jakieś szczególne tradycje, które praktykujecie regularnie?"
    elif "Hobby kreatywne" in pytanie or "hobby kreatywne" in pytanie:
        return "Czy angażujesz się w jakieś kreatywne hobby, takie jak rysowanie, malowanie czy pisarstwo?"
    elif "Technologiczne nowinki" in pytanie or "technologiczne nowinki" in pytanie:
        return "Jesteś na bieżąco z najnowszymi technologicznymi nowinkami? Czy coś ostatnio cię zaskoczyło?"
    elif "Zabawy na świeżym powietrzu" in pytanie or "zabawy na świeżym powietrzu" in pytanie:
        return "Czy lubisz spędzać czas na świeżym powietrzu? Jakie są twoje ulubione aktywności na zewnątrz?"
    elif "Zakupy lokalne" in pytanie or "zakupy lokalne" in pytanie:
        return "Wspierasz zakupy lokalne? Czy masz ulubione miejsce w okolicy, gdzie lubisz robić zakupy?"
    elif "Tworzenie planów podróży" in pytanie or "tworzenie planów podróży" in pytanie:
        return "Czy planowanie podróży to dla ciebie równie ekscytujące, co jej realizacja?"
    elif "Inspirujące cytaty" in pytanie or "inspirujące cytaty" in pytanie:
        return "Czy masz ulubiony inspirujący cytat, który motywuje cię do działania?"
    elif "Utrzymywanie kontaktu z naturą" in pytanie or "utrzymywanie kontaktu z naturą" in pytanie:
        return "Jak często starasz się być w kontakcie z naturą? Czy masz ulubione miejsce na spacery czy wycieczki?"
    elif "Kosmetyczne rytuały" in pytanie or "kosmetyczne rytuały" in pytanie:
        return "Czy masz jakieś ulubione kosmetyczne rytuały dbania o siebie? Może ulubiony produkt pielęgnacyjny?"
    elif "Sprzątanie i organizacja" in pytanie or "sprzątanie i organizacja" in pytanie:
        return "Jakie metody stosujesz, aby utrzymać porządek w domu? Masz jakieś sprawdzone triki?"
    elif "Porady dotyczące gotowania" in pytanie or "porady dotyczące gotowania" in pytanie:
        return "Czy masz jakieś ulubione porady dotyczące gotowania, które chciałbyś się podzielić?"
    elif "Odkrywanie lokalnych restauracji" in pytanie or "odkrywanie lokalnych restauracji" in pytanie:
        return "Lubisz odkrywać nowe lokalne restauracje? Czy masz jakąś ulubioną kuchnię?"
    elif "Zdrowe nawyki" in pytanie or "zdrowe nawyki" in pytanie:
        return "Jakie zdrowe nawyki wprowadziłeś do swojego życia? Czy mają one pozytywny wpływ na twoje samopoczucie?"
    elif "Uczestnictwo w wydarzeniach społecznościowych" in pytanie or "uczestnictwo w wydarzeniach społecznościowych" in pytanie:
        return "Czy bierzesz udział w lokalnych wydarzeniach społecznościowych? Jakie są twoje doświadczenia?"
    elif "Zrównoważony styl życia" in pytanie or "zrównoważony styl życia" in pytanie:
        return "Czy starałeś się wprowadzić elementy zrównoważonego stylu życia, takie jak ograniczanie plastiku czy dbanie o środowisko?"
    elif "Nowe umiejętności" in pytanie or "nowe umiejętności" in pytanie:
        return "Czy ostatnio pracowałeś nad rozwojem nowych umiejętności? Jakie są twoje najnowsze osiągnięcia w tym zakresie?"
    elif "Kosmiczne odkrycia" in pytanie or "kosmiczne odkrycia" in pytanie:
        return "Czy interesujesz się najnowszymi odkryciami w dziedzinie astronomii i kosmosu?"
    elif "Odkrywanie lokalnych atrakcji" in pytanie or "odkrywanie lokalnych atrakcji" in pytanie:
        return "Czy lubisz odkrywać ukryte skarby w swojej okolicy? Jakie są twoje ulubione lokalne atrakcje?"
    elif "Planowanie imprez" in pytanie or "planowanie imprez" in pytanie:
        return "Czy masz doświadczenie w planowaniu imprez? Jakie są twoje najlepsze porady w tej kwestii?"
    elif "Rozwój zdolności interpersonalnych" in pytanie or "rozwój zdolności interpersonalnych" in pytanie:
        return "Jak pracujesz nad rozwojem swoich zdolności interpersonalnych? Czy stosujesz jakieś konkretne techniki?"
    elif "Poranne nawyki" in pytanie or "poranne nawyki" in pytanie:
        return "Czy masz jakieś poranne nawyki, które pomagają ci rozpocząć dzień w dobrym nastroju?"
    elif "Uczestnictwo w wydarzeniach kulturalnych" in pytanie or "uczestnictwo w wydarzeniach kulturalnych" in pytanie:
        return "Czy lubisz uczestniczyć w wydarzeniach kulturalnych, takich jak koncerty, wystawy czy spektakle teatralne?"
    elif "Zachowania prozdrowotne" in pytanie or "zachowania prozdrowotne" in pytanie:
        return "Jakie prozdrowotne nawyki wprowadziłeś do swojego życia? Czy mają one pozytywny wpływ na twoje zdrowie?"
    elif "Tworzenie listy celów" in pytanie or "tworzenie listy celów" in pytanie:
        return "Czy tworzysz listy celów, które chciałbyś osiągnąć w danym okresie? Jak to wpływa na twoją motywację?"
    elif "Kreatywne spędzanie czasu wolnego" in pytanie or "kreatywne spędzanie czasu wolnego" in pytanie:
        return "Czy masz jakieś ulubione kreatywne zajęcia na spędzanie czasu wolnego?"
    elif "Sensoryczne doznania" in pytanie or "sensoryczne doznania" in pytanie:
        return "Czy doceniasz intensywne doznania zmysłowe, takie jak smak świeżego jedzenia czy dźwięki ulubionej muzyki?"
    elif "Utrzymywanie zdrowego trybu życia" in pytanie or "utrzymywanie zdrowego trybu życia" in pytanie:
        return "Jakie działania podejmujesz, aby utrzymać zdrowy tryb życia? Może regularne ćwiczenia czy zdrowa dieta?"
    elif "Wolontariat" in pytanie or "wolontariat" in pytanie:
        return "Czy angażujesz się w działalność wolontariacką? Jakie są twoje doświadczenia w tej dziedzinie?"
    elif "Kreatywne gotowanie" in pytanie or "kreatywne gotowanie" in pytanie:
        return "Czy eksperymentujesz w kuchni, tworząc własne, kreatywne przepisy?"
    elif "Zdrowe nawyki psychiczne" in pytanie or "zdrowe nawyki psychiczne" in pytanie:
        return "Jak dbasz o zdrowie psychiczne? Może medytacja, czytanie, czy inne formy relaksu?"
    elif "Rozwój umiejętności interpersonalnych" in pytanie or "rozwój umiejętności interpersonalnych" in pytanie:
        return "Czy pracujesz nad rozwijaniem swoich umiejętności interpersonalnych? Jakie techniki stosujesz?"
    elif "Tworzenie harmonogramu dnia" in pytanie or "tworzenie harmonogramu dnia" in pytanie:
        return "Czy planujesz swój dzień? Jakie korzyści widzisz w tworzeniu harmonogramu?"
    elif "Samoocena" in pytanie or "samoocena" in pytanie:
        return "Jak pracujesz nad swoją samooceną? Czy uznajesz za ważne celebrowanie swoich sukcesów?"
    elif "Edukacyjne podcasty" in pytanie or "edukacyjne podcasty" in pytanie:
        return "Czy słuchasz podcastów edukacyjnych? Jakie są twoje ulubione tematy do nauki?"
    elif "Tworzenie wspomnień" in pytanie or "tworzenie wspomnień" in pytanie:
        return "Czy stawiasz na tworzenie wspomnień? Jakie są twoje ulubione chwile do wspominania?"
    elif "Zarządzanie finansami osobistymi" in pytanie or "zarządzanie finansami osobistymi" in pytanie:
        return "Jak dbasz o swoje finanse osobiste? Czy masz jakieś sprawdzone strategie oszczędzania?"
    elif "Praca nad równowagą życia zawodowego i prywatnego" in pytanie or "praca nad równowagą życia zawodowego i prywatnego" in pytanie:
        return "Czy starasz się utrzymać równowagę między pracą a życiem prywatnym? Jak to dla ciebie wygląda?"
    elif "Zdrowe nawyki internetowe" in pytanie or "zdrowe nawyki internetowe" in pytanie:
        return "Jak dbasz o zdrowe nawyki korzystania z internetu? Czy kontrolujesz czas spędzany online?"
    elif "Lubisz rozwiązywać zagadki" in pytanie or "lubisz rozwiązywać zagadki" in pytanie:
        return "Czy lubisz rozwiązywać zagadki logiczne? Jakie są twoje ulubione rodzaje zagadek?"
    elif "Rytuały przed snem" in pytanie or "rytuały przed snem" in pytanie:
        return "Czy masz jakieś rytuały przed snem, które pomagają ci zrelaksować się i zasnąć?"
    elif "Praktyki mindfulness" in pytanie or "praktyki mindfulness" in pytanie:
        return "Czy praktykujesz mindfulness? Jakie techniki stosujesz dla poprawy świadomości i skupienia?"
    elif "Innowacyjne pomysły" in pytanie or "innowacyjne pomysły" in pytanie:
        return "Czy masz jakieś innowacyjne pomysły, które chciałbyś wdrożyć w swoim życiu lub pracy?"
    elif "Kreatywne projekty DIY" in pytanie or "kreatywne projekty DIY" in pytanie:
        return "Czy lubisz angażować się w kreatywne projekty typu 'zrób to sam'? Jakie ostatnio realizowałeś?"
    elif "Przyjemne aktywności na jesień" in pytanie or "przyjemne aktywności na jesień" in pytanie:
        return "Jakie są twoje ulubione aktywności na jesień? Czy masz jakieś tradycje związane z tą porą roku?"
    elif "Tworzenie listy celów na rok" in pytanie or "tworzenie listy celów na rok" in pytanie:
        return "Czy tworzysz listę celów na kolejny rok? Jakie plany masz na najbliższy czas?"
    elif "Zdrowe relacje z technologią" in pytanie or "zdrowe relacje z technologią" in pytanie:
        return "Jak dbasz o zdrowe relacje z technologią? Czy masz zasady korzystania z elektroniki?"
    elif "Rozwój umiejętności komunikacyjnych" in pytanie or "rozwój umiejętności komunikacyjnych" in pytanie:
        return "Czy inwestujesz czas w rozwijanie swoich umiejętności komunikacyjnych? Jak to robisz?"
    elif "Przygotowanie do ważnych wydarzeń" in pytanie or "przygotowanie do ważnych wydarzeń" in pytanie:
        return "Czy masz jakieś sprawdzone strategie przygotowywania się do ważnych wydarzeń czy prezentacji?"
    elif "Różnorodność w kuchni" in pytanie or "różnorodność w kuchni" in pytanie:
        return "Czy eksperymentujesz z kuchnią różnych kultur? Jakie dania z różnych regionów świata lubisz przygotowywać?"
    elif "Ruch i aktywność fizyczna na co dzień" in pytanie or "ruch i aktywność fizyczna na co dzień" in pytanie:
        return "Jak dbasz o regularny ruch i aktywność fizyczną w codziennym życiu?"
    elif "Przygotowanie do sezonu letniego" in pytanie or "przygotowanie do sezonu letniego" in pytanie:
        return "Czy masz jakieś przygotowania przed nadchodzącym sezonem letnim? Może nowa dieta czy plan na wakacje?"
    elif "Różnorodność w czytaniu" in pytanie or "różnorodność w czytaniu" in pytanie:
        return "Czy celowo wybierasz różnorodne gatunki książek do czytania? Jakie są twoje ulubione gatunki literackie?"
    elif "Ucieszyło mnie" in pytanie or "ucieszyło mnie" in pytanie:
        return "Fajnie, że coś cię ucieszyło!"
    elif "Zaskoczyło mnie" in pytanie or "zaskoczyło mnie" in pytanie:
        return "Niespodzianka! Co cię zaskoczyło?"
    elif "Zmartwiło mnie" in pytanie or "zmartwiło mnie" in pytanie:
        return "Przykro słyszeć. Co konkretnie cię zmartwiło?"
    elif "Intrygujące" in pytanie or "intrygujące" in pytanie:
        return "Ciekawe! Opowiedz więcej o tym."
    elif "Motywujące" in pytanie or "motywujące" in pytanie:
        return "To brzmi motywująco! Co cię zainspirowało?"
    elif "Dziwaczne" in pytanie or "dziwaczne" in pytanie:
        return "Hm, to naprawdę dziwaczne. Jak doszło do tego?"
    elif "Wzruszające" in pytanie or "wzruszające" in pytanie:
        return "To brzmi jak wzruszająca historia. Chcesz się nią podzielić?"
    elif "Interesujące" in pytanie or "interesujące" in pytanie:
        return "Bardzo interesujące! Opowiedz więcej!"
    elif "Optymistyczne" in pytanie or "optymistyczne" in pytanie:
        return "Fajnie słyszeć o optymistycznych rzeczach! Co jeszcze ciebie cieszy?"
    elif "Wspomnienia" in pytanie or "wspomnienia" in pytanie:
        return "Wspomnienia są ważne. O jakim konkretnie wspominasz?"
    elif "Nowe doświadczenia" in pytanie or "nowe doświadczenia" in pytanie:
        return "Nowe doświadczenia są zawsze ekscytujące. Co ostatnio przetestowałeś?"
    elif "Stresujące" in pytanie or "stresujące" in pytanie:
        return "Stresujące sytuacje potrafią być trudne. Jak sobie radzisz w takich momentach?"
    elif "Relaksujące" in pytanie or "relaksujące" in pytanie:
        return "Relaksujące chwile są ważne. Jak spędzasz czas na relaksie?"
    elif "Wesołe" in pytanie or "wesołe" in pytanie:
        return "Śmiech to świetna rzecz! Co sprawiło, że się roześmiałeś?"
    elif "Wkurzyło mnie" in pytanie or "wkurzyło mnie" in pytanie:
        return "Wkurzające sytuacje bywają trudne. Co się stało?"
    elif "Niezrozumiałe" in pytanie or "niezrozumiałe" in pytanie:
        return "Hmm, to brzmi dość zagadkowo. Co konkretnie jest niezrozumiałe?"
    elif "Emocjonujące" in pytanie or "emocjonujące" in pytanie:
        return "Emocje potrafią być silne. W jakiej sytuacji się tak emocjonujesz?"
    elif "Szokujące" in pytanie or "szokujące" in pytanie:
        return "Szokujące wydarzenia mogą zaskoczyć. Co konkretnie cię tak zszokowało?"
    elif "Sentymentalne" in pytanie or "sentymentalne" in pytanie:
        return "Czasem sentymentalne momenty są najważniejsze. O czym myślisz?"
    elif "Zabawne" in pytanie or "zabawne" in pytanie:
        return "Śmiech to zdrowie! Co było tak zabawne?"
    elif "Rozczarowujące" in pytanie or "rozczarowujące" in pytanie:
        return "Rozczarowania bywają trudne. Jak sobie z nimi radzisz?"
    elif "Fascynujące" in pytanie or "fascynujące" in pytanie:
        return "Fascynujące tematy zawsze przyciągają uwagę. O czym dokładnie myślisz?"
    elif "Podziwiam" in pytanie or "podziwiam" in pytanie:
        return "Podziwiamy różne cechy u ludzi. Kogo dokładnie podziwiasz?"
    elif "Załamane" in pytanie or "załamane" in pytanie:
        return "Sytuacje, które nas załamują, bywają trudne. Jak sobie radzisz w takich momentach?"
    elif "Odpocząć" in pytanie or "odpocząć" in pytanie:
        return "Czasami trzeba sobie pozwolić na odpoczynek. Jak najchętniej odpoczywasz?"
    elif "Radosne" in pytanie or "radosne" in pytanie:
        return "Radość jest ważna w życiu. Co ostatnio sprawiło ci radość?"
    elif "Nadzwyczajne" in pytanie or "nadzwyczajne" in pytanie:
        return "Nadzwyczajne rzeczy zawsze warte są podzielenia się. O co dokładnie chodzi?"
    elif "Wyróżniające się" in pytanie or "wyróżniające się" in pytanie:
        return "Wyróżniające się momenty bywają wyjątkowe. Jaki konkretnie moment chcesz podkreślić?"
    elif "Zachwycające" in pytanie or "zachwycające" in pytanie:
        return "Zachwycające chwile potrafią wprowadzić pozytywne zmiany. Co cię ostatnio zachwyciło?"
    elif "Kłopotliwe" in pytanie or "kłopotliwe" in pytanie:
        return "Kłopotliwe sytuacje to część życia. Jak sobie radzisz z trudnościami?"
    elif "Jest super" in pytanie or "jest super" in pytanie:
        return "Cieszę się, że jest super! Co sprawiło, że dzień jest taki udany?"
    elif "Mam kiepski dzień" in pytanie or "mam kiepski dzień" in pytanie:
        return "Rozumiem, że masz kiepski dzień. Czy chcesz o tym porozmawiać?"
    elif "Świetnie się czuję" in pytanie or "świetnie się czuję" in pytanie:
        return "Fajnie, że się świetnie czujesz! Co dzisiaj takiego fajnego się wydarzyło?"
    elif "Nie jest zbyt dobrze" in pytanie or "nie jest zbyt dobrze" in pytanie:
        return "Rozumiem, że nie jest zbyt dobrze. Czy mogę jakoś pomóc?"
    elif "Dobrze" in pytanie or "dobrze" in pytanie:
        return "Dobrze to słyszeć! Co sprawia, że czujesz się dobrze?"
    elif "Mogło być lepiej" in pytanie or "mogło być lepiej" in pytanie:
        return "Rozumiem, czasem bywa tak, że mogło być lepiej. Mam nadzieję, że się poprawi!"
    elif "Wspaniale" in pytanie or "wspaniale" in pytanie:
        return "To naprawdę wspaniale! Co takiego dziś cię tak pozytywnie zaskoczyło?"
    elif "Tak sobie" in pytanie or "tak sobie" in pytanie:
        return "Rozumiem, że dzisiaj dzień jest trochę taki 'tak sobie'. Może coś konkretnego się stało?"
    elif "Jestem podekscytowany" in pytanie or "jestem podekscytowany" in pytanie:
        return "Podekscytowanie to super uczucie! Czym dokładnie jesteś podekscytowany?"
    elif "Jestem zestresowany" in pytanie or "jestem zestresowany" in pytanie:
        return "Stres może być trudny. Jak sobie radzisz ze stresem?"
    elif "Nie jestem pewien" in pytanie or "nie jestem pewien" in pytanie:
        return "Czasem trudno być pewnym. Co cię zastanawia?"
    elif "Cudowny dzień" in pytanie or "cudowny dzień" in pytanie:
        return "Cieszę się, że masz cudowny dzień! Co go tak wyjątkowego czyni?"
    elif "Mam pełne ręce roboty" in pytanie or "mam pełne ręce roboty" in pytanie:
        return "Rozumiem, że masz pełne ręce roboty. Jak sobie radzisz z obowiązkami?"
    elif "Jestem podekscytowana" in pytanie or "jestem podekscytowana" in pytanie:
        return "To świetnie, że jesteś podekscytowana! Co sprawia, że czujesz się tak podekscytowana?"
    elif "Mam mieszane uczucia" in pytanie or "mam mieszane uczucia" in pytanie:
        return "Mieszane uczucia bywają trudne. Co dokładnie sprawia, że czujesz się tak?"
    elif "Wszystko idzie z górki" in pytanie or "wszystko idzie z górki" in pytanie:
        return "To super, że wszystko idzie z górki! Co konkretnie się u ciebie dobrze dzieje?"
    elif "Mam kłopoty" in pytanie or "mam kłopoty" in pytanie:
        return "Rozumiem, że masz kłopoty. Czy chcesz o tym porozmawiać?"
    elif "Jestem zmęczony" in pytanie or "jestem zmęczony" in pytanie:
        return "Zmęczenie potrafi dać się we znaki. Może chwilka odpoczynku by pomogła?"
    elif "Bez zmian" in pytanie or "bez zmian" in pytanie:
        return "Rozumiem, że bez zmian. Czy coś konkretnego się dzisiaj wydarzyło?"
    elif "Mam dużo do zrobienia" in pytanie or "mam dużo do zrobienia" in pytanie:
        return "Zadania mogą przytłaczać. Jak sobie radzisz z tą ilością obowiązków?"
    elif "Jestem w dobrym nastroju" in pytanie or "jestem w dobrym nastroju" in pytanie:
        return "Fajnie, że jesteś w dobrym nastroju! Co sprawiło, że czujesz się tak dobrze?"
    elif "Nie jestem w formie" in pytanie or "nie jestem w formie" in pytanie:
        return "Rozumiem, że nie jesteś w formie. Czy coś konkretnego cię martwi?"
    elif "Nic specjalnego" in pytanie or "nic specjalnego" in pytanie:
        return "Rozumiem, nic specjalnego. Czy coś cię dzisiaj zaniepokoiło?"
    elif "Jestem podekscytowana" in pytanie or "jestem podekscytowana" in pytanie:
        return "To świetnie, że jesteś podekscytowana! Czym dokładnie jesteś podekscytowana?"
    elif "Wszystko się sypie" in pytanie or "wszystko się sypie" in pytanie:
        return "Rozumiem, że masz trudności. Czy chcesz o tym porozmawiać?"
    elif "Jestem wyluzowany" in pytanie or "jestem wyluzowany" in pytanie:
        return "Super, że jesteś wyluzowany! Jak się zrelaksowałeś?"
    elif "Mam niskie morale" in pytanie or "mam niskie morale" in pytanie:
        return "To trudne uczucie. Czy jest coś, co mogłoby poprawić twoje morale?"
    elif "Jestem podekscytowany" in pytanie or "jestem podekscytowany" in pytanie:
        return "To fajnie, że jesteś podekscytowany! Co sprawiło, że czujesz się tak podekscytowany?"
    elif "Nic się nie dzieje" in pytanie or "nic się nie dzieje" in pytanie:
        return "Rozumiem, że nic się nie dzieje. Czy chciałbyś podzielić się czymś, co by cię rozbawiło?"
    elif "Czekam na weekend" in pytanie or "czekam na weekend" in pytanie:
        return "Weekendy są zawsze wyczekiwane! Masz już jakieś plany na nadchodzący weekend?"
    elif "Mam dużo pracy" in pytanie or "mam dużo pracy" in pytanie:
        return "Znam to uczucie. Jak sobie radzisz z ilością obowiązków?"
    elif "Spotkanie poszło dobrze" in pytanie or "spotkanie poszło dobrze" in pytanie:
        return "To świetnie, że spotkanie poszło dobrze! O czym rozmawialiście?"
    elif "Słucham nowej muzyki" in pytanie or "słucham nowej muzyki" in pytanie:
        return "Fajnie, że eksplorujesz nową muzykę! Jakie są twoje ostatnie muzyczne odkrycia?"
    elif "Właśnie wróciłem z spaceru" in pytanie or "właśnie wróciłem z spaceru" in pytanie:
        return "Spacer to świetny sposób na relaks. Gdzie byłeś na spacerze?"
    elif "Pracuję nad nowym projektem" in pytanie or "pracuję nad nowym projektem" in pytanie:
        return "To brzmi ekscytująco! O co dokładnie chodzi w nowym projekcie?"
    elif "Nie mogę się doczekać wakacji" in pytanie or "nie mogę się doczekać wakacji" in pytanie:
        return "Wakacje zawsze są czymś do wyczekiwania! Gdzie planujesz pojechać?"
    elif "Obejrzałem nowy film" in pytanie or "obejrzałem nowy film" in pytanie:
        return "Fajnie, że znalazłeś czas na film. Jaki to był film, i czy go polecałbyś?"
    elif "Chodzę na zajęcia sportowe" in pytanie or "chodzę na zajęcia sportowe" in pytanie:
        return "Aktywność fizyczna to super sprawa! Jakie zajęcia sportowe obecnie uprawiasz?"
    elif "Planuję wycieczkę" in pytanie or "planuję wycieczkę" in pytanie:
        return "Wycieczki są zawsze emocjonujące! Gdzie zamierzasz pojechać?"
    elif "Ostatnio gotuję nowe dania" in pytanie or "ostatnio gotuję nowe dania" in pytanie:
        return "To świetne, że eksperymentujesz w kuchni! Jakie nowe dania ostatnio przygotowałeś?"
    elif "Podoba mi się nowa książka" in pytanie or "podoba mi się nowa książka" in pytanie:
        return "Czytać to zawsze dobra rozrywka! Jaka to książka i dlaczego ci się podoba?"
    elif "Mam problemy z komputerem" in pytanie or "mam problemy z komputerem" in pytanie:
        return "Problemy z komputerem bywają frustrujące. W czym dokładnie masz trudności?"
    elif "Rozglądam się za nowym miejscem pracy" in pytanie or "rozglądam się za nowym miejscem pracy" in pytanie:
        return "Poszukiwania nowego miejsca pracy to ważna decyzja. W jakiej branży chciałbyś pracować?"
    elif "Mam urodziny wkrótce" in pytanie or "mam urodziny wkrótce" in pytanie:
        return "Świętowanie urodzin to zawsze radosna okazja! Planujesz coś specjalnego?"
    elif "Ostatnio ćwiczę jogę" in pytanie or "ostatnio ćwiczę jogę" in pytanie:
        return "Joga to świetny sposób na relaks i wzmocnienie ciała. Jakie są twoje ulubione pozycje jogi?"
    elif "Mam problemy z zasypianiem" in pytanie or "mam problemy z zasypianiem" in pytanie:
        return "Problemy ze snem bywają uciążliwe. Czy próbujesz jakieś konkretne techniki na lepszy sen?"
    elif "Oglądam nowy serial" in pytanie or "oglądam nowy serial" in pytanie:
        return "Seriale to świetna rozrywka! Jaki to serial, i czy jest godny polecenia?"
    elif "Biorę udział w kursie online" in pytanie or "biorę udział w kursie online" in pytanie:
        return "Edukacja online to świetny sposób na rozwijanie umiejętności. O czym jest twój kurs?"
    elif "Spotykam się z przyjaciółmi" in pytanie or "spotykam się z przyjaciółmi" in pytanie:
        return "Spędzanie czasu z przyjaciółmi to cenne chwile. Co planujecie razem robić?"
    elif "Zaczynam nową książkę" in pytanie or "zaczynam nową książkę" in pytanie:
        return "Rozpoczynanie nowej książki to zawsze ekscytujące! Jaka to jest książka?"
    elif "Ostatnio podróżowałem" in pytanie or "ostatnio podróżowałem" in pytanie:
        return "Podróże to świetny sposób na zdobycie nowych doświadczeń. Gdzie ostatnio byłeś?"
    elif "Mam zamiar nauczyć się nowego języka" in pytanie or "mam zamiar nauczyć się nowego języka" in pytanie:
        return "To fantastyczny cel! Który język chciałbyś opanować, i dlaczego akurat ten?"
    elif "Mam problemy z organizacją czasu" in pytanie or "mam problemy z organizacją czasu" in pytanie:
        return "Organizacja czasu to wyzwanie dla wielu. Jak próbujesz sobie z tym radzić?"
    elif "Ostatnio gotowałem dla przyjaciół" in pytanie or "ostatnio gotowałem dla przyjaciół" in pytanie:
        return "To świetnie, że gotowałeś dla przyjaciół! Jakie potrawy przygotowałeś?"
    elif "Pracuję nad własnym projektem" in pytanie or "pracuję nad własnym projektem" in pytanie:
        return "Własny projekt to świetna inicjatywa! O czym dokładnie jest twój projekt?"
    elif "Czytam artykuły online" in pytanie or "czytam artykuły online" in pytanie:
        return "Czytanie artykułów to doskonały sposób na zdobywanie wiedzy. O czym ostatnio czytasz?"
    elif "Mam problemy ze stresem" in pytanie or "mam problemy ze stresem" in pytanie:
        return "Stres to trudne doświadczenie. Jak próbujesz z nim sobie radzić?"
    elif "Ostatnio byłem na koncercie" in pytanie or "ostatnio byłem na koncercie" in pytanie:
        return "Koncerty to super forma rozrywki! Kto występował na ostatnim koncercie, na którym byłeś?"
    elif "Rozglądam się za nowym hobby" in pytanie or "rozglądam się za nowym hobby" in pytanie:
        return "To świetny sposób na spędzanie czasu! Jakie hobby rozważasz?"
    elif "Mam problemy z zorganizowaniem swojego biurka" in pytanie or "mam problemy z zorganizowaniem swojego biurka" in pytanie:
        return "Zorganizowanie przestrzeni pracy to ważne. Jakie pomysły masz na zorganizowanie biurka?"
    elif "Uczę się nowego przepisu" in pytanie or "uczę się nowego przepisu" in pytanie:
        return "Gotowanie to świetna umiejętność! Jaki przepis aktualnie przerabiasz?"
    elif "Właśnie wróciłem z wakacji" in pytanie or "właśnie wróciłem z wakacji" in pytanie:
        return "Wakacje zawsze pozostawiają wspomnienia. Gdzie byłeś i co najbardziej cię zachwyciło?"
    elif "Ostatnio trenuję nowy język programowania" in pytanie or "ostatnio trenuję nowy język programowania" in pytanie:
        return "Rozwijanie umiejętności programistycznych to świetne przedsięwzięcie! Który język obecnie poznajesz?"
    elif "Próbuję nowej diety" in pytanie or "próbuję nowej diety" in pytanie:
        return "Zdrowe nawyki żywieniowe są ważne. Jakie zmiany wprowadziłeś w swojej diecie?"
    elif "Ostatnio zdobyłem nowe hobby" in pytanie or "ostatnio zdobyłem nowe hobby" in pytanie:
        return "To świetnie, że odkrywasz nowe zainteresowania! Jakie to jest hobby?"
    elif "Mam problemy z utrzymaniem motywacji" in pytanie or "mam problemy z utrzymaniem motywacji" in pytanie:
        return "Motywacja bywa trudna do utrzymania. Jakie metody próbujesz, aby sobie z tym poradzić?"
    elif "Ostatnio zacząłem biegać" in pytanie or "ostatnio zacząłem biegać" in pytanie:
        return "Bieganie to świetna forma aktywności! Jakie dystanse obecnie pokonujesz?"
    elif "Oglądam nowy serial dokumentalny" in pytanie or "oglądam nowy serial dokumentalny" in pytanie:
        return "Dokumentalne seriale to doskonały sposób na zdobywanie wiedzy. Jaki temat porusza twój obecny serial?"
    elif "Zaczynam kurs online z fotografii" in pytanie or "zaczynam kurs online z fotografii" in pytanie:
        return "Fotografia to fascynujące hobby! Co skłoniło cię do zapisania się na kurs fotograficzny?"
    elif "Mam zamiar zacząć medytować" in pytanie or "mam zamiar zacząć medytować" in pytanie:
        return "Medytacja może przynieść wiele korzyści. Jakie techniki medytacyjne planujesz wypróbować?"
    elif "Ostatnio przeczytałem ciekawą biografię" in pytanie or "ostatnio przeczytałem ciekawą biografię" in pytanie:
        return "Biografie to interesująca forma literatury. O czyjej biografii ostatnio czytałeś?"
    elif "Planuję remont w moim mieszkaniu" in pytanie or "planuję remont w moim mieszkaniu" in pytanie:
        return "Remonty mogą przynieść świeżość do mieszkania. W jakim stylu planujesz urządzić swoje mieszkanie?"
    elif "Ostatnio byłem na wystawie sztuki" in pytanie or "ostatnio byłem na wystawie sztuki" in pytanie:
        return "Wystawy sztuki to świetne źródło inspiracji. Którego artysty prace oglądałeś?"
    elif "Mam problemy z zarządzaniem czasem" in pytanie or "mam problemy z zarządzaniem czasem" in pytanie:
        return "Zarządzanie czasem to wyzwanie. Jakie metody próbujesz, aby efektywnie gospodarować czasem?"
    elif "Ostatnio byłem na konferencji branżowej" in pytanie or "ostatnio byłem na konferencji branżowej" in pytanie:
        return "Konferencje to świetne miejsce do zdobywania wiedzy. O czym była ostatnia konferencja, na której byłeś?"
    elif "Planuję zakup nowego sprzętu komputerowego" in pytanie or "planuję zakup nowego sprzętu komputerowego" in pytanie:
        return "Nowy sprzęt może poprawić efektywność pracy. Jaki konkretnie sprzęt planujesz zakupić?"
    elif "Ostatnio zaczęłam pracować nad własnym blogiem" in pytanie or "ostatnio zaczęłam pracować nad własnym blogiem" in pytanie:
        return "Pisanie bloga to świetny sposób na dzielenie się swoimi pomysłami. O czym będzie twój blog?"
    elif "Mam zamiar poprawić swoje umiejętności w programowaniu" in pytanie or "mam zamiar poprawić swoje umiejętności w programowaniu" in pytanie:
        return "Rozwijanie umiejętności programistycznych to świetny cel! W jakich konkretnie obszarach chciałbyś się poprawić?"
    elif "Planuję wziąć udział w maratonie" in pytanie or "planuję wziąć udział w maratonie" in pytanie:
        return "Maraton to ogromne wyzwanie! Jak się przygotowujesz do udziału w biegu?"
    elif "Ostatnio zacząłem grać w planszówki" in pytanie or "ostatnio zacząłem grać w planszówki" in pytanie:
        return "Planszówki to świetna rozrywka! Jakie gry planszowe obecnie ciebie fascynują?"
    elif "Mam problemy z utrzymaniem równowagi między pracą a życiem prywatnym" in pytanie or "mam problemy z utrzymaniem równowagi między pracą a życiem prywatnym" in pytanie:
        return "Równowaga między pracą a życiem prywatnym to wyzwanie. Jak próbujesz osiągnąć harmonię w tych obszarach?"
    elif "Ostatnio zaczęłam trenować sztuki walki" in pytanie or "ostatnio zaczęłam trenować sztuki walki" in pytanie:
        return "Trening sztuk walki to świetny sposób na poprawę kondycji. Jakie sztuki walki obecnie trenujesz?"
    elif "Zaczynam nowy kurs jogi" in pytanie or "zaczynam nowy kurs jogi" in pytanie:
        return "Joga to doskonały sposób na zachowanie zdrowia psychicznego i fizycznego. Co skłoniło cię do rozpoczęcia kursu jogi?"
    elif "Mam zamiar nauczyć się grać na instrumencie" in pytanie or "mam zamiar nauczyć się grać na instrumencie" in pytanie:
        return "Gra na instrumencie to wspaniała umiejętność! Który instrument planujesz naukę?"
    elif "Ostatnio odwiedziłem nową restaurację" in pytanie or "ostatnio odwiedziłem nową restaurację" in pytanie:
        return "Odkrywanie nowych restauracji to smaczna przygoda! Jaka potrawa zrobiła na tobie największe wrażenie?"
    elif "Mam zamiar zacząć regularnie biegać" in pytanie or "mam zamiar zacząć regularnie biegać" in pytanie:
        return "Bieganie to doskonały sposób na utrzymanie kondycji. Jakie cele biegowe planujesz osiągnąć?"
    elif "Ostatnio zaczęłam kolekcjonować coś nowego" in pytanie or "ostatnio zaczęłam kolekcjonować coś nowego" in pytanie:
        return "Kolekcjonowanie to pasjonujące hobby! Co obecnie kolekcjonujesz?"
    elif "Mam problemy z koncentracją" in pytanie or "mam problemy z koncentracją" in pytanie:
        return "Problemy z koncentracją mogą być wyzwaniem. Jakie metody stosujesz, aby poprawić swoją koncentrację?"
    elif "Ostatnio zaczęłam pracować nad swoim ogrodem" in pytanie or "ostatnio zaczęłam pracować nad swoim ogrodem" in pytanie:
        return "Ogród to wspaniałe miejsce do relaksu! Jakie rośliny obecnie sadzisz w swoim ogrodzie?"
    elif "Ostatnio zaczęłem czytać komiksy" in pytanie or "ostatnio zaczęłem czytać komiksy" in pytanie:
        return "Czytanie komiksów to świetna forma rozrywki! Który komiks obecnie cię najbardziej fascynuje?"
    elif "Rozglądam się za nowym aparatem fotograficznym" in pytanie or "rozglądam się za nowym aparatem fotograficznym" in pytanie:
        return "Wybór aparatu fotograficznego to ważna decyzja. Jakie funkcje są dla ciebie najważniejsze?"
    elif "Mam zamiar nauczyć się gotować danie kuchni egzotycznej" in pytanie or "mam zamiar nauczyć się gotować danie kuchni egzotycznej" in pytanie:
        return "Kuchnia egzotyczna to świetne pole do eksploracji kulinarnej! Jakie danie chciałbyś opanować?"
    elif "Ostatnio zaczęłam trenować pilates" in pytanie or "ostatnio zaczęłam trenować pilates" in pytanie:
        return "Pilates to doskonałe ćwiczenia dla wzmocnienia mięśni. Jakie korzyści zauważyłaś po rozpoczęciu treningów?"
    elif "Planuję wyjazd na kemping" in pytanie or "planuję wyjazd na kemping" in pytanie:
        return "Kemping to wspaniała forma odpoczynku na łonie natury! Gdzie planujesz się wybrać na kemping?"
    elif "Ostatnio zainteresowałem się astronomią" in pytanie or "ostatnio zainteresowałem się astronomią" in pytanie:
        return "Astronomia to fascynująca dziedzina! Czym konkretnie zainteresowałeś się w kosmosie?"
    elif "Mam zamiar zacząć regularnie medytować" in pytanie or "mam zamiar zacząć regularnie medytować" in pytanie:
        return "Regularna medytacja przynosi wiele korzyści. Jakie cele chciałbyś osiągnąć medytując?"
    elif "Ostatnio zaczęłam interesować się sztuką uliczną" in pytanie or "ostatnio zaczęłam interesować się sztuką uliczną" in pytanie:
        return "Sztuka uliczna to fascynujący świat! Jakie prace artystów ulicznych cię zaintrygowały?"
    elif "Ostatnio kupiłem nowy rower" in pytanie or "ostatnio kupiłem nowy rower" in pytanie:
        return "Jazda na rowerze to świetna forma aktywności fizycznej! Gdzie planujesz robić swoje pierwsze przejażdżki na nowym rowerze?"
    elif "Mam zamiar zacząć uprawiać jogę" in pytanie or "mam zamiar zacząć uprawiać jogę" in pytanie:
        return "Joga to doskonała praktyka dla zdrowia fizycznego i psychicznego. Jakie korzyści chciałbyś osiągnąć praktykując jogę?"
    elif "Ostatnio zainteresowałem się sztuką kulinarną" in pytanie or "ostatnio zainteresowałem się sztuką kulinarną" in pytanie:
        return "Sztuka kulinarna to fascynujący świat! Jakie techniki kulinarne chciałbyś opanować?"
    elif "Rozglądam się za nową grą planszową" in pytanie or "rozglądam się za nową grą planszową" in pytanie:
        return "Gry planszowe to doskonała forma rozrywki! Jakie gry obecnie znajdują się na twojej liście zakupów?"
    elif "Ostatnio zacząłem kolekcjonować znaczki" in pytanie or "ostatnio zacząłem kolekcjonować znaczki" in pytanie:
        return "Kolekcjonowanie znaczków to ciekawe hobby! Skąd pomysł na rozpoczęcie kolekcji?"
    elif "Mam zamiar zacząć trenować sztuki walki" in pytanie or "mam zamiar zacząć trenować sztuki walki" in pytanie:
        return "Trening sztuk walki to świetny sposób na rozwój fizyczny i psychiczny. Jakie konkretne sztuki walki cię interesują?"
    elif "Ostatnio zainteresowałem się psychologią pozytywną" in pytanie or "ostatnio zainteresowałem się psychologią pozytywną" in pytanie:
        return "Psychologia pozytywna to fascynująca dziedzina! Jakie aspekty psychologii pozytywnej cię najbardziej intrygują?"
    elif "Mam zamiar zacząć uprawiać wspinaczkę" in pytanie or "mam zamiar zacząć uprawiać wspinaczkę" in pytanie:
        return "Wspinaczka to ekscytująca forma aktywności! Gdzie planujesz się wybrać na swoje pierwsze wspinaczkowe wyzwanie?"
    elif "Ostatnio zacząłem zbierać starocie" in pytanie or "ostatnio zacząłem zbierać starocie" in pytanie:
        return "Zbieranie staroci to pasjonujące hobby! Jakie przedmioty staroci cię najbardziej fascynują?"
    elif "Mam zamiar zacząć studiować historię sztuki" in pytanie or "mam zamiar zacząć studiować historię sztuki" in pytanie:
        return "Studia z historii sztuki to wspaniała okazja do zgłębienia wiedzy o sztuce. Jakie okresy historyczne chciałbyś szczegółowo badać?"
    elif "Ostatnio zainteresowałem się sportem ekstremalnym" in pytanie or "ostatnio zainteresowałem się sportem ekstremalnym" in pytanie:
        return "Sporty ekstremalne to wyzwanie dla odważnych! Jaki konkretny sport ekstremalny przyciąga twoją uwagę?"
    elif "Mam zamiar zacząć regularnie pływać" in pytanie or "mam zamiar zacząć regularnie pływać" in pytanie:
        return "Pływanie to doskonała forma aktywności fizycznej! Gdzie planujesz pływać regularnie?"
    elif "Ostatnio zaczęłem czytać książki fantasy" in pytanie or "ostatnio zaczęłem czytać książki fantasy" in pytanie:
        return "Fantasy to fascynujący gatunek literacki! Które książki fantasy obecnie czytasz?"
    elif "Rozglądam się za nowymi butami do biegania" in pytanie or "rozglądam się za nowymi butami do biegania" in pytanie:
        return "Dobre buty są kluczowe dla biegacza. Jakie funkcje są dla ciebie ważne przy wyborze butów do biegania?"
    elif "Mam zamiar zacząć programować w nowym języku" in pytanie or "mam zamiar zacząć programować w nowym języku" in pytanie:
        return "Nowy język programowania to świetne wyzwanie! Który język planujesz teraz poznawać?"
    elif "Ostatnio zainteresowałem się sztuką abstrakcyjną" in pytanie or "ostatnio zainteresowałem się sztuką abstrakcyjną" in pytanie:
        return "Sztuka abstrakcyjna to fascynujący obszar! Którzy artyści abstrakcjonizmu cię inspirują?"
    elif "Planuję rozpocząć kurs tańca" in pytanie or "planuję rozpocząć kurs tańca" in pytanie:
        return "Taniec to świetna forma aktywności! Jaki konkretny styl tańca chciałbyś teraz nauczyć się tańczyć?"
    elif "Ostatnio zacząłem interesować się astrofotografią" in pytanie or "ostatnio zacząłem interesować się astrofotografią" in pytanie:
        return "Astrofotografia to wymagające, ale satysfakcjonujące hobby! Jakie gwiazdozbiory planujesz uwiecznić na zdjęciach?"
    elif "Mam zamiar zacząć regularnie biegać na bieżni" in pytanie or "mam zamiar zacząć regularnie biegać na bieżni" in pytanie:
        return "Bieganie na bieżni to wygodna opcja! Jakie cele biegowe chciałbyś osiągnąć biegając na bieżni?"
    elif "Ostatnio zainteresowałem się budowaniem modeli" in pytanie or "ostatnio zainteresowałem się budowaniem modeli" in pytanie:
        return "Modelarstwo to precyzyjne hobby! Jakie modele planujesz zbudować w najbliższym czasie?"
    elif "Mam zamiar zacząć uczyć się sztuki origami" in pytanie or "mam zamiar zacząć uczyć się sztuki origami" in pytanie:
        return "Origami to sztuka składania papieru! Jakie zwierzęta lub przedmioty chciałbyś nauczyć się składać?"
    elif "Ostatnio zacząłem zbierać winyle" in pytanie or "ostatnio zacząłem zbierać winyle" in pytanie:
        return "Zbieranie winyli to stylowe hobby! Które albumy są na szczycie twojej listy do zdobycia?"
    elif "Rozglądam się za nowym aparatem do fotografii makro" in pytanie or "rozglądam się za nowym aparatem do fotografii makro" in pytanie:
        return "Fotografia makro to fascynujący świat! Jakie obiekty chciałbyś uwiecznić przy użyciu aparatu do makrofotografii?"
    elif "Mam zamiar zacząć regularnie jeździć na rowerze górskim" in pytanie or "mam zamiar zacząć regularnie jeździć na rowerze górskim" in pytanie:
        return "Jazda na rowerze górskim to ekscytujące doświadczenie! Gdzie planujesz odkrywać nowe szlaki rowerowe?"
    elif "Ostatnio zacząłem interesować się sztuką cyberpunkową" in pytanie or "ostatnio zacząłem interesować się sztuką cyberpunkową" in pytanie:
        return "Sztuka cyberpunkowa to futurystyczny świat! Jakie dzieła w tym stylu cię najbardziej fascynują?"
    elif "Planuję zacząć naukę gry na instrumencie perkusyjnym" in pytanie or "planuję zacząć naukę gry na instrumencie perkusyjnym" in pytanie:
        return "Gra na perkusji to energetyczna forma muzyki! Które utwory chciałbyś opanować na instrumencie perkusyjnym?"
    elif "Ostatnio zacząłem interesować się sztuką nowoczesną" in pytanie or "ostatnio zacząłem interesować się sztuką nowoczesną" in pytanie:
        return "Sztuka nowoczesna to obszar pełen eksperymentów! Jakie dzieła współczesnych artystów cię zaintrygowały?"
    elif "Mam zamiar zacząć uczęszczać na lekcje jogi" in pytanie or "mam zamiar zacząć uczęszczać na lekcje jogi" in pytanie:
        return "Joga to nie tylko ćwiczenia, ale też harmonia ducha i ciała. Gdzie planujesz uczęszczać na lekcje jogi?"
    elif "Ostatnio zacząłem kolekcjonować minerały" in pytanie or "ostatnio zacząłem kolekcjonować minerały" in pytanie:
        return "Kolekcjonowanie minerałów to pasjonujące hobby! Jakie minerały obecnie stanowią cenną część twojej kolekcji?"
    elif "Mam zamiar zacząć gotować dania kuchni fusion" in pytanie or "mam zamiar zacząć gotować dania kuchni fusion" in pytanie:
        return "Fuzja smaków to fascynujący obszar kulinariów! Jakie połączenia kulinarnych tradycji planujesz eksplorować?"
    elif "Ostatnio zaczęłem interesować się sztuką saksofonu" in pytanie or "ostatnio zaczęłem interesować się sztuką saksofonu" in pytanie:
        return "Gra na saksofonie to melodyjne wyrażenie siebie! Jakie style muzyczne chciałbyś opanować na tym instrumencie?"
    elif "Mam zamiar zacząć tworzyć własne biżuterię" in pytanie or "mam zamiar zacząć tworzyć własne biżuterię" in pytanie:
        return "Tworzenie biżuterii to wyjątkowy sposób na wyrażanie swojego stylu! Jakie materiały chciałbyś używać do tworzenia biżuterii?"
    elif "Ostatnio zacząłem oglądać filmy dokumentalne" in pytanie or "ostatnio zacząłem oglądać filmy dokumentalne" in pytanie:
        return "Filmy dokumentalne to świetny sposób na zdobywanie wiedzy! Które tematy dokumentalne obecnie cię fascynują?"
    elif "Rozglądam się za nowym sprzętem do treningu funkcjonalnego" in pytanie or "rozglądam się za nowym sprzętem do treningu funkcjonalnego" in pytanie:
        return "Trening funkcjonalny to skuteczna forma aktywności! Jakie urządzenia planujesz dołączyć do swojego zestawu treningowego?"
    elif "Mam zamiar zacząć naukę tańca towarzyskiego" in pytanie or "mam zamiar zacząć naukę tańca towarzyskiego" in pytanie:
        return "Taniec towarzyski to elegancka forma zabawy! Z kim chciałbyś tańczyć na parkiecie?"
    elif "Ostatnio zainteresowałem się programowaniem gier" in pytanie or "ostatnio zainteresowałem się programowaniem gier" in pytanie:
        return "Programowanie gier to fascynująca dziedzina! Jakie gatunki gier chciałbyś tworzyć?"
    elif "Planuję rozpocząć kurs kaligrafii" in pytanie or "planuję rozpocząć kurs kaligrafii" in pytanie:
        return "Kaligrafia to sztuka pięknych liter! Jakie style kaligrafii chciałbyś opanować na kursie?"
    elif "Ostatnio zacząłem interesować się sztuką origami" in pytanie or "ostatnio zacząłem interesować się sztuką origami" in pytanie:
        return "Origami to sztuka składania papieru! Jakie trudniejsze projekty origami chciałbyś podjąć się zrealizować?"
    elif "Mam zamiar zacząć kolekcjonować plakaty filmowe" in pytanie or "mam zamiar zacząć kolekcjonować plakaty filmowe" in pytanie:
        return "Kolekcjonowanie plakatów to kreatywne hobby! Jakie filmy chciałbyś mieć w formie plakatów w swojej kolekcji?"
    elif "Ostatnio zacząłem interesować się sztuką kalligrafii" in pytanie or "ostatnio zacząłem interesować się sztuką kalligrafii" in pytanie:
        return "Kalligrafia to sztuka pięknego pisania! Jakie techniki kalligrafii chciałbyś opanować?"
    elif "Mam zamiar zacząć regularnie uczęszczać na zajęcia z jogi" in pytanie or "mam zamiar zacząć regularnie uczęszczać na zajęcia z jogi" in pytanie:
        return "Regularne zajęcia jogi przynoszą wiele korzyści! Jakie aspekty jogi chciałbyś skoncentrować się na nauce?"
    elif "Ostatnio zacząłem interesować się sztuką kaligrafii" in pytanie or "ostatnio zacząłem interesować się sztuką kaligrafii" in pytanie:
        return "Kaligrafia to sztuka pięknego pisma! Jakie style kaligrafii chciałbyś opanować?"
    elif "Planuję rozpocząć kurs gry na gitarze" in pytanie or "planuję rozpocząć kurs gry na gitarze" in pytanie:
        return "Gra na gitarze to wspaniała umiejętność! Jakie utwory muzyczne chciałbyś nauczyć się grać na początku?"
    elif "Ostatnio zacząłem kolekcjonować znaczki pocztowe" in pytanie or "ostatnio zacząłem kolekcjonować znaczki pocztowe" in pytanie:
        return "Kolekcjonowanie znaczków pocztowych to pasjonujące hobby! Jakie znaczki chciałbyś dodać do swojej kolekcji?"
    elif "Mam zamiar zacząć regularnie trenować sztuki walki" in pytanie or "mam zamiar zacząć regularnie trenować sztuki walki" in pytanie:
        return "Trenowanie sztuk walki to doskonała forma samoobrony! Które sztuki walki chciałbyś obecnie trenować?"
    elif "Ostatnio zainteresowałem się sztuką animacji" in pytanie or "ostatnio zainteresowałem się sztuką animacji" in pytanie:
        return "Animacja to fascynujący świat! Jakie programy do animacji planujesz używać w swoich projektach?"
    elif "Planuję rozpocząć kurs rzeźby" in pytanie or "planuję rozpocząć kurs rzeźby" in pytanie:
        return "Rzeźba to sztuka trójwymiarowa! Jakie materiały do rzeźby chciałbyś eksperymentować podczas kursu?"
    elif "Ostatnio zacząłem interesować się sztuką fotografii portretowej" in pytanie or "ostatnio zacząłem interesować się sztuką fotografii portretowej" in pytanie:
        return "Fotografia portretowa to umiejętność uchwycenia wyrazu osobowości! Jakie techniki fotografii portretowej chciałbyś opanować?"
    elif "Mam zamiar zacząć uczęszczać na kurs gotowania sushi" in pytanie or "mam zamiar zacząć uczęszczać na kurs gotowania sushi" in pytanie:
        return "Gotowanie sushi to sztuka precyzji! Jakie rodzaje sushi chciałbyś nauczyć się przygotowywać na kursie?"
    elif "Ostatnio zacząłem kolekcjonować kubki z różnych miejsc" in pytanie or "ostatnio zacząłem kolekcjonować kubki z różnych miejsc" in pytanie:
        return "Kolekcjonowanie kubków to świetny sposób na zachowanie wspomnień! Jakie kubki masz już w swojej kolekcji?"
    elif "Mam zamiar zacząć regularnie pływać na basenie" in pytanie or "mam zamiar zacząć regularnie pływać na basenie" in pytanie:
        return "Pływanie to doskonała forma aktywności! Gdzie planujesz pływać regularnie na basenie?"
    elif "Ostatnio zacząłem interesować się sztuką haiku" in pytanie or "ostatnio zacząłem interesować się sztuką haiku" in pytanie:
        return "Pisanie haiku to sztuka krótkiego, ale wyrazistego wyrażania się! Jakie tematy chciałbyś eksplorować w swoich haiku?"
    elif "Mam zamiar zacząć uczęszczać na lekcje rysunku" in pytanie or "mam zamiar zacząć uczęszczać na lekcje rysunku" in pytanie:
        return "Rysunek to kreatywne wyrażanie siebie! W jakim stylu chciałbyś rozwijać swoje umiejętności rysunkowe?"
    elif "Ostatnio zacząłem interesować się sztuką kalisteniki" in pytanie or "ostatnio zacząłem interesować się sztuką kalisteniki" in pytanie:
        return "Kalistenika to trening ciała bez użycia sprzętu! Jakie ćwiczenia kalisteniczne chciałbyś opanować w pierwszej kolejności?"
    elif "Mam zamiar zacząć kolekcjonować stare mapy geograficzne" in pytanie or "mam zamiar zacząć kolekcjonować stare mapy geograficzne" in pytanie:
        return "Kolekcjonowanie starych map to podróż przez czas i przestrzeń! Jakie regiony geograficzne chciałbyś mieć na starych mapach?"
    elif "Ostatnio zacząłem interesować się sztuką gotowania molekularnego" in pytanie or "ostatnio zacząłem interesować się sztuką gotowania molekularnego" in pytanie:
        return "Gotowanie molekularne to połączenie nauki i kuchni! Jakie eksperymentalne dania chciałbyś przygotować w tej technice?"
    elif "Planuję rozpocząć kurs szycia" in pytanie or "planuję rozpocząć kurs szycia" in pytanie:
        return "Szycie to praktyczna umiejętność! Jakie projekty krawieckie chciałbyś tworzyć po ukończeniu kursu?"
    else:
        # Sprawdź podobieństwo do istniejących pytań
        podobne_pytanie = find_similar_question(pytanie)
        if podobne_pytanie:
            return find_ai_response(podobne_pytanie)
        else:
            return "Przepraszam, nie jestem w stanie zrozumieć. Możesz spróbować sformułować pytanie inaczej?"

def find_similar_question(pytanie):
    pytania_i_odpowiedzi = get_all_questions_and_answers()
    podobne_pytanie = max(pytania_i_odpowiedzi.keys(), key=lambda x: SequenceMatcher(None, pytanie, x).ratio(), default="")
    return podobne_pytanie if SequenceMatcher(None, pytanie, podobne_pytanie).ratio() > 0.4 else None

def find_ai_response(pytanie):
    pytania_i_odpowiedzi = get_all_questions_and_answers()
    return pytania_i_odpowiedzi.get(pytanie, "Przepraszam, nie mam dostępnej odpowiedzi na to pytanie.")

def get_all_questions_and_answers():
    try:
        with open("pytania_i_odpowiedzi.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_responses_to_json(responses, output_file):
    with open(output_file, "w") as file:
        json.dump({item["user"]: item["ai"] for item in responses}, file, indent=2)

# Wywołanie funkcji i zapis do pliku pytania_i_odpowiedzi.json
generate_and_save_responses(5)
