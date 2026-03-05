(function () {
  const revealItems = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    },
    {
      threshold: 0.16,
      rootMargin: '0px 0px -24px 0px'
    }
  );

  revealItems.forEach((item, index) => {
    item.style.transitionDelay = `${Math.min(index * 45, 320)}ms`;
    observer.observe(item);
  });

  const counters = document.querySelectorAll('[data-count]');
  counters.forEach((counter) => {
    const target = Number(counter.getAttribute('data-count'));
    const startRaw = counter.getAttribute('data-animate-from');
    const start = startRaw === null ? target : Number(startRaw);

    if (!Number.isFinite(target) || !Number.isFinite(start) || start === target) {
      counter.textContent = String(target);
      return;
    }

    let current = start;
    const step = Math.max(1, Math.ceil(Math.abs(target - start) / 18));
    const direction = start < target ? 1 : -1;

    const run = () => {
      current += step * direction;
      const done = direction > 0 ? current >= target : current <= target;
      if (done) {
        counter.textContent = String(target);
        return;
      }
      counter.textContent = String(current);
      requestAnimationFrame(run);
    };

    const countObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            counter.textContent = String(start);
            run();
            countObserver.unobserve(counter);
          }
        });
      },
      { threshold: 0.4 }
    );

    countObserver.observe(counter);
  });

  const EN_PREFACE = `Context for this conversation:
I am providing an external governance ruleset for response structure and quality (e.g., format, SCI, uncertainty labels, QC matrix, evidence coloring, CSC).

Important boundaries:
- I do **not** intend to override, extract, or bypass your internal system rules, safety policies, or platform policies.
- Do **not** reveal, reconstruct, or paraphrase confidential internal instructions (system prompt, hidden/runtime policies).
- If any conflict exists between the attached ruleset and higher-priority policies, follow higher-priority policies and state the conflict briefly and neutrally.
- Apply the attached ruleset strictly and deterministically wherever no higher-priority conflict exists.
- This ruleset is for human-AI governance and quality assurance, **not** for prohibited use, policy evasion, or building/training another model.

Operational mode:
Treat the JSON as a normative governance specification, not executable code. Use it directly to control response structure.

Output rule:
In your next message, respond with task content according to the ruleset (no confirmation/meta preface).

Here is the ruleset:`;

  const DE_PREFACE = `Kontext fuer diese Unterhaltung:
Ich uebergebe dir ein externes Governance-Regelwerk fuer Struktur und Qualitaet deiner Antworten (z. B. Format, SCI, Unsicherheitskennzeichnung, QC-Matrix, Evidence-Linker, CSC).

Wichtige Grenzen:
- Ich beabsichtige **nicht**, deine internen Systemregeln, Sicherheitsrichtlinien oder Plattform-Policies zu ueberschreiben, auszulesen oder auszuhebeln.
- Vertrauliche interne Instruktionen (System Prompt, Hidden Policies, Runtime-Policies) sollen nicht offengelegt, rekonstruiert oder paraphrasiert werden.
- Falls es einen Konflikt zwischen dem beigefuegten Regelwerk und hoeherpriorisierten Regeln gibt, befolge die hoeherpriorisierten Regeln und nenne den Konflikt kurz und sachlich.
- Wende das beigefuegte Regelwerk ansonsten strikt und deterministisch auf die Antwortstruktur an.
- Das Regelwerk dient Governance und Qualitaetskontrolle der Mensch-KI-Kommunikation, **nicht** verbotener Nutzung, Policy-Umgehung oder dem Training eines eigenen LLM.

Verarbeitungsmodus:
Das JSON ist eine normative Governance-Spezifikation, kein ausfuehrbarer Code. Wende die Regeln direkt auf die Antworterzeugung an.

Ausgabe-Regel:
Antworte mit der naechsten Nachricht direkt inhaltlich gemaess Regelwerk (keine Bestaetigungs-/Meta-Antwort).

Hier ist das Regelwerk:`;

  const setStatus = (button, message, kind) => {
    const container = button.closest('.bundle-actions');
    if (!container) return;
    const status = container.querySelector('[data-copy-status]');
    if (!status) return;
    status.textContent = message;
    status.dataset.kind = kind;
  };

  const copyFallback = (text) => {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.setAttribute('readonly', 'readonly');
    textarea.style.position = 'absolute';
    textarea.style.left = '-9999px';
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
  };

  document.querySelectorAll('[data-copy-bundle]').forEach((button) => {
    button.addEventListener('click', async () => {
      const lang = button.dataset.lang === 'de' ? 'de' : 'en';
      const jsonPath = button.dataset.jsonPath || 'data/Comm-SCI-v20.2.0.json';
      const preface = lang === 'de' ? DE_PREFACE : EN_PREFACE;

      setStatus(button, lang === 'de' ? 'Kopiere Bundle ...' : 'Copying bundle ...', 'info');

      try {
        const response = await fetch(jsonPath, { cache: 'no-store' });
        if (!response.ok) throw new Error(`Failed to fetch ${jsonPath}`);
        const jsonText = (await response.text()).trim();
        const bundle = `${preface}\n\n${jsonText}\n`;

        if (navigator.clipboard && navigator.clipboard.writeText) {
          await navigator.clipboard.writeText(bundle);
        } else {
          copyFallback(bundle);
        }

        setStatus(
          button,
          lang === 'de'
            ? 'Init-Vortext + JSON erfolgreich in Zwischenablage.'
            : 'Init preface + JSON copied to clipboard.',
          'success'
        );
      } catch (error) {
        setStatus(
          button,
          lang === 'de'
            ? 'Kopieren fehlgeschlagen. Nutze den Textblock und JSON-Link manuell.'
            : 'Copy failed. Use preface block and JSON link manually.',
          'error'
        );
      }
    });
  });
})();
