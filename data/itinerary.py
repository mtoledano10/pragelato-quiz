# Programme du voyage (a adapter si le planning change).

ITINERARY_NOTES = {
    "fr": [
        "Merci de venir uniquement avec un trolley et un sac a dos : aucun bagage en soute n'est possible.",
        "Pensez a apporter votre ordinateur et tout le materiel necessaire pour le travail a distance (chargeurs, adaptateurs, ecouteurs, etc.).",
        "Verifiez que vous avez bien recu par email votre assurance voyage de la part de Caroline.",
    ],
    "he": [
        "כולם מתבקשים להגיע עם טרולי ותיק גב בלבד, אין אפשרות לשליחת כבודה לבטן המטוס.",
        "כולנו מגיעים עם מחשבים וכל הציוד הנדרש לעבודה מרחוק (מטענים, מתאמים, אוזניות וכו').",
        "יש לוודא שקיבלתם במייל ביטוח נסיעות מקרולין.",
    ],
}

ITINERARY_DAYS = [
    {
        "date": "14.07",
        "day_name": {"fr": "Dimanche", "he": "יום ראשון"},
        "items": [
            {"time": "06:15", "fr": "Decollage de Ben Gourion (Terminal 3)", "he": "המראה מנתב\"ג (טרמינל 3)"},
            {"time": "09:25", "fr": "Atterrissage a Milan", "he": "נחיתה במילאנו"},
            {"time": "10:30", "fr": "Depart vers Pragelato", "he": "יציאה לפרג'לטו"},
            {"time": "13:30", "fr": "Dejeuner", "he": "ארוחת צהריים"},
            {"time": "14:30-17:00", "fr": "Travail a distance", "he": "עבודה מרחוק"},
            {"time": "17:00-18:00", "fr": "Visite des chambres du Club", "he": "סיור חדרים במועדון"},
            {"time": "19:30", "fr": "Bar", "he": "בר"},
            {"time": "20:00", "fr": "Diner", "he": "ארוחת ערב"},
        ],
    },
    {
        "date": "15.07",
        "day_name": {"fr": "Lundi", "he": "יום שני"},
        "items": [
            {"time": "08:00", "fr": "Petit-dejeuner", "he": "ארוחת בוקר"},
            {"time": "09:00-12:30", "fr": "Travail a distance", "he": "עבודה מרחוק"},
            {"time": "12:30", "fr": "Dejeuner", "he": "ארוחת צהריים"},
            {"time": "14:00-16:00", "fr": "Randonnee nature guidee", "he": "טיול טבע מודרך"},
            {
                "time": "16:00-19:30",
                "fr": "Temps libre (possibilite de visiter Sestriere / profiter du Club / les deux)",
                "he": "זמן חופשי (אפשרות לביקור בססטרייר / בילוי במועדון / שילוב ביניהם)",
            },
            {"time": "19:30", "fr": "Bar", "he": "בר"},
            {"time": "20:00", "fr": "Diner", "he": "ארוחת ערב"},
        ],
    },
    {
        "date": "16.07",
        "day_name": {"fr": "Mardi", "he": "יום שלישי"},
        "items": [
            {"time": "08:00", "fr": "Petit-dejeuner", "he": "ארוחת בוקר"},
            {"time": "09:00-12:00", "fr": "Travail a distance", "he": "עבודה מרחוק"},
            {"time": "12:00", "fr": "Dejeuner", "he": "ארוחת צהריים"},
            {"time": "13:00", "fr": "Depart du Club", "he": "עזיבת המועדון"},
            {"time": "15:00", "fr": "Arrivee a Turin et visite sur place", "he": "הגעה לטורינו וסיור במקום"},
            {"time": "16:30", "fr": "Temps libre a Turin", "he": "זמן חופשי בטורינו"},
            {"time": "19:00", "fr": "Depart vers l'aeroport de Milan", "he": "יציאה לשדה התעופה במילאנו"},
            {"time": "21:00", "fr": "Arrivee a l'aeroport", "he": "הגעה לשדה"},
        ],
    },
]
