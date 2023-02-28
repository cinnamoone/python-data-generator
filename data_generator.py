import random
import datetime

deceasedID= []
datasmierci = []

deceasedInfo = []


additionalServices = [
   ' _id: "urnService", surviceName: "urna", price: 200 ',
   ' _id: "coffinService", surviceName: "trumna", price: 500',
   'id: "wreathService", surviceName: "wieniec", price: 150',
   '_id: "organistService", surviceName: "organista", price: 300, employees: ["OliwierSzymczak", "ElizaWrobel"]',
   '_id: "transportService", surviceName: "transport", price: 250',
   '_id: "decorationService", surviceName: "dekoracje",price: 300',
   '_id: "pallbearers1", surviceName: "trunnonosze",price: 100, employees: ["WalentyWojtowicz"]',
   '_id: "pallbearers2", surviceName: "trunnonosze",price: 200 ,employees: ["WalentyWojtowicz", "AdamFlorek"]',
   '_id: "pallbearers3", surviceName: "trunnonosze", price: 300, employees: ["WalentyWojtowicz", "AdamFlorek", "MariuszLesniak"]',
   '_id: "pallbearers4", surviceName: "trunnonosze", price: 350, employees: ["WalentyWojtowicz", "AdamFlorek", "MariuszLesniak", "StanislawWalczak"]',
   '_id: "pallbearers5", surviceName: "trunnonosze", price: 400, employees: ["WalentyWojtowicz", "AdamFlorek", "MariuszLesniak", "StanislawWalczak", "KarolTomczak"]',
   '_id: "pallbearers6", surviceName: "trunnonosze", price: 450, employees: ["WalentyWojtowicz", "AdamFlorek", "MariuszLesniak", "StanislawWalczak", "KarolTomczak","DorianSowa"]']
drivers = [
    'driver: {employeeID: "ArkadiuszDomanski", nameAndSurname: "Arkadiusz Domański"}',
    'driver: {employeeID: "AntoniMarkowski", nameAndSurname: "Antoni Markowski"}',
    'driver: {employeeID: "JuliannaSwiatek", nameAndSurname: "Julianna Świątek"}',
    'driver: {employeeID: "KlaudiuszDudek",nameAndSurname: "Klaudiusz Dudek"}',
    'driver: {employeeID: "ArkadiuszDomanski",nameAndSurname: "Arkadiusz Domański"']

cars = ['car: { _idCar: "karawan1", markAndModel:"Mercedes-Benz W212 Pilato Skyline", color: "czarny" }',
        'car: { _idCar: "karawan2", markAndModel:"Renault Trafic 2.0Dci", color: "metaliczny" }', 
        'car: { _idCar: "karawan3", markAndModel: "Renault Trafic 2.0Dci", color: "metaliczny" }', 
        'car: { _idCar: "karawan4", markAndModel: "Volkswagen Transporter T5", color: "metaliczny" }',
        'car: { _idCar: "karawan5", markAndModel: "Mercedes-Benz Vito 114 CDI 4MATIC Extralang", color: "biały" }',
        'car: { _idCar: "karawan6", markAndModel: "Chrysler 300C Touring 3.0 CRD DPF Automatik", color: "czarny" }']

## generator zmarłych


