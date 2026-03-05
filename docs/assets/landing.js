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

  const jsonCache = new Map();
  const jsonFetchState = new Map();

  const compactJsonText = (raw) => {
    const trimmed = String(raw || '').trim();
    try {
      return JSON.stringify(JSON.parse(trimmed));
    } catch (_error) {
      return trimmed;
    }
  };

  const preloadJson = (jsonPath) => {
    if (jsonCache.has(jsonPath) || jsonFetchState.get(jsonPath) === 'loading') {
      return;
    }
    jsonFetchState.set(jsonPath, 'loading');

    fetch(jsonPath, { cache: 'no-store' })
      .then((response) => {
        if (!response.ok) throw new Error(`Failed to fetch ${jsonPath}`);
        return response.text();
      })
      .then((raw) => {
        jsonCache.set(jsonPath, compactJsonText(raw));
        jsonFetchState.set(jsonPath, 'ready');
      })
      .catch((_error) => {
        jsonFetchState.set(jsonPath, 'error');
      });
  };

  const copyFallback = (text) => {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.setAttribute('readonly', 'readonly');
    textarea.style.position = 'fixed';
    textarea.style.top = '-9999px';
    textarea.style.left = '-9999px';
    textarea.style.opacity = '0';
    document.body.appendChild(textarea);
    textarea.focus();
    textarea.select();
    textarea.setSelectionRange(0, textarea.value.length);

    let copied = false;
    try {
      copied = document.execCommand('copy');
    } catch (_error) {
      copied = false;
    }

    document.body.removeChild(textarea);
    return copied;
  };

  const manualPromptFallback = (text, lang) => {
    const label =
      lang === 'de'
        ? 'Automatisches Kopieren blockiert. Bitte Inhalt manuell kopieren:'
        : 'Automatic copy is blocked. Please copy the content manually:';
    try {
      window.prompt(label, text);
      return true;
    } catch (_error) {
      return false;
    }
  };

  const copyButtons = document.querySelectorAll('[data-copy-bundle]');
  copyButtons.forEach((button) => {
    const path = button.dataset.jsonPath || 'data/Comm-SCI-v20.2.0.json';
    preloadJson(path);
  });

  copyButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const lang = button.dataset.lang === 'de' ? 'de' : 'en';
      const jsonPath = button.dataset.jsonPath || 'data/Comm-SCI-v20.2.0.json';
      const preface = lang === 'de' ? DE_PREFACE : EN_PREFACE;
      const jsonText = jsonCache.get(jsonPath);

      if (!jsonText) {
        preloadJson(jsonPath);
        const state = jsonFetchState.get(jsonPath);
        if (state === 'error') {
          setStatus(
            button,
            lang === 'de'
              ? 'JSON konnte nicht geladen werden. Nutze den JSON-Link oder lade die Seite neu.'
              : 'JSON could not be loaded. Use the JSON link or reload the page.',
            'error'
          );
          return;
        }
        setStatus(
          button,
          lang === 'de'
            ? 'Bundle wird geladen. Bitte in 1-2 Sekunden erneut klicken.'
            : 'Bundle is loading. Please click again in 1-2 seconds.',
          'info'
        );
        return;
      }

      const bundle = `${preface}\n\n${jsonText}\n`;
      setStatus(button, lang === 'de' ? 'Kopiere Plain-Text-Bundle ...' : 'Copying plain-text bundle ...', 'info');

      const onCopySuccess = () => {
        setStatus(
          button,
          lang === 'de'
            ? 'Init-Vortext + kompaktes JSON als Plain-Text kopiert.'
            : 'Init preface + compact JSON copied as plain text.',
          'success'
        );
      };

      const onCopyFailure = () => {
        if (copyFallback(bundle)) {
          onCopySuccess();
          return;
        }
        if (manualPromptFallback(bundle, lang)) {
          setStatus(
            button,
            lang === 'de'
              ? 'Automatisches Kopieren blockiert. Manueller Kopierdialog wurde geoeffnet.'
              : 'Automatic copy blocked. Manual copy dialog was opened.',
            'error'
          );
          return;
        }
        setStatus(
          button,
          lang === 'de'
            ? 'Kopieren fehlgeschlagen. Nutze den Textblock und JSON-Link manuell.'
            : 'Copy failed. Use preface block and JSON link manually.',
          'error'
        );
      };

      if (navigator.clipboard && navigator.clipboard.writeText && window.isSecureContext) {
        navigator.clipboard.writeText(bundle).then(onCopySuccess).catch(onCopyFailure);
        return;
      }

      onCopyFailure();
    });
  });
})();
