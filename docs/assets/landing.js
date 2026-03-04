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
    let current = 0;
    const step = Math.max(1, Math.ceil(target / 18));

    const run = () => {
      current += step;
      if (current >= target) {
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
            run();
            countObserver.unobserve(counter);
          }
        });
      },
      { threshold: 0.4 }
    );

    countObserver.observe(counter);
  });
})();