names = ["ANNA", "MARIA", "KATARZYNA", "MAŁGORZATA", "AGNIESZKA", "BARBARA", "EWA", "KRYSTYNA", "MAGDALENA", "ELŻBIETA", "JOANNA", "ALEKSANDRA", 
             "ZOFIA", "MONIKA", "TERESA", "DANUTA", "NATALIA", "JULIA", "KAROLINA", "MARTA", "BEATA", "DOROTA", "HALINA", "JADWIGA", "JANINA", "ALICJA", 
             "JOLANTA", "GRAŻYNA", "IWONA", "IRENA", "PAULINA", "JUSTYNA", "ZUZANNA", "BOŻENA", "WIKTORIA", "URSZULA", "RENATA", "HANNA", "SYLWIA", "AGATA", "HELENA", 
             "PATRYCJA", "MAJA", "IZABELA", "EMILIA", "ANETA", "WERONIKA", "EWELINA", "OLIWIA", "MARTYNA", "KLAUDIA", "MARIANNA", "MARZENA", "GABRIELA", 
             "STANISŁAWA", "DOMINIKA", "KINGA", "LENA", "EDYTA", "AMELIA", "WIESŁAWA", "KAMILA", "WANDA", "ALINA", "LIDIA", "LUCYNA", "MARIOLA", "NIKOLA", 
             "MIROSŁAWA", "WIOLETTA", "MILENA", "DARIA", "ANGELIKA", "KAZIMIERA", "GENOWEFA", "BOGUMIŁA", "ANTONINA", "LAURA", "OLGA", "SANDRA", "HENRYKA", 
             "ILONA", "JÓZEFA", "STEFANIA", "MICHALINA", "SABINA", "BOGUSŁAWA", "MARLENA", "REGINA", "NADIA", "ŁUCJA", "ANITA", "KORNELIA", "WŁADYSŁAWA",
            "CZESŁAWA", "ANIELA", "IGA", "LILIANA", "JAGODA", "MARCELINA", "NINA", "POLA", "WIOLETA", "ADRIANNA", "ROKSANA", "KARINA", "DAGMARA", 
            "CECYLIA", "MALWINA", "SARA", "LEOKADIA", "ZDZISŁAWA", "ŻANETA", "ELIZA", "BRONISŁAWA", "EUGENIA", "RÓŻA", "TETIANA", "BERNADETA", 
            "NATALIIA", "KAJA", "OLENA", "JULITA", "DANIELA", "ALDONA", "IRYNA", "ANASTAZJA", "KLARA", "BLANKA", "OKSANA", "ROZALIA", "VIOLETTA",
            "MAGDA", "CELINA", "DIANA", "SVITLANA", "HONORATA", "LILIANNA", "OLHA", "ADRIANA", "PAULA", "MATYLDA", "BRYGIDA", "GERTRUDA", 
            "MIECZYSŁAWA", "IZABELLA", "MARIIA", "BOŻENNA", "AURELIA", "YULIIA", "KALINA", "MARIKA", "ELWIRA", "MARZANNA", "SONIA", "ANDŻELIKA", 
            "NELA", "VIKTORIIA", "ARLETA", "LIUDMYLA", "KATERYNA", "ANASTASIIA", "OLIVIA", "FRANCISZKA", "ADELA", "LUIZA", "JUDYTA", "HALYNA", 
            "ALFREDA", "NICOLE", "NATASZA", "TATIANA", "NICOLA", "JOWITA", "VICTORIA", "MARYNA", "ROMANA", "APOLONIA", "VANESSA", "LUDWIKA", 
            "JULIANNA", "TAMARA", "ELEONORA", "VALENTYNA", "MARZENNA", "WACŁAWA", "JESSICA", "INGA", "LIWIA", "ZENONA", "ESTERA", "MELANIA", 
            "ADA", "NADIIA", "BERNADETTA", "MIA", "WALENTYNA", "HILDEGARDA", "INNA", "ZENOBIA", "DONATA", "LUDMIŁA", "FELICJA", "ANETTA", 
            "BIANKA", "LARYSA", "ROMUALDA", "OTYLIA", "ELENA", "GIZELA", "AMANDA", "PELAGIA", "IRMINA", "LIUBOV", "RITA", "ERYKA", "OLEKSANDRA", 
            "IDA", "LILIA", "SŁAWOMIRA", "MAYA", "BERNARDA", "LILLA", "YANA", "LONGINA", "ALLA", "WALERIA", "TEODOZJA", "RYSZARDA", "TEODORA",
            "EMMA", "ADELAJDA", "KAMILLA", "MIRELA", "ALBINA", "LILIIA", "FAUSTYNA", "ALONA", "SAMANTA", "OLIMPIA", "LILA", "FELIKSA",
            "ALEXANDRA", "LUCJA", "MARYLA", "MARCELA", "SOFIIA", "ZYTA", "SOFIA", "LEONARDA", "GAJA", "MARIANA", "ANGELINA", "IVANNA", 
            "VERONIKA", "VIKTORIA", "OKTAWIA", "KSENIA", "VALERIIA", "KONSTANCJA", "PAMELA", "ZOJA", "KHRYSTYNA", "WANESSA", "BOLESŁAWA",
            "BOGNA", "JAGNA", "MIRELLA",
            "CLAUDIA", "LESIA", "NOEMI", "KRZYSZTOFA", "SALOMEA", "VIRA", "NADZIEJA", "EDWARDA", "ELFRYDA", "NEL", "INEZ", "MARIYA", 
            "PIOTR", "KRZYSZTOF", "ANDRZEJ", "TOMASZ", "JAN", "PAWEŁ", "MICHAŁ", "MARCIN", "STANISŁAW", "JAKUB", "ADAM", "MAREK", "ŁUKASZ", "GRZEGORZ", 
            "MATEUSZ", "WOJCIECH", "MARIUSZ", "DARIUSZ", "ZBIGNIEW", "JERZY", "MACIEJ", "RAFAŁ", "ROBERT", "JÓZEF", "KAMIL", "JACEK", "TADEUSZ", "DAWID",
            "RYSZARD", "SZYMON", "KACPER", "JANUSZ", "BARTOSZ", "JAROSŁAW", "MIROSŁAW", "SŁAWOMIR", "HENRYK", "ARTUR", "SEBASTIAN", "DAMIAN", "PATRYK", 
            "KAZIMIERZ", "PRZEMYSŁAW", "DANIEL", "KAROL", "ROMAN", "MARIAN", "WIESŁAW", "ANTONI", "FILIP", "ADRIAN", "ARKADIUSZ", "ALEKSANDER", "DOMINIK", 
            "BARTŁOMIEJ", "LESZEK", "FRANCISZEK", "WALDEMAR", "MIKOŁAJ", "ZDZISŁAW", "KRYSTIAN", "RADOSŁAW", "WIKTOR", "BOGDAN", "EDWARD", "MIECZYSŁAW", 
            "KONRAD", "WŁADYSŁAW", "HUBERT", "CZESŁAW", "IGOR", "EUGENIUSZ", "OSKAR", "STEFAN", "BOGUSŁAW", "ZYGMUNT", "IRENEUSZ", "MARCEL", "WITOLD",
                "MAKSYMILIAN", "SYLWESTER", "MIŁOSZ", "WŁODZIMIERZ", "ZENON", "ALAN", "OLIWIER", "CEZARY", "NIKODEM", "NORBERT", "LEON", "GABRIEL", "JULIAN", 
                "BŁAŻEJ", "OLEKSANDR", "FABIAN", "BRONISŁAW", "IGNACY", "EMIL", "ERYK", "WACŁAW", "TYMOTEUSZ", "LECH", "BOLESŁAW", "TYMON", "BERNARD", "EDMUND", 
                "SERHII", "VOLODYMYR", "ANDRII", "REMIGIUSZ", "KSAWERY", "NATAN", "LUCJAN", "OLAF", "ROMUALD", "BORYS", "KAJETAN", "SZCZEPAN", "ALBERT", 
                "SEWERYN", "GRACJAN", "ALFRED", "KUBA", "DMYTRO", "TOBIASZ", "IVAN", "LUDWIK", "JOACHIM", "MYKOLA", "LESŁAW", "BOGUMIŁ", "VASYL", "GERARD", 
                "VITALII", "ERNEST", "MAKSYM", "IHOR", "BRUNO", "FELIKS", "KORNEL", "OLIVIER", "JĘDRZEJ", "YURII", "ALOJZY", "VIKTOR", "OLEH", "ALEXANDER", 
                "ALEX", "MYKHAILO", "BOHDAN", "JULIUSZ", "LEONARD", "KLAUDIUSZ", "DAVID", "BENEDYKT", "ALEKS", "DORIAN", "RAJMUND", "TEODOR", "CYPRIAN", 
                "MARTIN", "OLIVER", "OLEKSII", "VLADYSLAV", "RUDOLF", "NATANIEL", "KONSTANTY", "RUSLAN", "DENIS", "HIERONIM", "BRAJAN", "GUSTAW", "MICHAEL", 
                "WINCENTY", "SAMUEL", "ZYGFRYD", "MARCELI", "PAVLO", "FLORIAN", "ERWIN", "MIESZKO", "KEVIN", "FRYDERYK", "ARIEL", "DENYS", "ANATOLII", "IWO",
                  "VADYM", "MILAN", "ARTEM", "ALEKSY", "PETRO", "BENIAMIN", "ROLAND", "SERGIUSZ", "WALENTY", "YAROSLAV", "KORDIAN", "ADOLF", "OLEG", "AUGUSTYN", 
                  "YEVHEN", "AMADEUSZ", "TARAS", "ANTON", "BRUNON", "JEREMI", "OLGIERD", "LEOPOLD", "VALERII", "PATRICK", "ALIAKSANDR", "EMILIAN", "KEWIN", 
                  "MAXIMILIAN", "HERBERT", "SERGII", "ALFONS", "ALBIN", "ANDREI", "YEVHENII", "THOMAS", "ARNOLD", "OLIWER", "OSCAR", "WILHELM", "NICOLAS",
                    "VICTOR", "VIACHESLAV", "STANISLAV", "ANATOL", "MAURYCY", "HELMUT", "WALTER", "GINTER", "OKTAWIAN", "MANFRED", "PETER", "EDWIN", "TEOFIL",
                      "SIARHEI", "ANDRIY", "KOSTIANTYN", "EMANUEL", "KORNELIUSZ", "WERNER", "JEREMIASZ", "JONASZ", "WALERIAN", "STEPAN", "KRYSPIN", "JONATAN", 
                      "CHRISTIAN", "LECHOSŁAW", "KASPER", "NATHAN", "ZIEMOWIT", "VALENTYN", "DZMITRY", "XAVIER", "BENJAMIN", "NIKOLAS", "MARK", "LEO",
                        "KLEMENS", "FERDYNAND", "JACOB", "PATRYCJUSZ", "TYTUS", "MIRON", "LONGIN", "NAZAR", "MAX", "ARON", "EDUARD", "IURII", "PAVEL", 
                        "KSAWIER", "PAUL", "HORST", "YURIY", "LEONID", "ILLIA", "WAWRZYNIEC", "HUGO", "JACENTY", "MATTHEW", "PHILIP", "ANDREAS", "CHRISTOPHER", 
                        "ELIASZ", "IZYDOR", "DIONIZY", "ŁUCJAN", "EWALD", "GERHARD", "ELIGIUSZ", "JOHN", "ANTHONY", "MARCO", "ROCH", "JAROMIR", "KASJAN", 
                        "MYKHAYLO", "SIMON", "MAKS", "RAFAEL", "BRIAN", "MOHAMED", "RADOMIR",
              "ROSTYSLAV", "BAZYLI", "NICHOLAS", "ZBYSŁAW", "JONATHAN", "VINCENT", "ALI", "WIT", "ULADZIMIR", "YURY", "SERHIY", "VITALIY", "VITALI", "KOSMA"]

