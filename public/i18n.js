const I18N = {
  fr: {
    appTitle: "🏔️ Pragelato & Turin",
    welcomeTitle: "Bienvenue !",
    welcomeSubtitle: "Un petit quiz pour decouvrir le village et la ville de Turin, entre collegues.",
    nicknameLabel: "Choisis un pseudo",
    nicknamePlaceholder: "Ex: Mika des Neiges",
    startBtn: "C'est parti !",
    homeGreeting: "Salut {name} 👋",
    homeSubtitle: "Qu'est-ce qu'on fait ?",
    cardVillageTitle: "Quiz Village",
    cardVillageSub: "Pragelato Vialattea",
    cardTurinTitle: "Quiz Turin",
    cardTurinSub: "La ville a decouvrir",
    cardMixTitle: "Quiz Mix",
    cardMixSub: "Un peu des deux",
    cardLeaderboardTitle: "Classement",
    cardLeaderboardSub: "Qui connait le mieux ?",
    cardGalleryTitle: "Galerie photo",
    cardGallerySub: "Souvenirs du groupe",
    changeNickname: "Changer de pseudo",
    quizProgress: "Question {current} / {total}",
    quizNext: "Suivant",
    quizSeeScore: "Voir mon score",
    quizQuit: "Quitter le quiz",
    resultPerfect: "Score parfait !",
    resultGreat: "Tres beau score !",
    resultGood: "Bien joue !",
    resultScoreLine: "{name}, tu as eu {score} / {total}",
    retryBtn: "Rejouer",
    homeBtn: "Accueil",
    leaderboardTitle: "🏆 Classement",
    tabAll: "Tout",
    tabVillage: "Village",
    tabTurin: "Turin",
    tabMix: "Mix",
    backBtn: "Retour",
    leaderboardEmpty: "Personne n'a encore joue dans cette categorie. Sois le premier !",
    galleryTitle: "📸 Galerie photo",
    galleryEmpty: "Aucune photo pour le moment. Ajoute la premiere avec le bouton +",
    galleryBy: "par {name}",
    addPhotoTitle: "Ajouter une photo",
    photoLabel: "Photo",
    captionLabel: "Legende (optionnel)",
    captionPlaceholder: "Ex: Vue sur le village au coucher du soleil",
    cancelBtn: "Annuler",
    publishBtn: "Publier",
    sending: "Envoi...",
    photoError: "Erreur lors de l'envoi de la photo",
  },
  he: {
    appTitle: "🏔️ פראג'לאטו וטורינו",
    welcomeTitle: "ברוכים הבאים!",
    welcomeSubtitle: "חידון קטן להכרות עם הכפר ועם העיר טורינו, בין עמיתים לעבודה.",
    nicknameLabel: "בחרו כינוי",
    nicknamePlaceholder: "לדוגמה: מיקה מההרים",
    startBtn: "יאללה, מתחילים!",
    homeGreeting: "היי {name} 👋",
    homeSubtitle: "מה עושים?",
    cardVillageTitle: "חידון הכפר",
    cardVillageSub: "פראג'לאטו ויה לאטאה",
    cardTurinTitle: "חידון טורינו",
    cardTurinSub: "העיר שמחכה לגילוי",
    cardMixTitle: "חידון מעורב",
    cardMixSub: "קצת משניהם",
    cardLeaderboardTitle: "טבלת דירוג",
    cardLeaderboardSub: "מי הכי בקיא?",
    cardGalleryTitle: "גלריית תמונות",
    cardGallerySub: "זכרונות מהקבוצה",
    changeNickname: "החלפת כינוי",
    quizProgress: "שאלה {current} מתוך {total}",
    quizNext: "הבא",
    quizSeeScore: "הצגת הניקוד שלי",
    quizQuit: "יציאה מהחידון",
    resultPerfect: "ניקוד מושלם!",
    resultGreat: "ניקוד מעולה!",
    resultGood: "כל הכבוד!",
    resultScoreLine: "{name}, קיבלת {score} מתוך {total}",
    retryBtn: "לשחק שוב",
    homeBtn: "מסך הבית",
    leaderboardTitle: "🏆 טבלת דירוג",
    tabAll: "הכל",
    tabVillage: "כפר",
    tabTurin: "טורינו",
    tabMix: "מעורב",
    backBtn: "חזרה",
    leaderboardEmpty: "עדיין אף אחד לא שיחק בקטגוריה הזו. היו הראשונים!",
    galleryTitle: "📸 גלריית תמונות",
    galleryEmpty: "עדיין אין תמונות. הוסיפו את הראשונה עם כפתור ה-+",
    galleryBy: "מאת {name}",
    addPhotoTitle: "הוספת תמונה",
    photoLabel: "תמונה",
    captionLabel: "כיתוב (לא חובה)",
    captionPlaceholder: "לדוגמה: נוף לכפר בשקיעה",
    cancelBtn: "ביטול",
    publishBtn: "פרסום",
    sending: "שולח...",
    photoError: "שגיאה בשליחת התמונה",
  },
};

const RTL_LANGS = new Set(["he"]);

function t(lang, key, vars) {
  const dict = I18N[lang] || I18N.fr;
  let str = dict[key] !== undefined ? dict[key] : (I18N.fr[key] || key);
  if (vars) {
    Object.entries(vars).forEach(([k, v]) => {
      str = str.replace(`{${k}}`, v);
    });
  }
  return str;
}

function applyStaticTranslations(lang) {
  document.documentElement.lang = lang;
  document.documentElement.dir = RTL_LANGS.has(lang) ? "rtl" : "ltr";

  document.querySelectorAll("[data-i18n]").forEach((el) => {
    el.textContent = t(lang, el.dataset.i18n);
  });
  document.querySelectorAll("[data-i18n-placeholder]").forEach((el) => {
    el.placeholder = t(lang, el.dataset.i18nPlaceholder);
  });
  document.querySelectorAll("#lang-switch .lang-btn").forEach((btn) => {
    btn.classList.toggle("active", btn.dataset.lang === lang);
  });
}
