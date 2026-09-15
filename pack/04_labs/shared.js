/** Shared progress bus + Grok grader prompts for Atlas of the Build Loop labs */
(function (global) {
  const KEY = "atlas_build_loop_progress_v1";

  function load() {
    try {
      return JSON.parse(localStorage.getItem(KEY) || "{}");
    } catch {
      return {};
    }
  }

  function save(data) {
    localStorage.setItem(KEY, JSON.stringify(data));
  }

  function touchLab(labId, patch) {
    const data = load();
    data.labs = data.labs || {};
    const cur = data.labs[labId] || { visits: 0, score: 0, best: 0, actions: 0, lastAt: null };
    cur.visits += patch.visit ? 1 : 0;
    cur.actions = (cur.actions || 0) + (patch.actions || 0);
    if (typeof patch.score === "number") {
      cur.score = patch.score;
      cur.best = Math.max(cur.best || 0, patch.score);
    }
    cur.lastAt = new Date().toISOString();
    data.labs[labId] = cur;
    data.lastLab = labId;
    save(data);
    return cur;
  }

  function setProfile(profile) {
    const data = load();
    data.profile = profile;
    data.profileAt = new Date().toISOString();
    save(data);
  }

  function markLesson(stem) {
    const data = load();
    data.lessons = data.lessons || {};
    data.lessons[stem] = { read: true, at: new Date().toISOString() };
    save(data);
  }

  /** Copy-paste grader prompts for Grok 4.5 (substance-only accuracy). */
  const GRADER_PROMPTS = {
    bias: {
      title: "Grok 4.5 tutor — scenario audit",
      blurb: "Your written audit fills in below as you type. Copy and send when you want teaching feedback.",
      text: `You are a tutor for Atlas of the Build Loop. I audited a professional scenario for conceptual errors.

I wrote a free-form answer. Do not require a particular format, headings, or numbering. The scenario mixes sound claims with planted errors. Do not assume I was told how many errors there are.

How to teach me:
- Be professional and concrete. Point at what I wrote.
- Accept any clear phrasing; grade the ideas, not the layout.
- If I flagged a statement that is actually sound, say so and explain why it belongs.
- If I named a real error, confirm the concept in one or two sentences.
- If I missed likely errors: when the official key is NOT included, ask one hint as a question — do not dump a full inventory. When the official key IS included, say what I missed and teach the concept.
- Ignore spelling and style. Educational only — not medical advice.

Then write:
1) Hits — mistakes I named that are real, with the correct concept restated briefly.
2) False alarms — sound claims I treated as errors, if any.
3) Gaps — important planted errors I missed (hint-only if no official key; full teach if the key is included).
4) One next move — a distinction or action to practice.

Material (filled from the lab):

Lesson:
{{LESSON}}

Scenario:
{{SCENARIO}}

My answer:
{{TRAINEE}}

Official key status:
{{KEY}}`,
    },
    steelman: {
      title: "Grok 4.5 tutor — steelman craft",
      blurb: "Your draft and checked boxes fill in below as you write. Copy and send when you want teaching feedback.",
      text: `You are a tutor for Atlas of the Build Loop. Help me learn to steelman misconceptions about cardio training, physiology, and bloodwork.

What a steelman is: the strongest fair form of the weak take — a version a smart critic could actually endorse — plus the conditions under which it would be true, and the limit that stops it overclaiming. It is not a rebuttal, a joke, or a slogan swap.

How to teach me:
- Be general: teach the move (fairness, strongest reason, conditions, limits). Do not grade me like a quiz key.
- Be concrete: point at sentences I wrote. If a checked box is not earned by the writing, say so.
- If my text is still a straw, a rebuttal, or the original slogan, name which one and why, using this topic.
- Ignore spelling and style. Educational only — not medical advice. Do not invent motives I did not claim.

Then write:
1) Diagnosis — what I did well, and what the steelman is still missing (one short paragraph).
2) Fairness — did I maximize the opponent’s reasonableness, or did I knock down a weaker version?
3) Craft — strongest reason? evidence or conditions of truth? a named limit?
4) One next move — a question to ask, a distinction to name, or a condition to add. Not a full rewrite unless a 2–4 sentence “one possible fair form” would teach the distinction (label it as one possible form, not the answer).

Material (filled from the lab):

Weak take:
{{WEAK}}

My steelman:
{{STEELMAN}}

Boxes I checked (my self-rubric):
{{RUBRIC}}`,
    },
    lock: {
      title: "Grok 4.5 grader — lab LOCK lines",
      blurb: "After any lab session, lock 3–10 takeaways (one claim per line) and grade them like Day 0 Core Summaries.",
      text: `You are grading ONLY my Lab LOCK lines for accuracy.

Rules:
- Judge substance only (facts, formulas, directions, lists, mechanisms).
- Ignore grammar, style, and wording quality.
- Do NOT rewrite my LOCK lines into polished prose.
- Do NOT give “say it like this” language coaching.

For each LOCK line:
1) Correct / Partial / Incorrect
2) If not Correct: name the wrong claim + give the correct concept in one short line

End with: Top accuracy risks (max 3)

Lab / decks practiced (optional):
[PASTE e.g. Lab Interpretation Arena · decks ct-06-hematology, ct-07-labs]

Material:
[PASTE LOCK lines only — one claim per line]`,
    },
  };

  function ensureGraderStyles() {
    if (document.getElementById("atlas-grader-styles")) return;
    const s = document.createElement("style");
    s.id = "atlas-grader-styles";
    s.textContent = `
      .atlas-grader {
        margin-top: 2rem;
        padding: 1.1rem 1.15rem;
        background: var(--inset, #eef4f8);
        border: 1px solid var(--border, #c5d4de);
        border-radius: 14px;
      }
      .atlas-grader h2 {
        margin: 0 0 .35rem;
        font-size: 1rem;
        color: var(--gold, #8b5a14);
      }
      .atlas-grader .atlas-grader-blurb {
        margin: 0 0 .75rem;
        color: var(--muted, #445566);
        font-size: .9rem;
        line-height: 1.45;
      }
      .atlas-grader .atlas-grader-how {
        margin: 0 0 .75rem;
        color: var(--text, #17212b);
        font-size: .85rem;
        line-height: 1.45;
      }
      .atlas-grader .atlas-grader-how code {
        background: rgba(255,255,255,.06);
        padding: .05em .35em;
        border-radius: 4px;
        font-size: .88em;
      }
      .atlas-grader pre {
        margin: 0 0 .75rem;
        padding: .85rem .9rem;
        max-height: 18rem;
        overflow: auto;
        background: var(--card, #fff);
        border: 1px solid var(--border, #c5d4de);
        border-radius: 10px;
        color: var(--text, #17212b);
        font-size: .78rem;
        line-height: 1.4;
        white-space: pre-wrap;
        word-break: break-word;
      }
      .atlas-grader .atlas-grader-actions {
        display: flex;
        flex-wrap: wrap;
        gap: .5rem;
        align-items: center;
      }
      .atlas-grader button.atlas-grader-copy {
        border: 0;
        background: linear-gradient(180deg, #7ee8d4, #2bb89a);
        color: #062f2c;
        padding: .55rem .95rem;
        border-radius: 10px;
        font-weight: 700;
        cursor: pointer;
        font-size: .9rem;
      }
      .atlas-grader button.atlas-grader-copy:hover { filter: brightness(1.06); }
      .atlas-grader .atlas-grader-status {
        color: var(--ok, #157a4b);
        font-size: .85rem;
        font-weight: 600;
        min-height: 1.2em;
      }
      .atlas-grader details.atlas-grader-lock {
        margin-top: 1rem;
        border-top: 1px solid #2a3550;
        padding-top: .85rem;
      }
      .atlas-grader details.atlas-grader-lock summary {
        cursor: pointer;
        color: #8b9cff;
        font-weight: 700;
        font-size: .9rem;
      }
      .atlas-grader details.atlas-grader-lock .atlas-grader-blurb { margin-top: .5rem; }
    `;
    document.head.appendChild(s);
  }

  async function copyText(text, statusEl) {
    try {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        await navigator.clipboard.writeText(text);
      } else {
        const ta = document.createElement("textarea");
        ta.value = text;
        ta.style.position = "fixed";
        ta.style.left = "-9999px";
        document.body.appendChild(ta);
        ta.select();
        document.execCommand("copy");
        document.body.removeChild(ta);
      }
      if (statusEl) {
        statusEl.textContent = "Copied — paste into a new Grok 4.5 chat.";
        setTimeout(() => { statusEl.textContent = ""; }, 3500);
      }
      return true;
    } catch (e) {
      if (statusEl) statusEl.textContent = "Copy failed — select the prompt text manually.";
      return false;
    }
  }

  function applyFill(template, values) {
    return String(template).replace(/\{\{(\w+)\}\}/g, (_, k) => (
      values && values[k] != null ? String(values[k]) : ""
    ));
  }

  /**
   * Mount lab-specific + LOCK grader panels.
   * @param {string|HTMLElement} mountEl
   * @param {string} labKey - bias | steelman
   * @param {{ how?: string, fillValues?: () => Record<string,string> }} [opts]
   */
  function mountGraderPrompt(mountEl, labKey, opts) {
    ensureGraderStyles();
    const host = typeof mountEl === "string" ? document.getElementById(mountEl) : mountEl;
    if (!host) return { refresh() {} };
    const pack = GRADER_PROMPTS[labKey];
    if (!pack) {
      host.innerHTML = "";
      return { refresh() {} };
    }
    const lock = GRADER_PROMPTS.lock;
    const getText = () => {
      if (opts && typeof opts.fillValues === "function") {
        return applyFill(pack.text, opts.fillValues());
      }
      return pack.text;
    };
    const how = (opts && opts.how) ||
      `Copy prompt → new Grok 4.5 chat → replace <code>[PASTE]</code> blocks with your work only → send. Substance-only grading (Correct / Partial / Incorrect). No style coaching.`;

    host.innerHTML = `
      <section class="atlas-grader" aria-label="Grok grader prompt">
        <h2>${pack.title}</h2>
        <p class="atlas-grader-blurb">${pack.blurb}</p>
        <p class="atlas-grader-how"><strong>How:</strong> ${how}</p>
        <pre id="atlas-grader-text" class="atlas-grader-pre"></pre>
        <div class="atlas-grader-actions">
          <button type="button" class="atlas-grader-copy" id="atlas-grader-copy-btn">Copy grader prompt</button>
          <span class="atlas-grader-status" id="atlas-grader-status" role="status"></span>
        </div>
        <details class="atlas-grader-lock">
          <summary>${lock.title}</summary>
          <p class="atlas-grader-blurb">${lock.blurb}</p>
          <pre id="atlas-grader-lock-text">${escapeHtml(lock.text)}</pre>
          <div class="atlas-grader-actions">
            <button type="button" class="atlas-grader-copy" id="atlas-grader-lock-copy">Copy LOCK grader prompt</button>
            <span class="atlas-grader-status" id="atlas-grader-lock-status" role="status"></span>
          </div>
        </details>
      </section>
    `;

    const pre = host.querySelector("#atlas-grader-text");
    function refresh() {
      pre.textContent = getText();
    }
    refresh();

    const status = host.querySelector("#atlas-grader-status");
    const lockStatus = host.querySelector("#atlas-grader-lock-status");
    host.querySelector("#atlas-grader-copy-btn").onclick = () => copyText(getText(), status);
    host.querySelector("#atlas-grader-lock-copy").onclick = () => copyText(lock.text, lockStatus);
    return { refresh };
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }

  global.AtlasProgress = { KEY, load, save, touchLab, setProfile, markLesson };
  global.AtlasLabGrader = { PROMPTS: GRADER_PROMPTS, mount: mountGraderPrompt, copyText };
})(window);
