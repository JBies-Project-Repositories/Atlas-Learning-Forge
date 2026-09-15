/**
 * Atlas of the Build Loop — multi-deck practice quiz
 * - Practice: instant feedback under choice
 * - Exam: no feedback until submit; optional timer (15-min steps or Off)
 * - Shuffle questions + unlabeled options every reshuffle/start
 * - Weak-area tracking in localStorage
 */

(function () {
  "use strict";

  const STORAGE_KEY = "atlas_build_loop_weak_v1";
  const bank = Array.isArray(window.QUESTIONS) ? window.QUESTIONS : [];

  const quizEl = document.getElementById("quiz");
  const filterEl = document.getElementById("lessonFilter");
  const modeSelect = document.getElementById("modeSelect");
  const timerSelect = document.getElementById("timerSelect");
  const examSizeSelect = document.getElementById("examSizeSelect");
  const progressText = document.getElementById("progressText");
  const scoreText = document.getElementById("scoreText");
  const timerDisplay = document.getElementById("timerDisplay");
  const modeHint = document.getElementById("modeHint");
  const btnReshuffle = document.getElementById("btnReshuffle");
  const btnReset = document.getElementById("btnReset");
  const btnStartExam = document.getElementById("btnStartExam");
  const btnSubmitExam = document.getElementById("btnSubmitExam");
  const btnWeakReport = document.getElementById("btnWeakReport");
  const weakPanel = document.getElementById("weakPanel");
  const examResults = document.getElementById("examResults");

  /** @type {{q: object, options: object[], answerKey: string|null}[]} */
  let session = [];
  /** practice | exam */
  let mode = "practice";
  /** exam not started yet when true in exam mode */
  let examArmed = false;
  let examSubmitted = false;
  let timerSecondsLeft = 0;
  let timerId = null;

  function shuffle(arr) {
    const a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  function loadStats() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
    } catch {
      return {};
    }
  }

  function saveStats(stats) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(stats));
  }

  function recordAnswer(q, correct) {
    const stats = loadStats();
    const id = q.id;
    if (!stats[id]) {
      stats[id] = {
        lessonId: q.lessonId,
        lesson: q.lesson,
        objective: q.objective || "",
        tries: 0,
        wrong: 0,
      };
    }
    stats[id].tries += 1;
    if (!correct) stats[id].wrong += 1;
    stats[id].lastAt = new Date().toISOString();
    saveStats(stats);
    if (typeof recordProgressEvent === "function") recordProgressEvent("answer", { id: q.id });
  }

  function lessonsFromBank() {
    const map = new Map();
    for (const q of bank) {
      if (!map.has(q.lessonId)) map.set(q.lessonId, q.lesson);
    }
    return [...map.entries()];
  }

  function parseDeckQuery() {
    try {
      const raw = new URLSearchParams(window.location.search).get("decks");
      if (!raw) return null;
      if (raw === "all") return "all";
      const ids = raw.split(",").map((s) => s.trim()).filter(Boolean);
      return ids.length ? ids : null;
    } catch { return null; }
  }
  let urlDeckSelection = parseDeckQuery();

  function populateFilter() {
    const lessons = lessonsFromBank();
    filterEl.innerHTML = "";
    const all = document.createElement("option");
    all.value = "all";
    all.textContent = `All decks (${bank.length} questions)`;
    filterEl.appendChild(all);
    if (Array.isArray(urlDeckSelection) && urlDeckSelection.length > 1) {
      const custom = document.createElement("option");
      custom.value = "__multi__";
      const n = bank.filter((q) => urlDeckSelection.includes(q.lessonId)).length;
      custom.textContent = `Chosen decks (${urlDeckSelection.length} · ${n} Qs)`;
      filterEl.appendChild(custom);
    }
    for (const [id, name] of lessons) {
      const count = bank.filter((q) => q.lessonId === id).length;
      const opt = document.createElement("option");
      opt.value = id;
      opt.textContent = `${name} (${count})`;
      filterEl.appendChild(opt);
    }
    if (urlDeckSelection === "all") filterEl.value = "all";
    else if (Array.isArray(urlDeckSelection) && urlDeckSelection.length === 1) filterEl.value = urlDeckSelection[0];
    else if (Array.isArray(urlDeckSelection) && urlDeckSelection.length > 1) filterEl.value = "__multi__";
  }

  function filteredBank() {
    const id = filterEl.value;
    if (id === "all") return bank.slice();
    if (id === "__multi__" && Array.isArray(urlDeckSelection)) {
      return bank.filter((q) => urlDeckSelection.includes(q.lessonId));
    }
    return bank.filter((q) => q.lessonId === id);
  }

  function recordProgressEvent(kind, detail) {
    try {
      const key = "atlas_build_loop_progress_v1";
      const data = JSON.parse(localStorage.getItem(key) || "{}");
      data.quiz = data.quiz || { sessions: 0, answered: 0, ids: [], lastAt: null };
      data.quiz.ids = Array.isArray(data.quiz.ids) ? data.quiz.ids : [];
      if (kind === "answer" && detail && detail.id) {
        if (!data.quiz.ids.includes(detail.id)) data.quiz.ids.push(detail.id);
        data.quiz.answered = data.quiz.ids.length;
        data.quiz.lastAt = new Date().toISOString();
      }
      localStorage.setItem(key, JSON.stringify(data));
    } catch (e) {}
  }

  function buildSession(limit) {
    let questions = shuffle(filteredBank());
    if (limit && limit > 0 && questions.length > limit) {
      questions = questions.slice(0, limit);
    }
    session = questions.map((q) => {
      const options = shuffle(
        q.options.map((o, idx) => ({
          ...o,
          key: `${q.id}-opt-${idx}-${Math.random().toString(36).slice(2, 7)}`,
        }))
      );
      return { q, options, answerKey: null };
    });
  }

  function stopTimer() {
    if (timerId) {
      clearInterval(timerId);
      timerId = null;
    }
  }

  function formatTime(sec) {
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return `${m}:${String(s).padStart(2, "0")}`;
  }

  function updateTimerDisplay() {
    const mins = Number(timerSelect.value) || 0;
    if (mins <= 0) {
      timerDisplay.classList.add("is-hidden");
      timerDisplay.textContent = "";
      return;
    }
    timerDisplay.classList.remove("is-hidden");
    if (timerId || (mode === "exam" && examArmed && !examSubmitted)) {
      timerDisplay.textContent = `Time ${formatTime(timerSecondsLeft)}`;
      timerDisplay.classList.toggle("timer-low", timerSecondsLeft > 0 && timerSecondsLeft <= 60);
    } else if (mode === "practice") {
      timerDisplay.textContent = `Timer ready: ${mins} min`;
      timerDisplay.classList.remove("timer-low");
    } else {
      timerDisplay.textContent = `Timer: ${mins} min (starts with exam)`;
      timerDisplay.classList.remove("timer-low");
    }
  }

  function startTimerIfNeeded() {
    stopTimer();
    const mins = Number(timerSelect.value) || 0;
    if (mins <= 0) {
      updateTimerDisplay();
      return;
    }
    timerSecondsLeft = mins * 60;
    updateTimerDisplay();
    timerId = setInterval(() => {
      timerSecondsLeft -= 1;
      if (timerSecondsLeft <= 0) {
        timerSecondsLeft = 0;
        updateTimerDisplay();
        stopTimer();
        if (mode === "exam" && !examSubmitted) {
          submitExam(true);
        } else if (mode === "practice") {
          alert("Timer finished.");
        }
        return;
      }
      updateTimerDisplay();
    }, 1000);
  }

  function updateModeUI() {
    mode = modeSelect.value;
    const exam = mode === "exam";
    btnStartExam.classList.toggle("is-hidden", !exam);
    btnSubmitExam.classList.toggle("is-hidden", !exam);
    btnReshuffle.classList.toggle("is-hidden", exam && examArmed && !examSubmitted);
    examSizeSelect.disabled = !exam;
    if (exam) {
      modeHint.textContent =
        "Exam mode: answers stay hidden until you click Submit. Set Timer to Off or 15 / 30 / 45 / 60 minutes. Start exam shuffles a set; Submit grades everything. Unanswered items are skipped (not counted as answers).";
    } else {
      modeHint.textContent =
        "Practice mode: instant feedback under each choice. Optional timer (15-minute steps) counts down if set—use Reshuffle to restart a timed practice block.";
    }
    updateTimerDisplay();
  }

  function updateStats() {
    const total = session.length;
    let answered = 0;
    let correct = 0;
    const reveal = mode === "practice" || examSubmitted;
    for (const item of session) {
      if (item.answerKey != null) {
        answered += 1;
        if (reveal) {
          const chosen = item.options.find((o) => o.key === item.answerKey);
          if (chosen && chosen.correct) correct += 1;
        }
      }
    }
    progressText.textContent = `${answered} / ${total} answered`;
    if (mode === "exam" && !examSubmitted) {
      scoreText.textContent = "hidden until submit";
      scoreText.classList.add("score-hidden");
    } else {
      scoreText.textContent = `${correct} correct`;
      scoreText.classList.remove("score-hidden");
    }
    btnSubmitExam.disabled = !(mode === "exam" && examArmed && !examSubmitted && total > 0);
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function render() {
    quizEl.innerHTML = "";
    examResults.classList.add("is-hidden");

    if (mode === "exam" && !examArmed) {
      quizEl.innerHTML =
        '<p class="empty">Exam mode ready. Choose lesson filter, timer (or Off), exam size, then <strong>Start exam</strong>.</p>';
      updateStats();
      return;
    }

    if (!session.length) {
      quizEl.innerHTML = '<p class="empty">No questions for this filter.</p>';
      updateStats();
      return;
    }

    const showFeedback = mode === "practice" || examSubmitted;

    session.forEach((item, index) => {
      const { q, options, answerKey } = item;
      const card = document.createElement("article");
      card.className = "card" + (answerKey != null && showFeedback ? " is-answered" : "");
      card.dataset.qid = q.id;

      const meta = document.createElement("div");
      meta.className = "card-meta";
      meta.innerHTML = `
        <span class="badge">${escapeHtml(q.lesson)}</span>
        <span class="badge badge-level">${escapeHtml(q.level || "")}</span>
      `;

      const num = document.createElement("div");
      num.className = "q-num";
      num.textContent = `Question ${index + 1} of ${session.length}`;

      const stem = document.createElement("p");
      stem.className = "stem";
      stem.textContent = q.stem;

      const list = document.createElement("ul");
      list.className = "options";
      list.setAttribute("role", "radiogroup");
      list.setAttribute("aria-label", `Question ${index + 1}`);

      const locked = showFeedback && answerKey != null;
      const examLocked = examSubmitted;
      const chosenOpt = answerKey
        ? options.find((o) => o.key === answerKey)
        : null;
      const correctOpt = options.find((o) => o.correct);

      options.forEach((opt) => {
        const li = document.createElement("li");
        li.className = "option";
        if (locked || examLocked) li.classList.add("is-locked");

        const isChosen = answerKey === opt.key;
        const isCorrectChoice = opt.correct;

        if (showFeedback && answerKey != null) {
          if (isChosen && isCorrectChoice) li.classList.add("is-correct");
          else if (isChosen && !isCorrectChoice) li.classList.add("is-wrong");
          else if (!isChosen && isCorrectChoice && chosenOpt && !chosenOpt.correct) {
            li.classList.add("is-reveal-correct");
          }
        }

        const label = document.createElement("label");
        label.className = "option-label";

        const input = document.createElement("input");
        input.type = "radio";
        input.name = `q-${q.id}`;
        input.value = opt.key;
        input.checked = isChosen;
        input.disabled = examSubmitted || (mode === "practice" && answerKey != null);
        input.addEventListener("change", () => onAnswer(q.id, opt.key));

        const text = document.createElement("span");
        text.className = "option-text";
        text.textContent = opt.text;

        label.appendChild(input);
        label.appendChild(text);
        li.appendChild(label);

        if (showFeedback && answerKey != null && isChosen) {
          const fb = document.createElement("div");
          fb.className =
            "feedback is-visible " + (isCorrectChoice ? "correct" : "wrong");
          fb.setAttribute("role", "status");
          fb.innerHTML = isCorrectChoice
            ? `<strong>Correct</strong>${escapeHtml(opt.feedback || "")}`
            : `<strong>Incorrect</strong>${escapeHtml(opt.feedback || "")}`;
          li.appendChild(fb);
        }

        if (
          showFeedback &&
          chosenOpt &&
          !chosenOpt.correct &&
          isCorrectChoice &&
          !isChosen
        ) {
          const tip = document.createElement("div");
          tip.className = "feedback is-visible correct";
          tip.innerHTML = `<strong>Correct choice</strong>${escapeHtml(
            correctOpt.feedback || ""
          )}`;
          li.appendChild(tip);
        }

        list.appendChild(li);
      });

      card.appendChild(meta);
      card.appendChild(num);
      card.appendChild(stem);
      card.appendChild(list);
      quizEl.appendChild(card);
    });

    updateStats();
  }

  function onAnswer(qid, optionKey) {
    const item = session.find((s) => s.q.id === qid);
    if (!item) return;
    if (examSubmitted) return;

    if (mode === "practice") {
      if (item.answerKey != null) return;
      item.answerKey = optionKey;
      const chosen = item.options.find((o) => o.key === optionKey);
      const ok = !!(chosen && chosen.correct);
      recordAnswer(item.q, ok);
      const status = document.getElementById("quiz-status");
      if (status) {
        status.textContent = ok
          ? "Correct. " + (chosen.feedback || "")
          : "Incorrect. " + ((chosen && chosen.feedback) || "");
      }
      render();
      const safe =
        typeof CSS !== "undefined" && CSS.escape
          ? CSS.escape(qid)
          : String(qid).replace(/"/g, '\\"');
      const card = quizEl.querySelector(`[data-qid="${safe}"]`);
      if (card) card.scrollIntoView({ behavior: "smooth", block: "nearest" });
      return;
    }

    // Exam: allow changing selection until submit
    item.answerKey = optionKey;
    updateStats();
    // Re-check radios without full feedback re-render cost: light update
    render();
  }

  function startExam() {
    examArmed = true;
    examSubmitted = false;
    examResults.classList.add("is-hidden");
    const size = Number(examSizeSelect.value) || 0;
    buildSession(size);
    startTimerIfNeeded();
    render();
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  function submitExam(fromTimer) {
    if (examSubmitted || !examArmed) return;
    examSubmitted = true;
    stopTimer();

    let correct = 0;
    let answered = 0;
    const byLesson = {};

    for (const item of session) {
      const lid = item.q.lessonId;
      if (!byLesson[lid]) {
        byLesson[lid] = { lesson: item.q.lesson, n: 0, c: 0 };
      }
      byLesson[lid].n += 1;
      if (item.answerKey != null) {
        answered += 1;
        const chosen = item.options.find((o) => o.key === item.answerKey);
        const ok = !!(chosen && chosen.correct);
        if (ok) {
          correct += 1;
          byLesson[lid].c += 1;
        }
        recordAnswer(item.q, ok);
      }
    }

    const pct = session.length
      ? Math.round((correct / session.length) * 100)
      : 0;
    const rows = Object.values(byLesson)
      .map((r) => {
        const a = r.n ? Math.round((r.c / r.n) * 100) : 0;
        return `<tr><td>${escapeHtml(r.lesson)}</td><td>${r.c}/${r.n}</td><td>${a}%</td></tr>`;
      })
      .join("");

    examResults.classList.remove("is-hidden");
    examResults.innerHTML = `
      <h2>Exam results${fromTimer ? " (time expired)" : ""}</h2>
      <p class="exam-score ${pct >= 80 ? "ok" : "bad"}">${correct} / ${session.length} correct (${pct}%)</p>
      <p class="muted">Answered ${answered} of ${session.length}. Feedback is now shown under each item.</p>
      <table class="weak-table">
        <thead><tr><th>Lesson in this set</th><th>Score</th><th>%</th></tr></thead>
        <tbody>${rows}</tbody>
      </table>
      <p class="muted">Scroll the quiz for full rationales. Use <strong>Weak areas</strong> for long-term stats.</p>
    `;

    render();
    examResults.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  function reshufflePractice() {
    if (mode === "exam") {
      // cancel armed exam and reshuffle practice-style only if not mid-exam preference: restart arming
      examArmed = false;
      examSubmitted = false;
      stopTimer();
      session = [];
      updateModeUI();
      render();
      return;
    }
    examSubmitted = false;
    const mins = Number(timerSelect.value) || 0;
    buildSession(0);
    if (mins > 0) startTimerIfNeeded();
    else {
      stopTimer();
      updateTimerDisplay();
    }
    render();
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  function clearAnswers() {
    if (mode === "exam" && examArmed && !examSubmitted) {
      for (const item of session) item.answerKey = null;
      render();
      return;
    }
    if (mode === "practice") {
      for (const item of session) item.answerKey = null;
      render();
    }
  }

  function showWeakReport() {
    const stats = loadStats();
    const entries = Object.values(stats);
    if (!entries.length) {
      weakPanel.classList.remove("is-hidden");
      weakPanel.innerHTML =
        "<h2>Weak areas</h2><p class='muted'>No history yet. Answer practice items or submit an exam.</p>";
      return;
    }

    const byLesson = {};
    for (const e of entries) {
      if (!byLesson[e.lessonId]) {
        byLesson[e.lessonId] = {
          lesson: e.lesson,
          tries: 0,
          wrong: 0,
        };
      }
      byLesson[e.lessonId].tries += e.tries;
      byLesson[e.lessonId].wrong += e.wrong;
    }

    const lessonRows = Object.values(byLesson)
      .map((r) => {
        const acc = r.tries ? Math.round(((r.tries - r.wrong) / r.tries) * 100) : 0;
        return { ...r, acc };
      })
      .sort((a, b) => a.acc - b.acc);

    const worstItems = entries
      .filter((e) => e.wrong > 0)
      .map((e) => ({
        ...e,
        rate: e.tries ? e.wrong / e.tries : 0,
      }))
      .sort((a, b) => b.rate - a.rate || b.wrong - a.wrong)
      .slice(0, 12);

    const lrows = lessonRows
      .map(
        (r) =>
          `<tr><td>${escapeHtml(r.lesson)}</td><td>${r.tries - r.wrong}/${r.tries}</td><td>${r.acc}%</td><td>${r.wrong} wrong</td></tr>`
      )
      .join("");

    const irows = worstItems
      .map(
        (e) =>
          `<tr><td>${escapeHtml(e.lesson)}</td><td>${escapeHtml(e.objective || e.id)}</td><td>${e.wrong}/${e.tries}</td></tr>`
      )
      .join("");

    weakPanel.classList.remove("is-hidden");
    weakPanel.innerHTML = `
      <div class="weak-head">
        <h2>Weak areas</h2>
        <button type="button" class="btn btn-ghost" id="btnClearStats">Clear history</button>
        <button type="button" class="btn btn-ghost" id="btnCloseWeak">Close</button>
      </div>
      <p class="muted">Tracked in this browser only (localStorage). Sorted by accuracy (worst first).</p>
      <h3>By lesson</h3>
      <table class="weak-table">
        <thead><tr><th>Lesson</th><th>Correct/Tries</th><th>Accuracy</th><th>Misses</th></tr></thead>
        <tbody>${lrows}</tbody>
      </table>
      <h3>Most missed items</h3>
      <table class="weak-table">
        <thead><tr><th>Lesson</th><th>Objective / id</th><th>Wrong/Tries</th></tr></thead>
        <tbody>${irows || "<tr><td colspan='3'>No misses recorded</td></tr>"}</tbody>
      </table>
      <p class="muted">Tip: set Lesson filter to a weak module and run Practice or a short Exam.</p>
    `;
    document.getElementById("btnCloseWeak").onclick = () =>
      weakPanel.classList.add("is-hidden");
    document.getElementById("btnClearStats").onclick = () => {
      if (confirm("Clear all weak-area history on this browser?")) {
        localStorage.removeItem(STORAGE_KEY);
        showWeakReport();
        if (!Object.keys(loadStats()).length) {
          weakPanel.classList.remove("is-hidden");
          weakPanel.innerHTML = `
            <div class="weak-head">
              <h2>Weak areas</h2>
              <button type="button" class="btn btn-ghost" id="btnCloseWeak">Close</button>
            </div>
            <p class="muted">History cleared. No weak-area stats on this browser.</p>`;
          document.getElementById("btnCloseWeak").onclick = () =>
            weakPanel.classList.add("is-hidden");
        }
      }
    };
    weakPanel.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  // Init
  if (!bank.length) {
    quizEl.innerHTML =
      '<p class="empty">Question bank failed to load (questions.js).</p>';
    return;
  }

  populateFilter();
  updateModeUI();
  buildSession(0);
  render();

  filterEl.addEventListener("change", () => {
    if (filterEl.value === "all") urlDeckSelection = "all";
    else if (filterEl.value !== "__multi__") urlDeckSelection = [filterEl.value];
    if (mode === "exam") {
      examArmed = false;
      examSubmitted = false;
      stopTimer();
      session = [];
      render();
    } else {
      reshufflePractice();
    }
  });

  modeSelect.addEventListener("change", () => {
    stopTimer();
    examArmed = false;
    examSubmitted = false;
    updateModeUI();
    if (mode === "practice") {
      buildSession(0);
      render();
    } else {
      session = [];
      render();
    }
  });

  timerSelect.addEventListener("change", () => {
    // Changing timer mid-exam restarts only if exam not submitted and armed
    if (mode === "exam" && examArmed && !examSubmitted) {
      startTimerIfNeeded();
    } else if (mode === "practice") {
      const mins = Number(timerSelect.value) || 0;
      if (mins > 0) startTimerIfNeeded();
      else {
        stopTimer();
        updateTimerDisplay();
      }
    } else {
      updateTimerDisplay();
    }
  });

  btnStartExam.addEventListener("click", startExam);
  btnSubmitExam.addEventListener("click", () => submitExam(false));
  btnReshuffle.addEventListener("click", reshufflePractice);
  btnReset.addEventListener("click", clearAnswers);
  btnWeakReport.addEventListener("click", showWeakReport);
})();
