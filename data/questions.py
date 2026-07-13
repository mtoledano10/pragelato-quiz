# Questions de depart pour le quiz Pragelato / Turin, en francais et en hebreu.
# A relire et adapter avant le sejour (infos village qui peuvent evoluer d'une saison a l'autre).
#
# Format de chaque question :
# {
#     "id": identifiant unique (str),
#     "category": "village" ou "turin",
#     "question": {"fr": "...", "he": "..."},
#     "options": {"fr": [4 propositions], "he": [4 propositions, MEME ORDRE que fr]},
#     "answer_index": index (0 a 3) de la bonne reponse (identique pour fr et he),
#     "fun_fact": {"fr": "...", "he": "..."},
# }
#
# IMPORTANT : les options fr et he doivent rester dans le meme ordre, car answer_index
# est partage entre les deux langues.
#
# Pour ajouter une question : copier un bloc, changer l'id (unique), remplir les champs.

QUESTIONS = [
    # --- Village Club Med Pragelato Vialattea ---
    {
        "id": "v1",
        "category": "village",
        "question": {
            "fr": "Dans quel pays se trouve le village Club Med de Pragelato ?",
            "he": "באיזו מדינה נמצא כפר הקלאב מד פראג'לאטו?",
        },
        "options": {
            "fr": ["France", "Italie", "Suisse", "Autriche"],
            "he": ["צרפת", "איטליה", "שווייץ", "אוסטריה"],
        },
        "answer_index": 1,
        "fun_fact": {
            "fr": "Pragelato est dans le Piemont, dans les Alpes italiennes.",
            "he": "פראג'לאטו נמצא באזור פיימונטה, באלפים האיטלקיים.",
        },
    },
    {
        "id": "v2",
        "category": "village",
        "question": {
            "fr": "A quelle altitude environ se situe le village ?",
            "he": "באיזה גובה בקירוב נמצא הכפר?",
        },
        "options": {
            "fr": ["1 200 m", "1 600 m", "2 200 m", "2 800 m"],
            "he": ["1,200 מ'", "1,600 מ'", "2,200 מ'", "2,800 מ'"],
        },
        "answer_index": 1,
        "fun_fact": {
            "fr": "Le village est niche a 1 600 metres, au calme dans sa vallee.",
            "he": "הכפר שוכן בגובה 1,600 מטר, בשקט עמקו.",
        },
    },
    {
        "id": "v3",
        "category": "village",
        "question": {
            "fr": "Comment s'appelle le domaine skiable auquel appartient Pragelato ?",
            "he": "מה שמו של תחום הסקי שאליו שייך פראג'לאטו?",
        },
        "options": {
            "fr": ["Via Lattea (la Voie Lactee)", "Via Roma", "Via Aurelia", "Via Dolomiti"],
            "he": ["ויה לאטאה (\"שביל החלב\")", "ויה רומא", "ויה אאורליה", "ויה דולומיטי"],
        },
        "answer_index": 0,
        "fun_fact": {
            "fr": "\"Via Lattea\" signifie Voie Lactee en italien : un des plus grands domaines relies d'Europe.",
            "he": "\"ויה לאטאה\" פירושו שביל החלב באיטלקית - אחד מתחומי הסקי המחוברים הגדולים באירופה.",
        },
    },
    {
        "id": "v4",
        "category": "village",
        "question": {
            "fr": "Le domaine Via Lattea, ce sont environ combien de km de pistes ?",
            "he": "לתחום הסקי ויה לאטאה יש בסביבות כמה ק\"מ של מסלולים?",
        },
        "options": {
            "fr": ["150 km", "250 km", "400 km", "600 km"],
            "he": ["150 ק\"מ", "250 ק\"מ", "400 ק\"מ", "600 ק\"מ"],
        },
        "answer_index": 2,
        "fun_fact": {
            "fr": "Environ 400 km de pistes reliees entre plusieurs stations italiennes.",
            "he": "כ-400 ק\"מ של מסלולים מחוברים בין כמה אתרי סקי איטלקיים.",
        },
    },
    {
        "id": "v5",
        "category": "village",
        "question": {
            "fr": "Autour de quoi les chalets du village sont-ils disposes ?",
            "he": "סביב מה בנויים הצ'אלטים של הכפר?",
        },
        "options": {
            "fr": ["Une fontaine du village", "Un lac", "Une eglise", "Un manege"],
            "he": ["מזרקה של הכפר", "אגם", "כנסייה", "קרוסלה"],
        },
        "answer_index": 0,
        "fun_fact": {
            "fr": "L'ambiance rappelle un authentique hameau de montagne, autour de sa fontaine.",
            "he": "האווירה מזכירה כפר הרים אותנטי, סביב המזרקה שלו.",
        },
    },
    {
        "id": "v6",
        "category": "village",
        "question": {
            "fr": "Combien de restaurants compte le village (restaurant d'altitude inclus) ?",
            "he": "כמה מסעדות יש בכפר (כולל מסעדת הגובה)?",
        },
        "options": {
            "fr": ["2", "3", "4", "6"],
            "he": ["2", "3", "4", "6"],
        },
        "answer_index": 2,
        "fun_fact": {
            "fr": "3 restaurants au village + 1 restaurant d'altitude sur les pistes.",
            "he": "3 מסעדות בכפר + מסעדת גובה אחת על המסלולים.",
        },
    },
    {
        "id": "v7",
        "category": "village",
        "question": {
            "fr": "Comment s'appelle l'endroit ou l'on peut boire un verre et gouter des specialites du Piemont ?",
            "he": "איך נקרא המקום שבו אפשר לשתות משהו ולטעום ממטעמי פיימונטה?",
        },
        "options": {
            "fr": ["La Trattoria", "Le Bistrot", "La Piazza", "Le Chalet"],
            "he": ["לה טראטוריה", "לה ביסטרו", "לה פיאצה", "הצ'אלט"],
        },
        "answer_index": 0,
        "fun_fact": {
            "fr": "La Trattoria, sur la place du village, propose les specialites piemontaises.",
            "he": "לה טראטוריה, בכיכר הכפר, מציעה את מיטב המטעמים הפיימונטיים.",
        },
    },
    {
        "id": "v8",
        "category": "village",
        "question": {
            "fr": "Quel type de pizza est propose au restaurant du village ?",
            "he": "איזה סוג פיצה מוגש במסעדת הכפר?",
        },
        "options": {
            "fr": ["Surgelee", "Cuite au feu de bois", "Cuite a la vapeur", "Precuite"],
            "he": ["קפואה", "אפויה בתנור עצים", "מבושלת באדים", "אפויה מראש"],
        },
        "answer_index": 1,
        "fun_fact": {
            "fr": "Pizzas au feu de bois et cuisine italienne authentique sont a l'honneur.",
            "he": "פיצות אפויות בתנור עצים ומטבח איטלקי אותנטי הם חלק מהחוויה.",
        },
    },
    {
        "id": "v9",
        "category": "village",
        "question": {
            "fr": "Combien de snowparks propose le domaine Via Lattea ?",
            "he": "כמה סנואפארקים יש בתחום הסקי ויה לאטאה?",
        },
        "options": {
            "fr": ["2", "4", "6", "10"],
            "he": ["2", "4", "6", "10"],
        },
        "answer_index": 2,
        "fun_fact": {
            "fr": "6 snowparks sont repartis sur l'ensemble du domaine.",
            "he": "6 סנואפארקים פרוסים לאורך כל התחום.",
        },
    },
    {
        "id": "v10",
        "category": "village",
        "question": {
            "fr": "Quelle station voisine, qui a accueilli des epreuves des Jeux Olympiques d'hiver de 2006, est reliee au domaine ?",
            "he": "איזה אתר סקי שכן, שבו התקיימו תחרויות באולימפיאדת החורף 2006, מחובר לתחום?",
        },
        "options": {
            "fr": ["Cortina d'Ampezzo", "Sestriere", "Courmayeur", "Bormio"],
            "he": ["קורטינה ד'אמפצו", "ססטריירה", "קורמאייר", "בורמיו"],
        },
        "answer_index": 1,
        "fun_fact": {
            "fr": "Sestriere a accueilli les epreuves de ski alpin des JO de Turin 2006.",
            "he": "בססטריירה נערכו תחרויות הסקי האלפיני של אולימפיאדת טורינו 2006.",
        },
    },
    {
        "id": "v11",
        "category": "village",
        "question": {
            "fr": "Combien de remontees mecaniques compte environ le domaine Via Lattea ?",
            "he": "בקירוב, כמה מתקני הרמה יש בתחום ויה לאטאה?",
        },
        "options": {
            "fr": ["40", "65", "92", "120"],
            "he": ["40", "65", "92", "120"],
        },
        "answer_index": 2,
        "fun_fact": {
            "fr": "Environ 92 remontees mecaniques desservent le domaine.",
            "he": "כ-92 מתקני הרמה משרתים את התחום.",
        },
    },
    {
        "id": "v12",
        "category": "village",
        "question": {
            "fr": "Dans quelle region d'Italie se trouve Pragelato ?",
            "he": "באיזה אזור באיטליה נמצא פראג'לאטו?",
        },
        "options": {
            "fr": ["Piemont", "Toscane", "Venetie", "Ombrie"],
            "he": ["פיימונטה", "טוסקנה", "ונטו", "אומבריה"],
        },
        "answer_index": 0,
        "fun_fact": {
            "fr": "Le Piemont est aussi la region de Turin, sa capitale.",
            "he": "פיימונטה הוא גם האזור שבו נמצאת טורינו, בירתו.",
        },
    },
    # --- Ville de Turin ---
    {
        "id": "t1",
        "category": "turin",
        "question": {
            "fr": "Quel est le monument symbole de Turin ?",
            "he": "מהו הסמל המזוהה ביותר עם העיר טורינו?",
        },
        "options": {
            "fr": ["La Mole Antonelliana", "Le Colisee", "La Tour de Pise", "Le Duomo"],
            "he": ["מולה אנטונליאנה", "הקולוסיאום", "מגדל פיזה", "הדואומו"],
        },
        "answer_index": 0,
        "fun_fact": {
            "fr": "La Mole Antonelliana est visible sur la piece italienne de 2 centimes d'euro.",
            "he": "מולה אנטונליאנה מופיעה על מטבע האירו האיטלקי של 2 סנט.",
        },
    },
    {
        "id": "t2",
        "category": "turin",
        "question": {
            "fr": "Quelle est la hauteur approximative de la Mole Antonelliana ?",
            "he": "מה גובהה בקירוב של מולה אנטונליאנה?",
        },
        "options": {
            "fr": ["100 m", "167 m", "230 m", "300 m"],
            "he": ["100 מ'", "167 מ'", "230 מ'", "300 מ'"],
        },
        "answer_index": 1,
        "fun_fact": {
            "fr": "Avec ses 167,5 m, c'est l'un des plus hauts batiments-musees du monde.",
            "he": "בגובה 167.5 מטר, זהו אחד מבנייני-המוזיאון הגבוהים בעולם.",
        },
    },
    {
        "id": "t3",
        "category": "turin",
        "question": {
            "fr": "A l'origine, la Mole Antonelliana devait etre...",
            "he": "במקור, מולה אנטונליאנה הייתה אמורה לשמש כ...",
        },
        "options": {
            "fr": ["Une synagogue", "Une gare", "Un palais royal", "Une caserne"],
            "he": ["בית כנסת", "תחנת רכבת", "ארמון מלכותי", "קסרקטין"],
        },
        "answer_index": 0,
        "fun_fact": {
            "fr": "Commandee en 1863 pour la communaute juive de Turin, avant de changer de destination.",
            "he": "היא הוזמנה ב-1863 עבור הקהילה היהודית של טורינו, לפני ששינתה ייעוד.",
        },
    },
    {
        "id": "t4",
        "category": "turin",
        "question": {
            "fr": "Quel musee abrite aujourd'hui la Mole Antonelliana ?",
            "he": "איזה מוזיאון שוכן כיום בתוך מולה אנטונליאנה?",
        },
        "options": {
            "fr": [
                "Le Musee national du cinema",
                "Le Musee egyptien",
                "Le Musee de l'automobile",
                "Le Musee des sciences",
            ],
            "he": ["המוזיאון הלאומי לקולנוע", "המוזיאון המצרי", "מוזיאון המכוניות", "מוזיאון המדע"],
        },
        "answer_index": 0,
        "fun_fact": {
            "fr": "Un ascenseur panoramique monte a 85 m pour une vue imprenable sur la ville et les Alpes.",
            "he": "מעלית פנורמית מגיעה לגובה 85 מ' לתצפית מרהיבה על העיר והאלפים.",
        },
    },
    {
        "id": "t5",
        "category": "turin",
        "question": {
            "fr": "Le Musee egyptien de Turin est particulierement connu car...",
            "he": "המוזיאון המצרי בטורינו ידוע במיוחד בזכות מה?",
        },
        "options": {
            "fr": [
                "C'est le seul musee hors d'Egypte entierement dedie a l'Egypte ancienne",
                "C'est le plus grand musee d'art moderne d'Italie",
                "Il n'expose que des copies",
                "Il a ouvert en 2020",
            ],
            "he": [
                "הוא המוזיאון היחיד מחוץ למצרים המוקדש כולו למצרים העתיקה",
                "הוא מוזיאון האמנות המודרנית הגדול באיטליה",
                "הוא מציג רק העתקים",
                "הוא נפתח בשנת 2020",
            ],
        },
        "answer_index": 0,
        "fun_fact": {
            "fr": "Il possede l'une des plus importantes collections egyptiennes au monde, apres celle du Caire.",
            "he": "יש בו אחד מהאוספים המצריים החשובים בעולם, מיד אחרי זה שבקהיר.",
        },
    },
    {
        "id": "t6",
        "category": "turin",
        "question": {
            "fr": "Turin est parfois surnommee...",
            "he": "טורינו מכונה לעיתים...",
        },
        "options": {
            "fr": ["Le petit Paris", "La petite Venise", "Le petit Londres", "La petite Rome"],
            "he": ["הפריז הקטנה", "ונציה הקטנה", "לונדון הקטנה", "רומא הקטנה"],
        },
        "answer_index": 0,
        "fun_fact": {
            "fr": "Ses places elegantes et son architecture baroque lui valent ce surnom.",
            "he": "הכיכרות האלגנטיות והאדריכלות הבארוקית העניקו לה את הכינוי הזה.",
        },
    },
    {
        "id": "t7",
        "category": "turin",
        "question": {
            "fr": "Quel celebre club de football a son musee a Turin ?",
            "he": "לאיזו קבוצת כדורגל מפורסמת יש מוזיאון בטורינו?",
        },
        "options": {
            "fr": ["AC Milan", "Juventus", "AS Roma", "Inter Milan"],
            "he": ["מילאן", "יובנטוס", "רומא", "אינטר מילאנו"],
        },
        "answer_index": 1,
        "fun_fact": {
            "fr": "Le Juventus Stadium et son musee retracent l'histoire du club.",
            "he": "אצטדיון יובנטוס והמוזיאון שלו מספרים את תולדות המועדון.",
        },
    },
    {
        "id": "t8",
        "category": "turin",
        "question": {
            "fr": "En quelle annee Turin a-t-elle accueilli les Jeux Olympiques d'hiver ?",
            "he": "באיזו שנה אירחה טורינו את אולימפיאדת החורף?",
        },
        "options": {
            "fr": ["1998", "2002", "2006", "2010"],
            "he": ["1998", "2002", "2006", "2010"],
        },
        "answer_index": 2,
        "fun_fact": {
            "fr": "Les JO d'hiver de Turin 2006 ont aussi profite au domaine skiable voisin, la Via Lattea.",
            "he": "אולימפיאדת החורף של טורינו ב-2006 גם קידמה את תחום הסקי השכן, ויה לאטאה.",
        },
    },
    {
        "id": "t9",
        "category": "turin",
        "question": {
            "fr": "Quelle grande marque automobile italienne est nee a Turin ?",
            "he": "איזה מותג רכב איטלקי גדול נולד בטורינו?",
        },
        "options": {
            "fr": ["Ferrari", "Fiat", "Lamborghini", "Alfa Romeo"],
            "he": ["פרארי", "פיאט", "למבורגיני", "אלפא רומיאו"],
        },
        "answer_index": 1,
        "fun_fact": {
            "fr": "Fiat (Fabbrica Italiana Automobili Torino) est fondee a Turin en 1899.",
            "he": "פיאט (Fabbrica Italiana Automobili Torino) נוסדה בטורינו ב-1899.",
        },
    },
    {
        "id": "t10",
        "category": "turin",
        "question": {
            "fr": "Quelle boisson chaude typique, melange de cafe, chocolat et creme, est nee a Turin ?",
            "he": "איזה משקה חם אופייני, שילוב של קפה, שוקולד וקצפת, נולד בטורינו?",
        },
        "options": {
            "fr": ["Le Bicerin", "Le Spritz", "Le Cappuccino", "L'Affogato"],
            "he": ["ביצ'רין", "ספריץ", "קפוצ'ינו", "אפוגאטו"],
        },
        "answer_index": 0,
        "fun_fact": {
            "fr": "Le Bicerin se deguste dans les cafes historiques de Turin depuis le 18e siecle.",
            "he": "הביצ'רין מוגש בבתי הקפה ההיסטוריים של טורינו כבר מהמאה ה-18.",
        },
    },
    {
        "id": "t11",
        "category": "turin",
        "question": {
            "fr": "Quel fleuve traverse la ville de Turin ?",
            "he": "איזה נהר חוצה את העיר טורינו?",
        },
        "options": {
            "fr": ["Le Po", "Le Tibre", "L'Arno", "L'Adige"],
            "he": ["הפו", "הטיבר", "הארנו", "האדיג'ה"],
        },
        "answer_index": 0,
        "fun_fact": {
            "fr": "Le Po, le plus long fleuve d'Italie, prend sa source non loin de la region.",
            "he": "הפו, הנהר הארוך באיטליה, מקורו לא רחוק מהאזור.",
        },
    },
    {
        "id": "t12",
        "category": "turin",
        "question": {
            "fr": "Turin fut la toute premiere capitale de l'Italie unifiee, en quelle annee ?",
            "he": "טורינו הייתה הבירה הראשונה של איטליה המאוחדת - באיזו שנה?",
        },
        "options": {
            "fr": ["1848", "1861", "1900", "1922"],
            "he": ["1848", "1861", "1900", "1922"],
        },
        "answer_index": 1,
        "fun_fact": {
            "fr": "Turin fut capitale du royaume d'Italie de 1861 a 1865, avant Florence puis Rome.",
            "he": "טורינו הייתה בירת ממלכת איטליה בין 1861 ל-1865, לפני פירנצה ואז רומא.",
        },
    },
]
