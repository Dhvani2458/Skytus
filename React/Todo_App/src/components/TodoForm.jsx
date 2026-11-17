import { useState } from "react";

function TodoForm({ onAdd, error }) {
  const [task, setTask] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

    const added = onAdd(task);

    if (added) {
      setTask("");
    }
  };

  return (
    <form className="todo-form" onSubmit={handleSubmit}>
      <div className="input-wrapper">
        <span className="input-icon">✍️</span>
        <input
          type="text"
          placeholder="What do you need to get done?"
          value={task}
          onChange={(event) => setTask(event.target.value)}
          maxLength={100}
          aria-label="Enter a new task"
        />
      </div>

      <button type="submit" className="add-btn">
        <span>+</span> Add Task
      </button>

      {error && <p className="error-message">⚠ {error}</p>}
    </form>
  );
}

export default TodoForm;