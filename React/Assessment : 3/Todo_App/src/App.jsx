import { useEffect, useState } from "react";
import TodoForm from "./components/TodoForm";
import TodoList from "./components/TodoList";
import "./App.css";

function App() {
  const [todos, setTodos] = useState(() => {
    try {
      return JSON.parse(localStorage.getItem("taskflow-todos")) || [];
    } catch {
      return [];
    }
  });

  const [theme, setTheme] = useState(
    () => localStorage.getItem("taskflow-theme") || "light"
  );

  const [filter, setFilter] = useState("all");
  const [error, setError] = useState("");

  useEffect(() => {
    localStorage.setItem("taskflow-todos", JSON.stringify(todos));
  }, [todos]);

  useEffect(() => {
    localStorage.setItem("taskflow-theme", theme);
    document.documentElement.setAttribute("data-theme", theme);
  }, [theme]);

  const addTodo = (text) => {
    const cleanText = text.trim();

    if (!cleanText) {
      setError("Please enter a task before adding it.");
      return false;
    }

    setTodos((previous) => [
      {
        id: Date.now(),
        text: cleanText,
        completed: false,
      },
      ...previous,
    ]);

    setError("");
    return true;
  };

  const editTodo = (id, newText) => {
    const cleanText = newText.trim();

    if (!cleanText) {
      setError("Task cannot be empty.");
      return false;
    }

    setTodos((previous) =>
      previous.map((todo) =>
        todo.id === id ? { ...todo, text: cleanText } : todo
      )
    );

    setError("");
    return true;
  };

  const deleteTodo = (id) => {
    setTodos((previous) => previous.filter((todo) => todo.id !== id));
    setError("");
  };

  const toggleTodo = (id) => {
    setTodos((previous) =>
      previous.map((todo) =>
        todo.id === id
          ? { ...todo, completed: !todo.completed }
          : todo
      )
    );
  };

  const clearCompleted = () => {
    setTodos((previous) => previous.filter((todo) => !todo.completed));
  };

  const completedCount = todos.filter((todo) => todo.completed).length;
  const pendingCount = todos.length - completedCount;
  const progress =
    todos.length === 0
      ? 0
      : Math.round((completedCount / todos.length) * 100);

  const filteredTodos = todos.filter((todo) => {
    if (filter === "pending") return !todo.completed;
    if (filter === "completed") return todo.completed;
    return true;
  });

  return (
    <div className="app">
      <div className="background-shape shape-one"></div>
      <div className="background-shape shape-two"></div>

      <main className="container">
        <header className="topbar">
          <a className="brand" href="/">
            <span className="brand-icon">✓</span>
            <span>TaskFlow</span>
          </a>

          <button
            className="theme-toggle"
            onClick={() =>
              setTheme((current) =>
                current === "light" ? "dark" : "light"
              )
            }
            aria-label="Toggle theme"
            title="Switch theme"
          >
            {theme === "light" ? "🌙" : "☀️"}
            <span>{theme === "light" ? "Dark mode" : "Light mode"}</span>
          </button>
        </header>

        <section className="welcome-section">
          <div>
            <p className="eyebrow">YOUR PERSONAL WORKSPACE</p>
            <h1>Make today count<span>.</span></h1>
            <p className="welcome-text">
              Organize your day, focus on what matters, and get things done.
            </p>
          </div>
          
        </section>

        <section className="stats-grid">
          <div className="stat-card">
            <div className="stat-icon purple">📋</div>
            <div>
              <p>Total Tasks</p>
              <h2>{todos.length}</h2>
            </div>
          </div>

          <div className="stat-card">
            <div className="stat-icon orange">⏳</div>
            <div>
              <p>Pending</p>
              <h2>{pendingCount}</h2>
            </div>
          </div>

          <div className="stat-card">
            <div className="stat-icon green">🎯</div>
            <div>
              <p>Completed</p>
              <h2>{completedCount}</h2>
            </div>
          </div>
        </section>

        <section className="progress-card">
          <div className="progress-heading">
            <div>
              <h3>Daily Progress</h3>
              <p>Keep going, you're doing great!</p>
            </div>
            <strong>{progress}%</strong>
          </div>

          <div className="progress-track">
            <div
              className="progress-fill"
              style={{ width: `${progress}%` }}
            ></div>
          </div>
        </section>

        <section className="todo-card">
          <div className="section-heading">
            <div>
              <h2>My Tasks</h2>
              <p>Write it down. Make it happen.</p>
            </div>
            <span className="task-count">{pendingCount} left</span>
          </div>

          <TodoForm onAdd={addTodo} error={error} />

          <div className="filter-row">
            <div className="filters">
              {["all", "pending", "completed"].map((item) => (
                <button
                  key={item}
                  className={`filter-btn ${filter === item ? "active" : ""}`}
                  onClick={() => setFilter(item)}
                >
                  {item.charAt(0).toUpperCase() + item.slice(1)}
                </button>
              ))}
            </div>

            {completedCount > 0 && (
              <button className="clear-btn" onClick={clearCompleted}>
                Clear completed
              </button>
            )}
          </div>

          <TodoList
            todos={filteredTodos}
            onEdit={editTodo}
            onDelete={deleteTodo}
            onToggle={toggleTodo}
          />

          <div className="todo-footer">
            <span>✨ Small steps lead to big results.</span>
            <span>{todos.length} total</span>
          </div>
        </section>

        <footer className="page-footer">
          Made with <span>♥</span> and a little productivity.
        </footer>
      </main>
    </div>
  );
}

export default App;