surnames = ["NOWAK","KOWALSKI","WIŚNIEWSKI","WÓJCIK","KOWALCZYK","KAMIŃSKI","LEWANDOWSKI","ZIELIŃSKI","SZYMAŃSKI","WOŹNIAK","DĄBROWSKI",
                "KOZŁOWSKI","JANKOWSKI","MAZUR","KWIATKOWSKI","WOJCIECHOWSKI","KRAWCZYK","KACZMAREK","PIOTROWSKI","GRABOWSKI","ZAJĄC","PAWŁOWSKI",
                "KRÓL","MICHALSKI","WRÓBEL","WIECZOREK","JABŁOŃSKI","NOWAKOWSKI","MAJEWSKI","OLSZEWSKI","STĘPIEŃ","DUDEK","JAWORSKI","ADAMCZYK",
                "MALINOWSKI","GÓRSKI","PAWLAK","NOWICKI","SIKORA","WITKOWSKI","RUTKOWSKI","WALCZAK","BARAN","MICHALAK","SZEWCZYK","OSTROWSKI",
                "TOMASZEWSKI","ZALEWSKI","WRÓBLEWSKI","PIETRZAK","JASIŃSKI","MARCINIAK","SADOWSKI","BĄK","ZAWADZKI","DUDA","JAKUBOWSKI","WILK",
                "CHMIELEWSKI","WŁODARCZYK","BORKOWSKI","SOKOŁOWSKI","SZCZEPAŃSKI","SAWICKI","LIS","KUCHARSKI","KALINOWSKI","MAZUREK","WYSOCKI",
                "KUBIAK","MACIEJEWSKI","KOŁODZIEJ","KAŹMIERCZAK","CZARNECKI","SOBCZAK","KONIECZNY","KRUPA","GŁOWACKI","URBAŃSKI","ZAKRZEWSKI",
                "MRÓZ","KRAJEWSKI","WASILEWSKI","SIKORSKI","LASKOWSKI","ZIÓŁKOWSKI","SZULC","GAJEWSKI","MAKOWSKI","KACZMARCZYK","BRZEZIŃSKI",
                "BARANOWSKI","PRZYBYLSKI","SZYMCZAK","KANIA","JANIK","BŁASZCZYK","BOROWSKI","KOZAK","ADAMSKI","GÓRECKI","SZCZEPANIAK","CHOJNACKI",
                "KOZIOŁ","LESZCZYŃSKI","CZERWIŃSKI","LIPIŃSKI","MUCHA","KOWALEWSKI","ANDRZEJEWSKI","WESOŁOWSKI","MIKOŁAJCZYK","CIEŚLAK","ZIĘBA",
                "JAROSZ","MUSIAŁ","MARKOWSKI","KOWALIK","KOŁODZIEJCZYK","KOPEĆ","BRZOZOWSKI","ŻAK","NOWACKI","PIĄTEK","DOMAŃSKI","ORŁOWSKI",
                "PAWLIK","KUREK","TOMCZYK","CIESIELSKI","TOMCZAK","WÓJTOWICZ","WAWRZYNIAK","KOT","WOLSKI","POLAK","KRUK","MARKIEWICZ","SOWA",
                "STASIAK","JASTRZĘBSKI","STANKIEWICZ","KARPIŃSKI","URBANIAK","ŁUCZAK","KLIMEK","PIASECKI","CZAJKOWSKI","WIERZBICKI","NAWROCKI",
                "GAJDA","STEFAŃSKI","BEDNAREK","BIELECKI","DZIEDZIC","MADEJ","JANICKI","MILEWSKI","SKIBA","SOSNOWSKI","MAJCHRZAK","LEŚNIAK",
                "JÓŹWIAK","KOWAL","MAJ","URBAN","ŚLIWIŃSKI","MAŁECKI","SOCHA","MAREK","DOMAGAŁA","BEDNARCZYK","KASPRZAK","WRONA","DOBROWOLSKI",
                "PAJĄK","MATUSZEWSKI","MICHALIK","OLEJNICZAK","RATAJCZAK","ORZECHOWSKI","WILCZYŃSKI","ROMANOWSKI","ŚWIĄTEK","KUROWSKI","OLEJNIK",
                "GRZELAK","OWCZAREK","ŁUKASIK","ROGOWSKI","MAZURKIEWICZ","SROKA","BUKOWSKI","SOBOLEWSKI","BARAŃSKI","KOSIŃSKI","KĘDZIERSKI",
                "MARSZAŁEK","BEDNARZ","ZYCH","SOBCZYK","SKOWROŃSKI","MARCINKOWSKI","MATUSIAK","RYBAK","KOZIEŁ","CHRZANOWSKI","LISOWSKI","ŚWIDERSKI",
                "KASPRZYK","BEDNARSKI","BIAŁEK","WITEK","KUCZYŃSKI","PLUTA","KWIECIEŃ","PALUCH","JANISZEWSKI","GRZYBOWSKI","CHMIEL","JĘDRZEJEWSKI",
                "MUSZYŃSKI","CZAJKA","MARCZAK","TUREK","MORAWSKI","MARZEC","MAŁEK","KACZOR","ŻUKOWSKI","CZAJA","KUBICKI","PIEKARSKI","ŚLIWA","CZECH",
                "SZCZĘSNY","OSIŃSKI","PRZYBYSZ","KRZEMIŃSKI","JANOWSKI","GOŁĘBIEWSKI","BIERNACKI","KULESZA","STEFANIAK","SZYDŁOWSKI","LECH","SMOLIŃSKI",
                "MICHAŁOWSKI","STANISZEWSKI","SERAFIN","GÓRA","BANACH","KUJAWA","LEWICKI","CIEŚLIK","RAK","MURAWSKI","POPŁAWSKI","KACPRZAK","PIETRZYK",
                "DĘBSKI","STACHOWIAK","RUDNICKI","ŻUREK","PIĄTKOWSKI","GÓRNY","BANAŚ","ZAWADA","GÓRKA","KARCZEWSKI","PODGÓRSKI","NIEMIEC","MATYSIAK",
                "SOWIŃSKI","ŻURAWSKI","GOŁĘBIOWSKI","CZYŻ","KLIMCZAK","BIENIEK","ROSIŃSKI","KUŚ","GODLEWSKI","GRUSZKA","AUGUSTYNIAK","KRAWIEC",
                "SKRZYPCZAK","GROCHOWSKI","DROZD","PANEK","PTAK","PRZYBYŁA","GIL","KOMOROWSKI","RÓŻAŃSKI","WINIARSKI","KONOPKA","CYBULSKI","SIWEK",
                "SŁOWIK","LEŚNIEWSKI","KULIK","GRZYB","KŁOS","KRZYŻANOWSKI","CICHOŃ","SZCZEPANIK","GRACZYK","ZARZYCKI","KACZYŃSKI","MIELCZAREK",
                "TOKARSKI","ZAREMBA","MIKOŁAJCZAK","MŁYNARCZYK","STAŃCZYK","CICHOCKI","BIERNAT","SZOSTAK","BUCZEK","SZYMCZYK","STRZELECKI","WĘGRZYN",
                "JUREK","SZCZYGIEŁ","MAĆKOWIAK","BARTKOWIAK","SKOWRON","GĄSIOR","JANUS","BOGUSZ","CIEŚLA","FILIPIAK","GAWRON","JANIAK","KALETA",
                "NIEWIADOMSKI","KULA","KUBIK","KUCHARCZYK","PAŁKA","KOSTRZEWA","RZEPKA","BAGIŃSKI","KSIĄŻEK","RAKOWSKI","SIENKIEWICZ","GAWLIK",
                "RÓŻYCKI","BARTCZAK","MALEC","ANTCZAK","FRĄCZEK","ZARĘBA","BANASIAK","TRZCIŃSKI","KRÓLIKOWSKI","ŻEBROWSKI","DŁUGOSZ","HAJDUK",
                "ROGALSKI","MIKULSKI","ROGALA","LACH","BOREK","KISIEL","TROJANOWSKI","ROJEK","GAWROŃSKI","TKACZYK","GRZEGORCZYK","WITCZAK","STEC",
                "DOBOSZ","MALISZEWSKI","WOLNY","WĄSIK","RYBICKI","RADOMSKI","ŚLUSARCZYK","MIKA","ZABOROWSKI","KMIECIK","GAŁĄZKA","BIAŁAS","KACZOROWSKI",
                "WALKOWIAK","PAWELEC","GRZESIAK","FRĄCKOWIAK","BOGUCKI","FRANKOWSKI","SOKÓŁ","WNUK","LIPSKI","BOCHENEK","ZYGMUNT","CICHY","KWAŚNIEWSKI",
                "KARWOWSKI","WÓJCICKI","WIĘCKOWSKI","ŻMUDA","NAWROT","JANAS","JUSZCZAK","DUDZIŃSKI","PIETRAS","GAWEŁ","MROCZEK","ROSIAK","LASOTA",
                "WOJTCZAK","KOŁODZIEJSKI","SKRZYPEK","PASTERNAK","ŁAPIŃSKI","WROŃSKI","JĘDRZEJCZYK","BURZYŃSKI","FIJAŁKOWSKI","BUJAK","KRYSIAK",
                "MISIAK","DĄBEK","GRUSZCZYŃSKI","KARAŚ","PIÓRKOWSKI","CZYŻEWSKI","PIWOWARCZYK","MASŁOWSKI","KUBACKI","GUTOWSKI","BOROWIEC",
                "SZAFRAŃSKI","KAŁUŻNY","JAGODZIŃSKI","SOŁTYS","STELMACH","ZAJĄCZKOWSKI","ŁUKASZEWSKI","TARNOWSKI","JAGIEŁŁO","CEBULA","ŁUKASIEWICZ",
                "KAŁUŻA","LISIECKI","ZIELONKA","BIELAWSKI","WOŹNY","CYGAN","JURKIEWICZ","KRAKOWIAK","PILARSKI","SKOCZYLAS","SKIBIŃSKI","DRZEWIECKI",
                "PAKUŁA","JĘDRZEJCZAK","SZCZEŚNIAK","WILCZEK","FALKOWSKI","FILIPEK","BOBER","KĘDZIORA","JAKUBIAK","GĄSIOROWSKI","SOBIERAJ","STRZELCZYK",
                "TWARDOWSKI","DĘBOWSKI","FLIS","WASIAK","RACZYŃSKI","KUBICA","MIERZEJEWSKI","GOŁĄB","STANEK","BARTOSIK","GUZIK","GÓRNIAK","WIĘCEK",
                "GÓRAL","WOLAK","KULIG","MAJCHER","MATUSZAK","DROZDOWSKI","BILSKI","MOTYKA","RUSIN","CHOLEWA","NOWACZYK","SZWED","GRZYWACZ",
                "CZAPLA","KOPCZYŃSKI","KRUPIŃSKI","STOLARCZYK","FLOREK","URBAŃCZYK","PACZKOWSKI","BURY","JAŚKIEWICZ","MISZTAL","PYTEL","WOJTAS",
                "MICHAŁEK","KASZUBA","KUC","GWÓŹDŹ","PROKOP","DZIUBA","RUCIŃSKI","DUBIEL","MALICKI","ZAGÓRSKI","BIAŁY","JANKOWIAK","BIELAK",
                "BOŻEK","ŚWIERCZYŃSKI","KACZMARSKI","MODZELEWSKI","KĘPA","PARTYKA","ZWOLIŃSKI","SKÓRA","GAŁKA","JANUSZ","PŁONKA","BIEŃKOWSKI",
                "MILCZAREK",]
