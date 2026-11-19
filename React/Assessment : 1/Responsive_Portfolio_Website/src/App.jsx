
import { useState } from "react";
import "./App.css";

const skills = [
  "React.js", "JavaScript", "HTML5", "CSS3",
  "Python", "Java", "Git & GitHub", "Cybersecurity"
];


const projects = [
  {
    title: "Steganography",
    description:
      "A data-hiding project focused on concealing information within digital media for privacy and secure communication.",
    tech: "Python · Steganography · Security",
    icon: "🕵️",
    link: "https://github.com/Dhvani2458/Steganography",
  },
  {
    title: "Personal Firewall",
    description:
      "A personal firewall project focused on monitoring and controlling network traffic to improve system security.",
    tech: "Python · Networking · Cybersecurity",
    icon: "🛡️",
    link: "https://github.com/Dhvani2458/Personal-firewall",
  },
  {
    title: "MindReader Chatbot",
    description:
      "A chatbot project designed to interact with users and provide responses through a conversational interface.",
    tech: "Python · Chatbot · NLP",
    icon: "🤖",
    link: "https://github.com/Dhvani2458/MindReader_Chatbot",
  },
  {
    title: "Natural Language to Code",
    description:
      "A project that explores translating natural-language instructions into programming code.",
    tech: "Python · NLP · Code Generation",
    icon: "⌨️",
    link: "https://github.com/Dhvani2458/Natural-Language-to-code-language",
  },
  {
    title: "Caesar Cipher",
    description:
      "A classical cryptography project that demonstrates text encryption and decryption using a shift cipher.",
    tech: "Python · Cryptography · Encryption",
    icon: "🔐",
    link: "https://github.com/Dhvani2458/Caesar-Cipher",
  },
  {
    title: "Quantum Security Scanner",
    description:
      "A security analysis application designed to identify potential quantum computing threats and explore post-quantum cryptography recommendations.",
    tech: "React · Python · Post-Quantum Cryptography",
    icon: "⚛️",
    link: "https://github.com/Dhvani2458/Quantum-Security-Scanner",
  },
];


function Header({ dark, setDark }) {
  const [menuOpen, setMenuOpen] = useState(false);

  const links = ["Home", "About", "Skills", "Projects", "Contact"];

  return (
    <header className="header">
      <a href="#home" className="logo">
        dhvani<span>.</span>
      </a>

      <button
        className="menu-toggle"
        onClick={() => setMenuOpen(!menuOpen)}
        aria-label="Toggle navigation"
        aria-expanded={menuOpen}
      >
        {menuOpen ? "✕" : "☰"}
      </button>

      <nav className={menuOpen ? "nav open" : "nav"}>
        {links.map((link) => (
          <a
            key={link}
            href={`#${link.toLowerCase()}`}
            onClick={() => setMenuOpen(false)}
          >
            {link}
          </a>
        ))}
        <button
          className="theme-toggle"
          onClick={() => setDark(!dark)}
          aria-label="Toggle color theme"
        >
          {dark ? "☀️" : "🌙"}
        </button>
      </nav>
    </header>
  );
}

function Hero() {
  return (
    <section id="home" className="hero section">
      <div className="hero-content">
        <p className="eyebrow">HELLO, WORLD! I'M</p>
        <h1>
          Dhvani <span>Tandel</span>
        </h1>
        <h2>Developer & Tech Enthusiast</h2>
        <p className="hero-description">
          I build responsive web experiences and explore the
          intersection of software development and cybersecurity.
          Turning ideas into useful digital solutions, one line
          of code at a time.
        </p>

        <div className="hero-buttons">
          <a href="#projects" className="btn primary">
            Explore My Work ↗
          </a>
          <a href="#contact" className="btn secondary">
            Let's Connect
          </a>
        </div>

        <div className="hero-tags">
          <span>⌘ Frontend Development</span>
          <span>◈ Cybersecurity</span>
        </div>
      </div>

      <div className="hero-visual">
        <div className="orbit orbit-one" />
        <div className="orbit orbit-two" />
        <div className="code-card">
          <div className="code-dots">
            <i /><i /><i />
          </div>
          <p className="code-muted">developer.js</p>
          <div className="code-lines">
            <p><span>const</span> developer = {"{"}</p>
            <p className="indent">name: <b>"Dhvani"</b>,</p>
            <p className="indent">role: <b>"Developer"</b>,</p>
            <p className="indent">passion: <b>"Building"</b>,</p>
            <p className="indent">learning: <b>true</b></p>
            <p>{"};"}</p>
            <br />
            <p><span>while</span> (curious) {"{"}</p>
            <p className="indent">keepBuilding();</p>
            <p>{"}"}</p>
          </div>
          <div className="code-status">
            <span /> Available for opportunities
          </div>
        </div>
        <div className="floating-badge badge-top">{"</>"}</div>
        <div className="floating-badge badge-bottom">✦ React</div>
      </div>
    </section>
  );
}

function SectionTitle({ label, title, highlight }) {
  return (
    <div className="section-title">
      <p className="eyebrow">{label}</p>
      <h2>{title} <span>{highlight}</span></h2>
    </div>
  );
}

