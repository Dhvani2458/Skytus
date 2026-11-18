
function FormInput({
  label,
  name,
  type = "text",
  value,
  placeholder,
  error,
  touched,
  onChange,
  onBlur,
  rightElement
}) {
  const isInvalid = touched && error;
  const isValid = touched && !error && value.trim() !== "";

  return (
    <div className="form-group">
      <label htmlFor={name}>{label}</label>

      <div
        className={`input-wrapper ${
          isInvalid ? "invalid" : isValid ? "valid" : ""
        }`}
      >
        <input
          id={name}
          name={name}
          type={type}
          value={value}
          placeholder={placeholder}
          onChange={onChange}
          onBlur={onBlur}
        />

        {rightElement}
      </div>

      {isInvalid && (
        <p className="error-text">{error}</p>
      )}

      {isValid && (
        <p className="success-text">Looks good!</p>
      )}
    </div>
  );
}

export default FormInput;
