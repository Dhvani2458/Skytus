import { useState } from "react";
import TodoItem from "./TodoItem";

function TodoList({ todos, onEdit, onDelete, onToggle }) {
  const [editingId, setEditingId] = useState(null);
  const [editText, setEditText] = useState("");

  const handleListClick = (event) => {
    const button = event.target.closest("button[data-action]");
    if (!button) return;

    const { action, id } = button.dataset;
    const todoId = Number(id);

    if (action === "delete") {
      onDelete(todoId);
      if (editingId === todoId) setEditingId(null);
    }

    if (action === "edit") {
      const todo = todos.find((item) => item.id === todoId);
      if (todo) {
        setEditingId(todoId);
        setEditText(todo.text);
      }
    }

    if (action === "save") {
      const saved = onEdit(todoId, editText);
      if (saved) {
        setEditingId(null);
        setEditText("");
      }
    }

    if (action === "cancel") {
      setEditingId(null);
      setEditText("");
    }
  };

  if (todos.length === 0) {
    return (
      <div className="empty-state">
        <div className="empty-icon">📝</div>
        <h3>No tasks here!</h3>
        <p>Add a new task or select another filter.</p>
      </div>
    );
  }

  return (
    <div className="todo-list" onClick={handleListClick}>
      {todos.map((todo) => (
        <TodoItem
          key={todo.id}
          todo={todo}
          onToggle={onToggle}
          isEditing={editingId === todo.id}
          editText={editText}
          onEditText={setEditText}
        />
      ))}
    </div>
  );
}

export default TodoList;