function About() {
  return (
    <section id="about" className="section">
      <SectionTitle label="GET TO KNOW ME" title="About" highlight="Me" />
      <div className="about-grid">
        <div className="about-mark">
          <span>D</span>
          <div className="mark-caption">Curious mind. Creative code.</div>
        </div>
        <div className="about-copy">
          <h3>A developer who loves to learn.</h3>
          <p>
            I'm pursuing a B.Tech in Information Technology with
            a specialization in Cyber Security. I enjoy creating
            web applications, solving technical problems, and
            exploring new technologies.
          </p>
          <p>
            My goal is to combine practical development skills
            with a security-first mindset to create digital
            experiences that are both useful and reliable.
          </p>
          <div className="about-facts">
            <div><strong>03+</strong><span>Projects to explore</span></div>
            <div><strong>08</strong><span>Skills and technologies</span></div>
            <div><strong>∞</strong><span>Things to learn</span></div>
          </div>
        </div>
      </div>
    </section>
  );
}

function Skills() {
  return (
    <section id="skills" className="section">
      <SectionTitle label="MY TOOLKIT" title="Skills &" highlight="Technologies" />
      <p className="section-description">
        Technologies I use and continue to develop my skills in.
      </p>
      <div className="skills-grid">
        {skills.map((skill, index) => (
          <div className="skill-card" key={skill}>
            <span className="skill-number">
              {String(index + 1).padStart(2, "0")}
            </span>
            <span>{skill}</span>
            <span className="skill-arrow">↗</span>
          </div>
        ))}
      </div>
    </section>
  );
}


function ProjectCard({ project, index }) {
  return (
    <article className="project-card">
      <div className="project-top">
        <span className="project-icon">{project.icon}</span>
        <span className="project-index">
          {String(index + 1).padStart(2, "0")}
        </span>
      </div>

      <h3>{project.title}</h3>
      <p>{project.description}</p>

      <div className="project-footer">
        <span>{project.tech}</span>
      </div>

      {project.link ? (
        <a
          className="project-link"
          href={project.link}
          target="_blank"
          rel="noopener noreferrer"
          aria-label={`View ${project.title} on GitHub`}
        >
          View on GitHub <span>↗</span>
        </a>
      ) : (
        <span className="project-link project-unavailable">
          Project overview
        </span>
      )}
    </article>
  );
}


function Projects() {
  return (
    <section id="projects" className="section">
      <SectionTitle
        label="SELECTED WORK"
        title="Featured"
        highlight="Projects"
      />

      <p className="section-description">
        A selection of projects showcasing my development interests.
      </p>

      <div className="projects-grid">
        {projects.map((project, index) => (
          <ProjectCard
            key={project.title}
            project={project}
            index={index}
          />
        ))}
      </div>
    </section>
  );
}

function Contact() {
  const [form, setForm] = useState({
    name: "",
    email: "",
    message: "",
  });
  const [errors, setErrors] = useState({});
  const [submitted, setSubmitted] = useState(false);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setForm((previous) => ({ ...previous, [name]: value }));
    setErrors((previous) => ({ ...previous, [name]: "" }));
    setSubmitted(false);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const nextErrors = {};

    if (!form.name.trim()) {
      nextErrors.name = "Please enter your name.";
    }

    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email.trim())) {
      nextErrors.email = "Please enter a valid email address.";
    }

    if (form.message.trim().length < 10) {
      nextErrors.message = "Message must contain at least 10 characters.";
    }

    setErrors(nextErrors);

    if (Object.keys(nextErrors).length === 0) {
      setSubmitted(true);
      setForm({ name: "", email: "", message: "" });
    }
  };

  return (
    <section id="contact" className="section">
      <SectionTitle label="SAY HELLO" title="Let's Work" highlight="Together" />
      <div className="contact-grid">
        <div className="contact-copy">
          <h3>Have an idea in mind?</h3>
          <p>
            Whether it's a development opportunity, a project idea,
            or just a conversation about technology, I'd love to connect.
          </p>
          <a className="email-link" href="mailto:dhvani2548@gmail.com">
            dhvani2548@gmail.com ↗
          </a>
          <p className="contact-note">
            Replace this placeholder with your actual email address.
          </p>
        </div>

        <form className="contact-form" onSubmit={handleSubmit} noValidate>
          <label htmlFor="name">Your name</label>
          <input
            id="name"
            name="name"
            value={form.name}
            onChange={handleChange}
            placeholder="Enter your name"
            autoComplete="name"
          />
          {errors.name && <small className="error">{errors.name}</small>}

          <label htmlFor="email">Email address</label>
          <input
            id="email"
            name="email"
            type="email"
            value={form.email}
            onChange={handleChange}
            placeholder="you@example.com"
            autoComplete="email"
          />
          {errors.email && <small className="error">{errors.email}</small>}

          <label htmlFor="message">Your message</label>
          <textarea
            id="message"
            name="message"
            value={form.message}
            onChange={handleChange}
            placeholder="Tell me about your idea..."
            rows="5"
          />
          {errors.message && <small className="error">{errors.message}</small>}

          <button type="submit" className="btn primary submit-btn">
            Send Message ↗
          </button>

          {submitted && (
            <p className="success">
              Validation successful! This demo form does not send messages yet.
            </p>
          )}
        </form>
      </div>
    </section>
  );
}

function Footer() {
  return (
    <footer className="footer">
      <a href="#home" className="logo">dhvani<span>.</span></a>
      <p>Designed & built with React.</p>
      <a href="#home">Back to top ↑</a>
    </footer>
  );
}

export default function App() {
  const [dark, setDark] = useState(true);

  return (
    <div className={dark ? "app dark" : "app light"}>
      <Header dark={dark} setDark={setDark} />
      <main>
        <Hero />
        <About />
        <Skills />
        <Projects />
        <Contact />
      </main>
      <Footer />
    </div>
  );
}