streets= ["Rybałtowska", "Składowa", "Sołtysa Dytmara", "Spokojna", "Stanisława Kunickiego", "Stanisława Lentza", "Stanisława Pyjasa", 
          "św. Bronisławy", "Śląska", "Śmiała", "Wjazdowa", "Rzepichy", "Królewska", "Aleja Kasy Oszczędności Miasta Krakowa", 
          "Kazimierza Wielkiego", "Koło Strzelnicy", "Aleja Konarowa", "Kopalina", "Jadwigi z Łobzowa", "Henryka Rodakowskiego", "Cygańska",
          "Koziarówka", "Błażeja Czepca", "Stanisława Kostki Potockiego", "Słomnicka", "Rysi Stok", "Ojcowska", "Odlewnicza", "Niska", 
          "Mrówczana", "Michała Wójcickiego", "Krakusów", "Kaszubska", "Jana Stanisławskiego", "Nad Sudołem", "Mydlnicka", "Pod Skałą", 
          "Szafirowa", "Stańczyka", "Aleja 3 Maja", "Cedrowa", "Jarzynowa", "Emaus", "Estreicherów", "Generała Kiwerskiego", 
          "Osiedle Krowodrza Górka", "Eugeniusza Romera", "Zaczarowane Koło", "Halki", "Bularnia", "Wądół", "Piotra Borowego", 
          "Wielkotyrnowska", "Kraków skwer Skwer im. Więźniów Obozów Zagłady", "Konopna", "Kawiory", "ks. Stanisława Truszkowskiego",
          "ks. Piotra Skargi", "Park Decjusza", "Zygmunta Wyrobka", "Wacława Nałkowskiego", "Tadeusza Wyrwy-Furgalskiego", "Brzegowa", 
          "Tadeusza Kasprzyckiego", "Świętego Wojciecha", "Suche Łąki", "Starego Wiarusa", "Park Tadeusza Kościuszki", "Tadeusza Makowskiego",
          "Podłącze", "Pod Sowińcem", "Tadeusza Ochlewskiego", "Zakręt", "Wincentego Wodzinowskiego", "Za Targiem", "Andrzeja Frycza-Modrzewskiego", 
          "Aleja Artura Grottgera", "Bakałarzy", "Górka Narodowa", "Bażancia", "Biała", "Bliska", "Bratysławska", "Pylna", "Rolnicza", "Aleja Adama Mickiewicza", 
          "Adama Marczyńskiego", "Osiedle Wolfganga Amadeusa Mozarta", "Władysława Anczyca", "Michała Stachowicza", "Mieczysława Karłowicza", "Stelmachów",
          "Adama Chmiela", "Piotra Kluzeka", "Owsiana", "Drzymały", "Ludwika Pasteura", "Kaczorówka", "Aleja Pustelnika", "Nad Strugą", "Kraków bulw. Bulwar Rodła", 
          "Grenadierów", "Grzegorza Korzeniaka", "Henryka Sienkiewicza", "Hamernia", "Gontyna", "Bukietowa", "Ireny Kosmowskiej", "Jabłonna", "Morelowa", 
          "Aleja Modrzewiowa", "mjr. Łupaszki", "Maćkowa Góra", "Margaretek", "Nad Źródłem", "Dzielna", "Marynarska", "Maurycego Beniowskiego", 
          "Aleja Mieczysława Małeckiego", "Misjonarska", "Mlaskotów", "Jana Sawickiego", "Jana Zygmunta Robla", "Jasna", "Senatorska", "Siewna", "Skalna",
          "Sosnowiecka", "Spiżowa", "Jana i Józefa Kotlarczyków", "Stanisława Ciechanowskiego", "Jana Buszka", "Jabłonkowska", "Stanisława Tondosa",
          "Jarosława Dolińskiego", "Ryszarda Berwińskiego", "Józefa Elsnera", "Zygmunta Starego", "Leopolda Kmietowicza", "Aleja Juliusza Słowackiego", 
          "Józefa Mehoffera", "Władysława Podkowińskiego", "Towarowa", "Jerzego Jurowicza", "Przyszłości", "rtm. Witolda Pileckiego", "Stefana Banacha",
          "Gryczana", "Bytomska", "Flisacka", "Władysława Natansona", "Włóczków", "Arsenał", "Alojzego Kaczmarczyka", "Kuźnicza", "Kazimierza Nitscha",
          "Kasztelańska", "Za Skłonem", "Chabrowa", "Feliksa Szlachtowskiego", "Gajówka", "Osiedle Witkowice Nowe", "Turowiec", "Tadeusza Peipera", 
          "Osiedle Srebrne Uroczysko", "Skotnica", "Samuela Bogumiła Lindego", "Piotra Wysockiego", "Gabrieli Zapolskiej", "Franciszka Pększyca-Grudzińskiego",
          "Zaborska", "Feliksa Kopery", "Jemiołuszek", "Na Mostkach", "Marii Bobrzeckiej", "Lucjana Siemieńskiego", "Kazimierza Morawskiego", "Na Wirach", 
          "Narcyzowa", "Lucjana Rydla", "Ludomira Różyckiego", "Toruńska", "Ludwika Krzywickiego", "Na Borach", "Migdałowa", "Janusza Korczaka",
          "Emilii Plater", "gen. Mariana Kukiela", "Doktora Twardego", "bpa Józefa Gawliny", "Cicha", "Bydgoska", "Lniana", "Lubelska", "Mariana Hemara",
          "Aleja Marszałka Ferdinanda Focha", "Emila Godlewskiego", "Proszowicka", "Gabriela Narutowicza", "gen. Tadeusza Pełczyńskiego", "Franciszka Kowalskiego",
          "Franciszka Bielaka", "Edmunda Biernackiego", "Cisowa", "Budrysów", "Bursztynowa", "Czesława Niemena", "Czyżyków", "Gaik", "Gzymsików", "Prądnicka", "Porzecze",
          "Piastowska", "Pasternik", "Oleandry", "Ogrodniczek", "Nawigacyjna", "Gnieźnieńska", "Gospodarska", "Gramatyka", "Eliasza Radzikowskiego", 
          "Erazma i Stanisława Fabijańskich", "Feliksa Radwańskiego", "Ukryta", "Uboczna", "Tytusa Czyżewskiego", "Tkacka", "Bolesława Prusa", "Bodziszkowa",
          "Białe Wzgórze", "Balicka", "Astronomów", "Adolfa Szyszki-Bohusza", "Urodzajna", "Wincentego Weryhy-Darowskiego", "Filarecka", "Generała Franciszka Paszkowskiego", 
          "gen. Józefa Olszyny-Wilczyńskiego", "Aleja Zygmunta Krasińskiego", "Osiedle Złota Podkowa", "Kraków inne Zjazd Rogoziany", "Zaścianek", "Henryka Müncha", 
          "Zaklucze", "Włodzimierza Tetmajera", "Aleja Do Kopca", "Juliana Fałata", "Jesionowa", "Jerzego Dobrzyckiego", "Jaskółcza", "Jantarowa", "Jałowcowa", 
          "Jacka Malczewskiego", "Hoża", "Henryka Pachońskiego", "Astronautów", "Josepha Conrada", "Józefa Herzoga", "Józefitów", 
          "Józefa Friedleina", "Jordanowska", "Jodłowa", "Jaxy Gryfity", "Jana Stróżeckiego", "Jadwigi Majówny", "Insurekcji Kościuszkowskiej", "Junacka", 
          "Juliusza Lea", "Altanowa", "Akademicka", "Dziewanny", "Palmowa", "Pejzażowa", "Pękowicka", "Pod Fortem", "Pod Sikornikiem", "Pomorska", "Potoczek",
          "Bolesława Leśmiana", "Gdyńska", "Generał Marii Wittek", "Orlich Gniazd", "Olchowa", "Dożynkowa", "Do Obserwatorium", "28 Lipca 1943", "Igrców", "Sewera", 
          "Ignacego Domeyki", "Henryka Reymana", "Nawojowska", "Niezapominajek", "Ojca Eugeniusza Krajewskiego", "Przegorzalska", "Bielańska", "Na Polach", 
          "Młodej Polski", "dr. Owcy-Orwicza", "Justowska", "Kazimierza Herwina-Piątka", "Klonowa", "Kołaczy", "Kraków inne kopiec Józefa Piłsudskiego", 
          "Kuźnicy Kołłątajowskiej", "Lajkonika", "Na Polankach", "Nasza", "Agrestowa", "Adama Vetulaniego", "Pod Szańcami", "Pod Szwedem", "Poniedziałkowy Dół",
          "Poręba", "Porzeczkowa", "Północna", "Przegon", "Przepiórcza", "Lazurowa", "Legnicka", "Leona Wyczółkowskiego", "Witolda Budryka", "Wincentego Oszustowskiego",
          "Wiedeńska", "Warmijska", "Urzędnicza", "Tomasza Arciszewskiego", "Jeleniowa", "Zawodzie", "Zbrojów", "Józefa Grzesiaka Czarnego", "Zakliki z Mydlnik", 
          "Zakamycze", "Lisia", "Tadeusza Boya-Żeleńskiego", "Tadeusza Rogalskiego", "Lenartowicza", "Wiosenna", "Władysława Syrokomli", "Włodzimierza Puchalskiego",
          "Wojciecha Halczyna", "Wójtowska", "Wrocławska", "Józefa Chełmońskiego", "Rusznikarska - Deptak", "Stanisława Grochowiaka", "Stanisława Konarskiego", 
          "Starowolska", "Stefana Jaracza", "Szymona Zimorowicza", "Szaserów", "Syreny", "Symfoniczna", "Stanisława Tomkowicza", "Stanisława Przybyszewskiego", "Skrajna", 
          "Sarnie Uroczysko", "Kraków inne Las Wolski", "Krzywy Zaułek", "Królowej Jadwigi", "Kluczborska", "Klemensa Bąkowskiego", "Aleja Kijowska", "Kazimierza Wyżgi", 
          "Aleja Kasztanowa", "Kadrówki", "Kadecka", "Sokola", "Słowicza", "Romana Ingardena", "Na Grabinach", "Na Budzyniu", "Na Błoniach", "Matki Pauli Zofii Tajber", 
          "Łukasza Górnickiego", "Ludwika Iwaszki", "Litewska", "Władysława Reymonta", "Wodociągowa", "Piotra Stachiewicza", "Na Nowinach", "Nad Zalewem",
          "rtm. Zbigniewa Dunin-Wąsowicza", "Strzelnica", "Szopkarzy", "Nietoperzy", "Olkuska", "Opolska", "Orla", "Oświęcimska", "Piaskowa", "Piaszczysta", 
          "Pod Sulnikiem", "Plac Inwalidów", "Pod Stokiem", "Fiszera", "Do Przystani", "Fryderyka Chopina", "gen. Augusta Fieldorfa-Nila", "Głęboka", "Grażyny", 
          "inż. Adama Bielańskiego", "Jana Lechonia", "Jana Łazarskiego", "Jana Palacha", "Feliksa Konecznego", "Czeremchowa", "Pod Janem", "Papiernicza", "Pamiętna",
          "Nowowiejska", "Chełmska", "Grabowa", "Edwarda Bzymka-Strzałkowskiego", "dr. Tadeusza Kudlińskiego", "Czarnowiejska", "Czeladnicza", "Bociana", 
          "Waleriana Tumanowicza", "Kujawska", "Józefa Korzeniowskiego", "Jontkowa Górka", "Jana Styki", "Cichy Kącik", "Księcia Józefa", "Kronikarza Galla", 
          "Kręta", "Kosmonautów", "Kogucia", "Kazimierza Czapińskiego", "gen. Mieczysława Smorawińskiego", "Podłużna", "Mirowska", "Litawora", "Leśna", "Zgody",
          "Zygmuntowska", "Kraków inne Źródło im. Jerzego Setmajera", "Żmujdzka", "Leszczynowa", "Leona Chwistka", "Kmieca", "Osiedle Bronowice Nowe", 
          "Vlastimila Hofmana", "6 Sierpnia", "Zaszkolna", "Przesmyk", "Stawowa", "Rusznikarska", "Przeskok", "Zygmunta Mysłakowskiego", "Włościańska", "Świerkowa",
          "Podkamyk", "Lekarska", "Legendy", "Złota", "Zefirowa", "Zarzecze", "Kamedulska", "Katowicka", "Kazimierza Pużaka", "Kazimierza Wierzyńskiego", 
          "kopiec Tadeusza Kościuszki", "Krowoderskich Zuchów", "Krucza", "Aleja Sosnowa", "Okulistów", "Konwisarzy", "Kamienna", "Aleja 29 Listopada", "Dolina", "Dworna",
          "Aleja Panieńskich Skał", "Bałtycka", "Batowicka", "Bibicka", "Kościelna", "Łowiecka", "Kraków rondo Rondo Ofiar Katynia",
          "Starego Dębu", "Park Stanisława Wyspiańskiego", "Stanisława Wyspiańskiego", "Jerzego Samuela Bandtkiego", "Park Jordana", "Józefa Ignacego Kraszewskiego", 
          "Józefa Rostafińskiego", "Na Błonie", "Mikołaja Reja", "Pod Strzechą", "Karola Szymanowskiego", "Heleny Modrzejewskiej", "Bruzdowa", "Smętna", "Puszczyków",
          "Bolesława Komorowskiego", "Wojciecha Weissa", "Borówczana", "Złoty Róg", "Bartosza Głowackiego", "Bagatela", "Armii Krajowej", "Tadeusza Kościuszki",
          "Polna", "Nawojki", "Świętokrzyska", "Plac Nowowiejski", "Okrąg", "Okrężna", "Olszanicka", "Pajęcza", "Zdrowa", "Piotra Brzezińskiego", "Ludmiły Korbutowej", 
          "Antoniego Odyńca", "Antoniego Augustynka-Wichury", "Stanisława Rokosza", "Stanisława Skarbińskiego", "Szarotki", "Amazonek", "Aleksandra Prystora", "Drożyna",
          "Eugeniusza Kwiatkowskiego", "Daniela Chodowieckiego", "Daleka", "Ludomira Benedyktowicza", "Stanisława Kasznicy", "Pleszowska", "Zygmunta Glogera", "Zakątek",
          "Winowców", "Wilcza", "Rędzina", "Rybna", "Rzeczna", "Salwatorska", "Karola Frycza", "Słotna", "Bolesława Czerwieńskiego", "Jasnogórska", 
          "ks. Ferdynanda Machaya", "Filtrowa", "Mieczysława Niedziałkowskiego", "gen. Bolesława Wieniawy-Długoszowskiego", "ks. Kazimierza Siemaszki",
          "Generała Stanisława Sosabowskiego", "Głogowa", "Głogowiec", "Górna", "Gradowa", "Gustawa Ehrenberga", "Cieszyńska", "Chocimska", "Tatarska", 
          "Turystyczna", "Waleczna", "Wesele", "Wilczy Stok", "Wioślarska", "Władysława Żeleńskiego", "Wojskowa", "Chmurna", "Jęczmienna", "Belwederczyków",
          "Bolesława Wallek-Walewskiego", "Na Wyrębę", "Juliana Tokarskiego", "Józefa Wybickiego", "Józefa Mackiewicza", "Józefa Kałuży", "Koralowa", "Józefa Becka"]

