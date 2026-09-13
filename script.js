const PROJECTS = [
  {
    title: "Meet tea",
    url: "https://github.com/robertfullstack/Meet-TEA-3.0-Final",
    tag: "Front-end Web Designer Developer",
    year: "2024 - 1º Semestre e 2º Semestre",
    desc: "Rede social inclusiva para pessoas autistas, com foco em comunicação e interação social, oferecendo recursos de acessibilidade e personalização para atender às necessidades específicas da comunidade.",
    tech: ["React", "JavaScript", "Firebase"],
    img: "Images/MeetTea.png"
  },
  {
    title: "Seren",
    url: "https://github.com/Best-of-the-class/sistema-gerenciamento-psicologia",
    tag: "Back-end Web Developer",
    year: "2025 - 1º Semestre",
    desc: "Sistema de gerenciamento para psicólogos, com funcionalidades de cadastro de pacientes, registro de agendamentos visando otimizar a gestão do psicólogo.",
    tech: ["React", "MongoDB", "Node.js", "Express"],
    img: "Images/Seren.png"
  },
  {
    title: "Pindorama",
    url: "https://github.com/Best-of-the-class/sistema-web-pindorama",
    tag: "Back-end Web Developer",
    year: "2025 - 2º Semestre",
    desc: "Pindorama é uma aplicação web para difundir conteúdos sobre o Patrimônio Cultural Imaterial Brasileiro. O projeto visa promover a preservação e valorização das tradições culturais do Brasil.",
    tech: ["Ruby on Rails", "Python", "React", "Docker", "PostGreSQL"],
    img: "Images/Pindorama.png"
  },
  {
    title: "Poupas",
    url: "https://github.com/Best-of-the-class/Poupas",
    tag: "Mobile - Desktop Front-end Web Developer",
    year: "2026 - 1º Semestre",
    desc: "O Poupas é um aplicativo mobile de gamificação para educação financeira voltado para o público infanto-juvenil. O objetivo do aplicativo é ensinar conceitos de economia e finanças de forma divertida.",
    tech: ["Flutter", ".NET", "Dart", "GO", "PostGreSQL"],
    img: "Images/Poupas.png"
  }
];

let activeIndex = 0;

function renderProject() {
  const project = PROJECTS[activeIndex];

  document.getElementById("projImg").src = project.img;
  document.getElementById("projImg").alt = project.title;
  document.getElementById("projTag").textContent = project.tag;
  document.getElementById("projYear").textContent = project.year;
  document.getElementById("projDesc").textContent = project.desc;
  document.getElementById("projCount").textContent = `${activeIndex + 1} / ${PROJECTS.length}`;

  const titleEl = document.getElementById("projTitle");
  titleEl.innerHTML = `<a href="${project.url}" target="_blank" rel="noreferrer">${project.title}</a>`;

  const techRow = document.getElementById("projTech");
  techRow.innerHTML = "";
  project.tech.forEach((t) => {
    const chip = document.createElement("span");
    chip.className = "an-tech-chip";
    chip.textContent = t;
    techRow.appendChild(chip);
  });

  renderDots();
}

function renderDots() {
  const dots = document.getElementById("dots");
  dots.innerHTML = "";
  PROJECTS.forEach((_, index) => {
    const dot = document.createElement("button");
    dot.className = "an-dot" + (index === activeIndex ? " active" : "");
    dot.textContent = "✦";
    dot.style.transform = index === activeIndex ? "scale(1.3)" : "scale(1)";
    dot.addEventListener("click", () => {
      activeIndex = index;
      renderProject();
    });
    dots.appendChild(dot);
  });
}

document.getElementById("prevBtn").addEventListener("click", () => {
  activeIndex = (activeIndex - 1 + PROJECTS.length) % PROJECTS.length;
  renderProject();
});

document.getElementById("nextBtn").addEventListener("click", () => {
  activeIndex = (activeIndex + 1) % PROJECTS.length;
  renderProject();
});

renderProject();

const tickerTrack = document.getElementById("tickerTrack");
const items = Array.from({ length: 12 }, () =>
  `<span class="item">Software Designer (também) <span class="dot">✦</span></span>`
).join("");
tickerTrack.innerHTML = items + items;

const hero = document.querySelector(".an-hero");
if (hero) {
  hero.addEventListener("pointermove", (event) => {
    const bounds = hero.getBoundingClientRect();
    hero.style.setProperty("--reveal-x", `${event.clientX - bounds.left}px`);
    hero.style.setProperty("--reveal-y", `${event.clientY - bounds.top}px`);
  });
}

if ("IntersectionObserver" in window) {
  document.documentElement.classList.add("has-reveal");
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12 }
  );
  document.querySelectorAll(".an-reveal").forEach((el, index) => {
    el.style.transitionDelay = `${Math.min(index * 70, 280)}ms`;
    observer.observe(el);
  });
}
