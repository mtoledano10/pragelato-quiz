const NICK_KEY = "pragelato_nickname";
const LANG_KEY = "pragelato_lang";

const screens = {
  nickname: document.getElementById("screen-nickname"),
  home: document.getElementById("screen-home"),
  quiz: document.getElementById("screen-quiz"),
  result: document.getElementById("screen-result"),
  leaderboard: document.getElementById("screen-leaderboard"),
  gallery: document.getElementById("screen-gallery"),
};

const topbarUser = document.getElementById("topbar-user");
const fab = document.getElementById("fab-add-photo");

let state = {
  nickname: localStorage.getItem(NICK_KEY) || "",
  lang: localStorage.getItem(LANG_KEY) || "fr",
  quiz: { category: "mix", questions: [], index: 0, score: 0, answered: false },
};

function showScreen(name) {
  Object.entries(screens).forEach(([key, el]) => {
    el.hidden = key !== name;
  });
  fab.hidden = name !== "gallery";
  if (state.nickname) {
    topbarUser.hidden = false;
    topbarUser.textContent = state.nickname;
  } else {
    topbarUser.hidden = true;
  }
}

function goHome() {
  document.getElementById("home-greeting").textContent = t(state.lang, "homeGreeting", { name: state.nickname });
  showScreen("home");
}

// --- Langue ---

function setLang(lang) {
  state.lang = lang;
  localStorage.setItem(LANG_KEY, lang);
  applyStaticTranslations(lang);

  const currentScreen = Object.entries(screens).find(([, el]) => !el.hidden)?.[0];
  if (currentScreen === "home") goHome();
  else if (currentScreen === "leaderboard") openLeaderboard(state.leaderboardCategory || "");
  else if (currentScreen === "gallery") openGallery();
  else if (currentScreen === "quiz") goHome();
}

document.querySelectorAll("#lang-switch .lang-btn").forEach((btn) => {
  btn.addEventListener("click", () => setLang(btn.dataset.lang));
});

// --- Pseudo ---

document.getElementById("nickname-form").addEventListener("submit", (e) => {
  e.preventDefault();
  const value = document.getElementById("nickname-input").value.trim();
  if (!value) return;
  state.nickname = value;
  localStorage.setItem(NICK_KEY, value);
  goHome();
});

document.getElementById("change-nickname").addEventListener("click", () => {
  document.getElementById("nickname-input").value = state.nickname;
  showScreen("nickname");
});

// --- Navigation depuis l'accueil ---

document.querySelectorAll(".card-action").forEach((btn) => {
  btn.addEventListener("click", () => {
    const action = btn.dataset.action;
    if (action === "quiz") startQuiz(btn.dataset.category);
    if (action === "leaderboard") openLeaderboard();
    if (action === "gallery") openGallery();
  });
});

document.querySelectorAll("[data-back='home']").forEach((btn) => {
  btn.addEventListener("click", goHome);
});

// --- Quiz ---

async function startQuiz(category) {
  const res = await fetch(`/api/questions?category=${category}&count=8&lang=${state.lang}`);
  const questions = await res.json();
  state.quiz = { category, questions, index: 0, score: 0, answered: false };
  showScreen("quiz");
  renderQuestion();
}

function renderQuestion() {
  const { questions, index } = state.quiz;
  const q = questions[index];
  state.quiz.answered = false;

  document.getElementById("quiz-progress-fill").style.width =
    `${(index / questions.length) * 100}%`;
  document.getElementById("quiz-progress-label").textContent =
    t(state.lang, "quizProgress", { current: index + 1, total: questions.length });

  document.getElementById("quiz-question").textContent = q.question;
  document.getElementById("quiz-funfact").hidden = true;
  document.getElementById("quiz-next").hidden = true;

  const optionsEl = document.getElementById("quiz-options");
  optionsEl.innerHTML = "";
  q.options.forEach((opt, i) => {
    const b = document.createElement("button");
    b.className = "quiz-option";
    b.textContent = opt;
    b.addEventListener("click", () => answerQuestion(i));
    optionsEl.appendChild(b);
  });
}

function answerQuestion(choiceIndex) {
  if (state.quiz.answered) return;
  state.quiz.answered = true;

  const { questions, index } = state.quiz;
  const q = questions[index];
  const buttons = document.querySelectorAll("#quiz-options .quiz-option");

  buttons.forEach((b, i) => {
    b.disabled = true;
    if (i === q.answerIndex) b.classList.add("correct");
    else if (i === choiceIndex) b.classList.add("wrong");
  });

  if (choiceIndex === q.answerIndex) state.quiz.score += 1;

  const fact = document.getElementById("quiz-funfact");
  fact.hidden = false;
  fact.textContent = q.funFact || "";

  const nextBtn = document.getElementById("quiz-next");
  nextBtn.hidden = false;
  nextBtn.textContent = index + 1 < questions.length
    ? t(state.lang, "quizNext")
    : t(state.lang, "quizSeeScore");
}

document.getElementById("quiz-next").addEventListener("click", () => {
  state.quiz.index += 1;
  if (state.quiz.index < state.quiz.questions.length) {
    renderQuestion();
  } else {
    finishQuiz();
  }
});

