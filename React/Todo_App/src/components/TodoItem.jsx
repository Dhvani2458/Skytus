function TodoItem({ todo, onToggle, isEditing, editText, onEditText }) {
  return (
    <div className={`todo-item ${todo.completed ? "completed" : ""}`}>
      <label className="checkbox-wrapper">
        <input
          type="checkbox"
          checked={todo.completed}
          onChange={() => onToggle(todo.id)}
          aria-label={`Mark ${todo.text} as ${
            todo.completed ? "pending" : "completed"
          }`}
        />
        <span className="custom-checkbox"></span>
      </label>

      <div className="todo-content">
        {isEditing ? (
          <input
            className="edit-input"
            type="text"
            value={editText}
            onChange={(event) => onEditText(event.target.value)}
            autoFocus
            maxLength={100}
          />
        ) : (
          <span className="todo-text">{todo.text}</span>
        )}
        <small>{todo.completed ? "Completed" : "In progress"}</small>
      </div>

      <div className="todo-actions">
        {isEditing ? (
          <>
            <button
              type="button"
              className="action-btn save-btn"
              data-action="save"
              data-id={todo.id}
              title="Save"
            >
              ✓
            </button>
            <button
              type="button"
              className="action-btn cancel-btn"
              data-action="cancel"
              data-id={todo.id}
              title="Cancel"
            >
              ×
            </button>
          </>
        ) : (
          <>
            <button
              type="button"
              className="action-btn edit-btn"
              data-action="edit"
              data-id={todo.id}
              title="Edit task"
            >
              ✎
            </button>
            <button
              type="button"
              className="action-btn delete-btn"
              data-action="delete"
              data-id={todo.id}
              title="Delete task"
            >
              🗑
            </button>
          </>
        )}
      </div>
    </div>
  );
}

export default TodoItem;