
import { useState, useEffect } from "react";
import FormInput from "./components/FormInput";
import PasswordStrength from "./components/PasswordStrength";
import "./App.css";

const initialValues = {
  name: "",
  email: "",
  password: "",
  confirmPassword: ""
};

function validateField(name, value, values) {
  switch (name) {
    case "name":
      return value.trim() ? "" : "Full name is required.";

    case "email":
      if (!value.trim()) return "Email is required.";
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)
        ? ""
        : "Please enter a valid email address.";

    case "password":
      if (!value) return "Password is required.";
      if (value.length < 8) return "At least 8 characters are required.";
      if (!/[A-Z]/.test(value)) return "Add at least one uppercase letter.";
      if (!/[a-z]/.test(value)) return "Add at least one lowercase letter.";
      if (!/[0-9]/.test(value)) return "Add at least one number.";
      if (!/[^A-Za-z0-9]/.test(value)) return "Add at least one special character.";
      return "";

    case "confirmPassword":
      if (!value) return "Please confirm your password.";
      return value === values.password ? "" : "Passwords do not match.";

    default:
      return "";
  }
}

function App() {
  const [values, setValues] = useState(() => {
    try {
      const saved = sessionStorage.getItem("validationFormData");
      return saved ? { ...initialValues, ...JSON.parse(saved) } : initialValues;
    } catch {
      return initialValues;
    }
  });

  const [errors, setErrors] = useState({});
  const [touched, setTouched] = useState({});
  const [showPassword, setShowPassword] = useState(false);
  const [submitted, setSubmitted] = useState(false);

  useEffect(() => {
    try {
      sessionStorage.setItem("validationFormData", JSON.stringify(values));
    } catch {
      // Storage may be unavailable in some browser settings.
    }
  }, [values]);

  const handleChange = (event) => {
    const { name, value } = event.target;

    const updatedValues = {
      ...values,
      [name]: value
    };

    setValues(updatedValues);
    setSubmitted(false);

    if (touched[name]) {
      setErrors((previous) => ({
        ...previous,
        [name]: validateField(name, value, updatedValues)
      }));
    }

    // Recheck confirmation if the original password changes.
    if (name === "password" && touched.confirmPassword) {
      setErrors((previous) => ({
        ...previous,
        confirmPassword: validateField(
          "confirmPassword",
          updatedValues.confirmPassword,
          updatedValues
        )
      }));
    }
  };

  const handleBlur = (event) => {
    const { name, value } = event.target;

    setTouched((previous) => ({
      ...previous,
      [name]: true
    }));

    setErrors((previous) => ({
      ...previous,
      [name]: validateField(name, value, values)
    }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    const newErrors = {};

    Object.keys(values).forEach((name) => {
      newErrors[name] = validateField(name, values[name], values);
    });

    setErrors(newErrors);
    setTouched({
      name: true,
      email: true,
      password: true,
      confirmPassword: true
    });

    const hasErrors = Object.values(newErrors).some(
      (error) => error !== ""
    );

    if (hasErrors) {
      setSubmitted(false);
      return;
    }

    setSubmitted(true);

    // Clear temporary data after successful submission.
    sessionStorage.removeItem("validationFormData");
  };

  const resetForm = () => {
    setValues(initialValues);
    setErrors({});
    setTouched({});
    setSubmitted(false);
    sessionStorage.removeItem("validationFormData");
  };

  return (
    <main className="page-container">
      <section className="form-card">
        <div className="brand-icon">✓</div>

        <p className="eyebrow">WELCOME ABOARD</p>
        <h1>Create Your Account</h1>
        <p className="subtitle">
          Fill in your details to get started.
        </p>

        {submitted ? (
          <div className="success-panel">
            <div className="success-icon">✓</div>
            <h2>Registration Successful!</h2>
            <p>
              Your form has been validated successfully.
            </p>
            <button
              type="button"
              className="submit-button"
              onClick={resetForm}
            >
              Create Another Account
            </button>
          </div>
        ) : (
          <form onSubmit={handleSubmit} noValidate>
            <FormInput
              label="Full Name"
              name="name"
              value={values.name}
              placeholder="Enter your full name"
              error={errors.name}
              touched={touched.name}
              onChange={handleChange}
              onBlur={handleBlur}
            />

            <FormInput
              label="Email Address"
              name="email"
              type="email"
              value={values.email}
              placeholder="example@email.com"
              error={errors.email}
              touched={touched.email}
              onChange={handleChange}
              onBlur={handleBlur}
            />

            <FormInput
              label="Password"
              name="password"
              type={showPassword ? "text" : "password"}
              value={values.password}
              placeholder="Create a strong password"
              error={errors.password}
              touched={touched.password}
              onChange={handleChange}
              onBlur={handleBlur}
              rightElement={
                <button
                  type="button"
                  className="toggle-password"
                  onClick={() => setShowPassword(!showPassword)}
                >
                  {showPassword ? "Hide" : "Show"}
                </button>
              }
            />

            <PasswordStrength password={values.password} />

            <FormInput
              label="Confirm Password"
              name="confirmPassword"
              type={showPassword ? "text" : "password"}
              value={values.confirmPassword}
              placeholder="Re-enter your password"
              error={errors.confirmPassword}
              touched={touched.confirmPassword}
              onChange={handleChange}
              onBlur={handleBlur}
            />

            <button type="submit" className="submit-button">
              Create Account →
            </button>

            <p className="form-note">
              Your information is temporarily saved in this browser session.
            </p>
          </form>
        )}
      </section>

      <footer>
        Made with care · Form Validation Project
      </footer>
    </main>
  );
}

export default App;