# for i in range(700):
#         name = random.choice(names)
#         surname = random.choice(surnames)
#         _id = f"{name}{surname}"
#         deceasedID.append(_id)
#         birth_year = random.randint(1939, 1998)
#         birth_month = random.randint(1, 12)
#         birth_day = random.randint(1, 28)
#         birth_date = datetime.datetime(birth_year, birth_month, birth_day)
#         death_year = random.randint(2015, 2022)
#         death_month = random.randint(1, 12)
#         death_day = random.randint(1, 28)
#         death_date = datetime.datetime(death_year, death_month, death_day, 0, 0)
#         datasmierci.append(death_date)
#         pesel = f"{birth_date.year%100}{birth_date.month:02d}{birth_date.day:02d}" + str(random.randint(100000, 999999))
#         deceasedInfo.append({
#             "_id": _id,
#             "name": name,
#             "surname": surname,
#             "birthDate": str(birth_date.date()),
#             "deathDate": str(death_date.date()),
#             "pesel": str(pesel)  
#         })

transportDetails = []
for i in range(700):
      streetName = random.choice(streets)
      streetNr= random.randint(1,100)
      _id = f"{streetName}{streetNr}"
      houseNr =  random.randint(1,100)
      postalCode=  f"{random.randint(29,32)}-{random.randint(100,600)}"
      car = random.choice(cars)
      driver = random.choice(drivers)
      transportDetails.append({
      "_id": _id,
      "pickUpLocation": {
        "town": "Kraków",
        "streetName": streetName, 
        "streetNr": streetName,
        "houseNr": houseNr,
        "postalCode": postalCode},
      "car": car,
      "driver": drivers})
    



## generator

#printy
# print(deceasedInfo)
# print(funeralDetails)
# print(FuneralList)
#print(transportDetails)