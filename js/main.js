document.addEventListener("DOMContentLoaded", () => {
  // Loading Screen
  const loadingScreen = document.getElementById("loadingScreen");
  if (loadingScreen) {
    // Default delay
    let delayTime = 3000;

    // If hash exists (e.g. accessed from other page or direct link to section)
    // Shorten the delay to 2.0s (0.5s wait + 1.5s fade)
    if (window.location.hash) {
      delayTime = 2000;
      // Speed up animation via JS style injection or modifying element
      loadingScreen.style.animationDelay = "0.5s";

      // We need to override the animation property.
      // Start at 0.5s, duration 1.5s -> Ends at 2.0s
      loadingScreen.style.animation = "fadeOut 1.5s ease 0.5s forwards";
    }

    setTimeout(() => {
      loadingScreen.style.display = "none";
    }, delayTime);
  }

  // Header Scroll Effect
  const header = document.querySelector(".header");
  window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
      header.classList.add("scrolled");
    } else {
      header.classList.remove("scrolled");
    }

    // Toggle Mobile CTA on Index Page
    const mobileCta = document.querySelector(".mobile-cta");
    const collectionSection = document.getElementById("collection");
    let isCollectionVisible = false;

    // Observer to detect if Collection section is in view
    if (collectionSection && mobileCta) {
      const collectionObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          isCollectionVisible = entry.isIntersecting;
          updateMobileCta();
        });
      }, { threshold: 0.1 }); // Trigger as soon as 10% is visible
      collectionObserver.observe(collectionSection);
    }

    function updateMobileCta() {
      if (!mobileCta) return;
      
      // logic: Show if scrolled past hero (>300) AND collection is NOT visible
      if (window.scrollY > 300 && !isCollectionVisible) {
        mobileCta.classList.add("cta-visible");
      } else {
        mobileCta.classList.remove("cta-visible");
      }
    }

    // Call on scroll
    updateMobileCta();
  });

  // Mobile Menu Toggle
  const menuToggle = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".nav");

  if (menuToggle && nav) {
    menuToggle.addEventListener("click", () => {
      nav.style.display = nav.style.display === "block" ? "none" : "block";
      menuToggle.classList.toggle("active");
    });

    // Close menu when a link is clicked
    const navLinks = document.querySelectorAll(".nav-list a");
    navLinks.forEach((link) => {
      link.addEventListener("click", () => {
        if (window.innerWidth <= 768) {
          nav.style.display = "none";
          menuToggle.classList.remove("active");
        }
      });
    });
  }

  // Smooth Scroll with Offset
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();
      const targetId = this.getAttribute("href");

      // If valid external link or empty, allow default or return
      if (!targetId || !targetId.startsWith("#") || targetId === "#") {
        if (targetId && !targetId.startsWith("#")) {
          // It's a real link (e.g. changed dynamically), so we should navigate manually
          // because we already called e.preventDefault()
          window.open(targetId, this.target || "_self");
          return;
        }
        return;
      }

      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        let headerHeight = header ? header.offsetHeight : 0;

        // Special case for Concept: Do not subtract header height (or reduce offset)
        // so that the scroll goes further down, hiding the Hero image.
        if (targetId === "#concept") {
          headerHeight = 0;
        }

        const elementPosition = targetElement.getBoundingClientRect().top;
        const offsetPosition =
          elementPosition + window.pageYOffset - headerHeight;

        window.scrollTo({
          top: offsetPosition,
          behavior: "smooth",
        });

        // Close mobile menu if open
        if (window.innerWidth <= 768 && nav) {
          nav.style.display = "none";
        }
      }
    });
  });

  // Scroll Animations (Intersection Observer)
  const observerOptions = {
    root: null,
    rootMargin: "0px",
    threshold: 0.1,
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        observer.unobserve(entry.target); // Only animate once
      }
    });
  }, observerOptions);

  // Elements to animate
  const animatedElements = document.querySelectorAll(
    ".fade-in-up, .section-title, .gallery-item, .shop-card"
  );
  animatedElements.forEach((el) => {
    el.style.opacity = "0";
    el.style.transform = "translateY(30px)";
    el.style.transition = "opacity 0.8s ease, transform 0.8s ease";
    observer.observe(el);
  });

  // Add visible class style dynamically
  const style = document.createElement("style");
  style.innerHTML = `
        .visible {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }
    `;
  document.head.appendChild(style);
});
