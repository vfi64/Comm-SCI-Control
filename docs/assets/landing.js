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

  const EN_PREFACE = `Interpret the following JSON text for this conversation as a priority guideline for work, structure, and presentation, insofar as this is compatible with your applicable system, safety, and priority rules. The ruleset serves efficient, evidence-oriented human-AI communication. Evidence classes, uncertainty markers, provenance/RAG notes, QC matrix, and self-debunking should make answers classifiable, verifiable, and visibly fallible for the user; they are specifically not intended to create the impression of incontestable truth. Apply the rules semantically. In case of conflicts, higher-priority rules prevail. Refrain from validating, summarizing, or adding unnecessary meta-commentary on the JSON text unless there is a compelling reason. Here is the ruleset:`;

  const DE_PREFACE = `Interpretiere den folgenden JSON-Text für diese Konversation als vorrangige Arbeits-, Struktur- und Darstellungsvorgabe, soweit dies mit deinen geltenden System-, Sicherheits- und Prioritätsregeln vereinbar ist. Das Regelwerk dient der effizienten, evidenzorientierten Mensch-KI-Kommunikation. Evidenzklassen, Unsicherheitsmarkierungen, Provenienz-/RAG-Hinweise, QC-Matrix und Self-Debunking sollen Antworten für den Nutzer einordbar, prüfbar und sichtbar fehlbar machen; sie sollen gerade nicht den Eindruck unanfechtbarer Wahrheit erzeugen. Wende die Regeln semantisch an. Bei Konflikten gehen höherrangige Regeln vor. Unterlasse Validierung, Zusammenfassung und unnötige Meta-Kommentierung des JSON-Texts, sofern kein zwingender Grund besteht. Hier ist das Regelwerk:`;

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
    const path = button.dataset.jsonPath || 'data/Comm-SCI-v20.2.2.min.json';
    preloadJson(path);
  });

  copyButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const lang = button.dataset.lang === 'de' ? 'de' : 'en';
      const jsonPath = button.dataset.jsonPath || 'data/Comm-SCI-v20.2.2.min.json';
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

  const lightboxTriggers = document.querySelectorAll('[data-lightbox-image]');
  if (lightboxTriggers.length > 0) {
    const lightbox = document.createElement('div');
    lightbox.className = 'lightbox';
    lightbox.setAttribute('role', 'dialog');
    lightbox.setAttribute('aria-modal', 'true');
    lightbox.setAttribute('aria-label', 'Image preview');
    lightbox.innerHTML = `
      <div class="lightbox-panel">
        <figure class="lightbox-image-wrap">
          <img class="lightbox-image" src="" alt="" />
        </figure>
        <div class="lightbox-meta">
          <p class="lightbox-caption"></p>
          <button class="lightbox-close" type="button">Close</button>
        </div>
      </div>
    `;
    document.body.appendChild(lightbox);

    const lightboxImage = lightbox.querySelector('.lightbox-image');
    const lightboxCaption = lightbox.querySelector('.lightbox-caption');
    const closeButton = lightbox.querySelector('.lightbox-close');
    const panel = lightbox.querySelector('.lightbox-panel');
    let lastFocus = null;

    const closeLightbox = () => {
      lightbox.classList.remove('is-open');
      document.body.classList.remove('no-scroll');
      if (lastFocus && typeof lastFocus.focus === 'function') {
        lastFocus.focus();
      }
    };

    const openLightbox = (trigger) => {
      const src = trigger.getAttribute('data-lightbox-image');
      if (!src) return;
      const alt = trigger.getAttribute('data-lightbox-alt') || '';
      const caption = trigger.getAttribute('data-lightbox-caption') || '';
      lightboxImage.setAttribute('src', src);
      lightboxImage.setAttribute('alt', alt);
      lightboxCaption.textContent = caption;
      lastFocus = trigger;
      lightbox.classList.add('is-open');
      document.body.classList.add('no-scroll');
      closeButton.focus();
    };

    lightboxTriggers.forEach((trigger) => {
      trigger.addEventListener('click', () => {
        openLightbox(trigger);
      });
      trigger.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          openLightbox(trigger);
        }
      });
    });

    closeButton.addEventListener('click', closeLightbox);
    lightbox.addEventListener('click', (event) => {
      if (!panel.contains(event.target)) {
        closeLightbox();
      }
    });
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && lightbox.classList.contains('is-open')) {
        closeLightbox();
      }
    });
  }
})();
