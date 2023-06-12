from experta import Fact, Rule, KnowledgeEngine, AND, OR, NOT

# defined symptom list
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


class Symptom(Fact):
    """
    A class representing a symptom object that inherits from the Fact class.

    This class can be used to store and represent information about symptoms
    as objects in an application. It contains no additional methods or attributes
    other than those present in its parent Fact class.
    """

    pass


class Disease(Fact):
    """
    A class representing a disease object that inherits from the Fact class.

    This class can be used to store and represent information about diseases
    as objects in an application. It contains no additional methods or attributes
    other than those present in its parent Fact class.
    """

    pass


class DiagnosisEngine(KnowledgeEngine):
    """
    A class representing an expert system that uses rule-based reasoning to diagnose diseases based on
    the presented symptoms.

    This class inherits from the KnowledgeEngine class and contains multiple rules for different diseases.

    Attributes:
    None

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
        self.declare(Disease(name="grypa"))

    @Rule(
        AND(
            Symptom(name="kaszel"),
            Symptom(name="gorączka"),
            Symptom(name="duszność"),
            OR(Symptom(name="osłabienie"), NOT(Symptom(name="osłabienie"))),
            OR(
                Symptom(name="ból w klatce piersiowej"),
                NOT(Symptom(name="ból w klatce piersiowej")),
            ),
        )
    )
    def diagnoza_zapalenie_pluc(self):
        self.declare(Disease(name="zapalenie płuc"))

    @Rule(
        AND(
            Symptom(name="częste oddawanie moczu"),
            Symptom(name="niegasnące pragnienie"),
            Symptom(name="utrata masy ciała"),
            OR(Symptom(name="osłabienie"), NOT(Symptom(name="osłabienie"))),
            OR(
                Symptom(name="powolne gojenie się ran"),
                NOT(Symptom(name="powolne gojenie się ran")),
            ),
            OR(Symptom(name="częste infekcje"), NOT(Symptom(name="częste infekcje"))),
        )
    )
    def diagnoza_cukrzyca(self):
        self.declare(Disease(name="cukrzyca"))

    @Rule(
        AND(
            Symptom(name="podwyższone ciśnienie"),
            OR(Symptom(name="ból_głowy"), NOT(Symptom(name="ból_głowy"))),
            OR(Symptom(name="duszności"), NOT(Symptom(name="duszności"))),
            OR(Symptom(name="zawroty głowy"), NOT(Symptom(name="zawroty głowy"))),
            OR(
                Symptom(name="ból w klatce piersiowej"),
                NOT(Symptom(name="ból w klatce piersiowej")),
            ),
            OR(
                Symptom(name="kłopoty z widzeniem"),
                NOT(Symptom(name="kłopoty z widzeniem")),
            ),
        )
    )
    def diagnoza_nadcisnienie(self):
        self.declare(Disease(name="nadciśnienie tętnicze"))

    @Rule(
        AND(
            Symptom(name="ból w klatce piersiowej"),
            Symptom(name="uczucie ucisku"),
            Symptom(name="duszności"),
            OR(
                Symptom(name="ból promieniujący do ramienia"),
                NOT(Symptom(name="ból promieniujący do ramienia")),
            ),
            OR(Symptom(name="zasłabnięcia"), NOT(Symptom(name="zasłabnięcia"))),
        )
    )
    def diagnoza_choroba_wiencowa(self):
        self.declare(Disease(name="choroba wieńcowa"))

    @Rule(
        AND(
            Symptom(name="duszności"),
            Symptom(name="przewlekły kaszel"),
            Symptom(name="świsty podczas oddychania"),
            OR(
                Symptom(name="częste infekcje górnych dróg oddechowych"),
                NOT(Symptom(name="częste infekcje górnych dróg oddechowych")),
            ),
        )
    )
    def diagnoza_astma(self):
        self.declare(Disease(name="astma"))

    @Rule(
        AND(
            Symptom(name="urazy złamania kości"),
            OR(Symptom(name="utrata wysokości"), NOT(Symptom(name="utrata wysokości"))),
            OR(
                Symptom(name="zgarbiona postawa"),
                NOT(Symptom(name="zgarbiona postawa")),
            ),
        )
    )
    def diagnoza_osteoporoza(self):
        self.declare(Disease(name="osteoporoza"))

    @Rule(
        AND(
            Symptom(name="ból stawów"),
            Symptom(name="obrzęk stawów"),
            OR(Symptom(name="zmęczenie"), NOT(Symptom(name="zmęczenie"))),
            OR(Symptom(name="gorączka"), NOT(Symptom(name="gorączka"))),
        )
    )
    def diagnoza_zapalenie_stawow(self):
        self.declare(Disease(name="reumatoidalne zapalenie stawów"))

    @Rule(
        AND(
            Symptom(name="silny ból głowy"),
            Symptom(name="nadwrażlisość na światło, dźwiek lub zapach"),
            OR(Symptom(name="nudności"), NOT(Symptom(name="nudności"))),
            OR(Symptom(name="wymioty"), NOT(Symptom(name="wymioty"))),
        )
    )
    def diagnoza_migrena(self):
        self.declare(Disease(name="migrena"))

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
        self.declare(Disease(name="rak płuc"))


# Create an instance of the DiagnosisEngine class
engine = DiagnosisEngine()

# Reset the instance of the DiagnosisEngine class
engine.reset()


print(
    f"Cześć, jestem Twoim wirutalnym asystentem i na podstawie podanych przez Ciebie objawów postaram się określić na jaką chorobę cierpisz"
)


# Iterate through each symptom in the SYMPTOMS list
for item in SYMPTOMS:
    # Prompt the user for a confirmation on whether they are experiencing the current symptom
    while True:
        confirmed_symptom = input(
            f"Czy występuje/ą u Cibie takie objawy jak {item}? (TAK / NIE): "
        )
        # If the user confirms that they are or are not experiencing the symptom, declare it in the DiagnosisEngine
        if confirmed_symptom.lower() in ["tak", "nie"]:
            engine.declare(
                Symptom(name=item),
            )
            break
        # If the user inputs an invalid response, prompt them to try again
        else:
            print(f"Wprowadzono nie poprawną odpowiedź! Wpisz TAK lub NIE.")

engine.run()


for disease in engine.facts.values():
    if isinstance(disease, Disease):
        print(f"Diagnoza: {disease['name']}")

print("")
