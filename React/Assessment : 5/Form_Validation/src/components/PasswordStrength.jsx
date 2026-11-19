
function PasswordStrength({ password }) {
  const checks = [
    password.length >= 8,
    /[A-Z]/.test(password),
    /[a-z]/.test(password),
    /[0-9]/.test(password),
    /[^A-Za-z0-9]/.test(password)
  ];

  const score = checks.filter(Boolean).length;

  const strength =
    score <= 2
      ? "Weak"
      : score <= 4
      ? "Medium"
      : "Strong";

  return (
    <div className="password-strength">
      <div className="strength-bars">
        {[1, 2, 3, 4, 5].map((item) => (
          <span
            key={item}
            className={item <= score ? `filled ${strength.toLowerCase()}` : ""}
          />
        ))}
      </div>

      <p>
        Password strength: <strong>{password ? strength : "Not entered"}</strong>
      </p>
    </div>
  );
}

export default PasswordStrength;