document.getElementById("quiz-quit").addEventListener("click", goHome);

async function finishQuiz() {
  const { score, questions, category } = state.quiz;
  const total = questions.length;

  document.getElementById("result-score").textContent =
    t(state.lang, "resultScoreLine", { name: state.nickname, score, total });
  const ratio = total ? score / total : 0;
  document.getElementById("result-emoji").textContent =
    ratio === 1 ? "🏆" : ratio >= 0.7 ? "🎉" : ratio >= 0.4 ? "👍" : "🙂";
  document.getElementById("result-title").textContent =
    ratio === 1 ? t(state.lang, "resultPerfect") : ratio >= 0.7 ? t(state.lang, "resultGreat") : t(state.lang, "resultGood");

  showScreen("result");

  try {
    await fetch("/api/scores", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ nickname: state.nickname, category, score, total }),
    });
  } catch (err) {
    console.error("Impossible d'enregistrer le score", err);
  }
}

document.getElementById("result-retry").addEventListener("click", () => {
  startQuiz(state.quiz.category);
});
document.getElementById("result-home").addEventListener("click", goHome);

// --- Classement ---

async function openLeaderboard(category = "") {
  state.leaderboardCategory = category;
  showScreen("leaderboard");
  document.querySelectorAll("#leaderboard-tabs .tab").forEach((tabEl) => {
    tabEl.classList.toggle("active", tabEl.dataset.category === category);
  });

  const res = await fetch(`/api/leaderboard${category ? `?category=${category}` : ""}`);
  const scores = await res.json();
  const list = document.getElementById("leaderboard-list");
  list.innerHTML = "";

  if (!scores.length) {
    const empty = document.createElement("div");
    empty.className = "empty-state";
    empty.textContent = t(state.lang, "leaderboardEmpty");
    list.appendChild(empty);
    return;
  }

  const categoryKey = { village: "tabVillage", turin: "tabTurin", mix: "tabMix" };
  const dateLocale = state.lang === "he" ? "he-IL" : "fr-FR";

  scores.forEach((s, i) => {
    const item = document.createElement("div");
    item.className = "list-item";
    const date = new Date(s.createdAt);
    const catLabel = t(state.lang, categoryKey[s.category] || "tabMix");
    item.innerHTML = `
      <span class="list-rank">#${i + 1}</span>
      <span class="list-name">${escapeHtml(s.nickname)}<br><span class="list-meta">${escapeHtml(catLabel)} - ${date.toLocaleDateString(dateLocale)}</span></span>
      <span class="list-score">${s.score}/${s.total}</span>
    `;
    list.appendChild(item);
  });
}

document.querySelectorAll("#leaderboard-tabs .tab").forEach((tab) => {
  tab.addEventListener("click", () => openLeaderboard(tab.dataset.category));
});

// --- Galerie ---

async function openGallery() {
  showScreen("gallery");
  const res = await fetch("/api/photos");
  const photos = await res.json();
  const grid = document.getElementById("gallery-grid");
  grid.innerHTML = "";

  if (!photos.length) {
    const empty = document.createElement("div");
    empty.className = "empty-state";
    empty.textContent = t(state.lang, "galleryEmpty");
    grid.appendChild(empty);
    return;
  }

  photos.forEach((p) => {
    const item = document.createElement("div");
    item.className = "gallery-item";
    item.innerHTML = `
      <img src="${p.url}" alt="${escapeHtml(p.caption || "photo")}" loading="lazy" />
      ${p.caption ? `<div class="gallery-caption">${escapeHtml(p.caption)}</div>` : ""}
      <div class="gallery-nickname">${escapeHtml(t(state.lang, "galleryBy", { name: p.nickname }))}</div>
    `;
    grid.appendChild(item);
  });
}

const photoModal = document.getElementById("photo-modal");
fab.addEventListener("click", () => {
  photoModal.hidden = false;
});
document.getElementById("photo-cancel").addEventListener("click", () => {
  photoModal.hidden = true;
});

document.getElementById("photo-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const fileInput = document.getElementById("photo-file");
  const caption = document.getElementById("photo-caption").value.trim();
  if (!fileInput.files[0]) return;

  const formData = new FormData();
  formData.append("photo", fileInput.files[0]);
  formData.append("nickname", state.nickname);
  formData.append("caption", caption);

  const submitBtn = e.target.querySelector("button[type='submit']");
  const originalLabel = submitBtn.textContent;
  submitBtn.disabled = true;
  submitBtn.textContent = t(state.lang, "sending");

  try {
    await fetch("/api/photos", { method: "POST", body: formData });
    photoModal.hidden = true;
    e.target.reset();
    openGallery();
  } catch (err) {
    alert(t(state.lang, "photoError"));
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = originalLabel;
  }
});

function escapeHtml(str) {
  const div = document.createElement("div");
  div.textContent = str;
  return div.innerHTML;
}

// --- Demarrage ---

applyStaticTranslations(state.lang);

if (state.nickname) {
  goHome();
} else {
  showScreen("nickname");
}
