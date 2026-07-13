const express = require("express");
const multer = require("multer");
const path = require("path");
const fs = require("fs");
const crypto = require("crypto");

const questions = require("./data/questions");

const ROOT = __dirname;
const STORE_PATH = path.join(ROOT, "data", "store.json");
const UPLOADS_DIR = path.join(ROOT, "uploads");

if (!fs.existsSync(UPLOADS_DIR)) fs.mkdirSync(UPLOADS_DIR, { recursive: true });
if (!fs.existsSync(STORE_PATH)) {
  fs.writeFileSync(STORE_PATH, JSON.stringify({ scores: [], photos: [] }, null, 2));
}

function readStore() {
  return JSON.parse(fs.readFileSync(STORE_PATH, "utf8"));
}

function writeStore(store) {
  fs.writeFileSync(STORE_PATH, JSON.stringify(store, null, 2));
}

const app = express();
app.use(express.json());
app.use(express.static(path.join(ROOT, "public")));
app.use("/uploads", express.static(UPLOADS_DIR));

// --- Quiz ---

app.get("/api/questions", (req, res) => {
  const category = req.query.category || "mix";
  const count = Math.min(parseInt(req.query.count, 10) || 10, 30);
  const lang = req.query.lang === "he" ? "he" : "fr";

  let pool = questions;
  if (category === "village" || category === "turin") {
    pool = questions.filter((q) => q.category === category);
  }

  const shuffled = [...pool].sort(() => Math.random() - 0.5).slice(0, count);
  const localized = shuffled.map((q) => ({
    id: q.id,
    category: q.category,
    question: q.question[lang],
    options: q.options[lang],
    answerIndex: q.answerIndex,
    funFact: q.funFact[lang],
  }));
  res.json(localized);
});

app.post("/api/scores", (req, res) => {
  const { nickname, category, score, total } = req.body || {};
  if (!nickname || typeof score !== "number" || typeof total !== "number") {
    return res.status(400).json({ error: "nickname, score et total sont requis" });
  }

  const store = readStore();
  const entry = {
    id: crypto.randomUUID(),
    nickname: String(nickname).trim().slice(0, 30),
    category: category || "mix",
    score,
    total,
    createdAt: new Date().toISOString(),
  };
  store.scores.push(entry);
  writeStore(store);
  res.status(201).json(entry);
});

app.get("/api/leaderboard", (req, res) => {
  const store = readStore();
  const category = req.query.category;
  let scores = store.scores;
  if (category) scores = scores.filter((s) => s.category === category);

  scores = [...scores].sort((a, b) => {
    const ratioA = a.score / a.total;
    const ratioB = b.score / b.total;
    if (ratioB !== ratioA) return ratioB - ratioA;
    return new Date(b.createdAt) - new Date(a.createdAt);
  });

  res.json(scores.slice(0, 50));
});

// --- Photos ---

const storage = multer.diskStorage({
  destination: (req, file, cb) => cb(null, UPLOADS_DIR),
  filename: (req, file, cb) => {
    const ext = path.extname(file.originalname || "").slice(0, 10) || ".jpg";
    cb(null, `${crypto.randomUUID()}${ext}`);
  },
});

const upload = multer({
  storage,
  limits: { fileSize: 15 * 1024 * 1024 },
  fileFilter: (req, file, cb) => {
    if (!file.mimetype.startsWith("image/")) {
      return cb(new Error("Seules les images sont acceptees"));
    }
    cb(null, true);
  },
});

app.get("/api/photos", (req, res) => {
  const store = readStore();
  const photos = [...store.photos].sort(
    (a, b) => new Date(b.createdAt) - new Date(a.createdAt)
  );
  res.json(photos);
});

app.post("/api/photos", upload.single("photo"), (req, res) => {
  if (!req.file) return res.status(400).json({ error: "Photo manquante" });

  const nickname = String(req.body.nickname || "Anonyme").trim().slice(0, 30);
  const caption = String(req.body.caption || "").trim().slice(0, 200);

  const store = readStore();
  const entry = {
    id: crypto.randomUUID(),
    nickname,
    caption,
    url: `/uploads/${req.file.filename}`,
    createdAt: new Date().toISOString(),
  };
  store.photos.push(entry);
  writeStore(store);
  res.status(201).json(entry);
});

app.use((err, req, res, next) => {
  console.error(err);
  res.status(400).json({ error: err.message || "Erreur serveur" });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, "0.0.0.0", () => {
  console.log(`Pragelato Quiz lance sur http://localhost:${PORT}`);
  console.log("Accessible depuis les telephones sur le meme wifi via l'IP de cet ordinateur.");
});
