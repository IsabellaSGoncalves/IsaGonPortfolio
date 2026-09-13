from pathlib import Path

ROOT = Path(__file__).parents[2]


def load_styles() -> str:
    components_path = ROOT / "src" / "Components"
    css = "\n".join(
        (components_path / filename).read_text(encoding="utf-8")
        for filename in ("Base.css", "Profile.css", "Carousel.css", "Skills.css")
    )
    fonts = """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=Cinzel+Decorative:wght@400;700&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap" rel="stylesheet">
    """
    reveal_script = """
    <script>
    (() => {
        const setupHeroLens = () => {
            document.querySelectorAll('.an-hero:not([data-lens-ready])').forEach((hero) => {
                hero.dataset.lensReady = 'true';
                hero.addEventListener('pointermove', (event) => {
                    const bounds = hero.getBoundingClientRect();
                    hero.style.setProperty('--reveal-x', `${event.clientX - bounds.left}px`);
                    hero.style.setProperty('--reveal-y', `${event.clientY - bounds.top}px`);
                });
            });
        };
        const start = () => {
            if (!('IntersectionObserver' in window)) return;
            document.documentElement.classList.add('has-reveal');
            const observer = new IntersectionObserver((entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-visible');
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.12 });
            const reveal = () => {
                const elements = document.querySelectorAll('.an-reveal:not([data-reveal-ready])');
                elements.forEach((element, index) => {
                    element.dataset.revealReady = 'true';
                    element.style.transitionDelay = `${Math.min(index * 70, 280)}ms`;
                    observer.observe(element);
                });
            };
            reveal();
            setupHeroLens();
            new MutationObserver(reveal).observe(document.body, { childList: true, subtree: true });
            new MutationObserver(setupHeroLens).observe(document.body, { childList: true, subtree: true });
        };
        if (document.body) start();
        else document.addEventListener('DOMContentLoaded', start, { once: true });
    })();
    </script>
    """
    return f"{fonts}<style>{css}</style>{reveal_script}"
