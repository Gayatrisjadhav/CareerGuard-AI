VanillaTilt.init(document.querySelectorAll(".tilt"), {
  max: 25,
  speed: 400,
  glare: true,
  "max-glare": 0.3,
});

function toggleDarkMode() {
  document.body.classList.toggle("dark-mode");
}

gsap.registerPlugin(ScrollTrigger);

gsap.utils.toArray(".result-section").forEach((section, i) => {
  gsap.from(section, {
    opacity: 0,
    y: 50,
    duration: 1.2,
    scrollTrigger: {
      trigger: section,
      start: "top 90%",
      toggleActions: "play none none reset"
    }
  });
});
