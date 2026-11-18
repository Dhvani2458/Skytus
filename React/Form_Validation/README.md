# Form Validation App

A responsive React application that validates user input in real time and provides clear error messages. It checks required fields, email format, password strength, and password confirmation before allowing form submission.

## 🌐 Live Demo

[**View Form Validation App**](https://formvalidation-henna.vercel.app/)

## ✨ Features

- **Real-Time Validation:** Validates fields as users enter information.
- **Required Field Validation:** Ensures all fields are completed.
- **Email Validation:** Checks whether the entered email address has a valid format.
- **Password Strength:** Requires a strong password with uppercase, lowercase, numbers, and special characters.
- **Confirm Password:** Checks whether both passwords match.
- **Dynamic Error Messages:** Displays and hides error messages based on user input.
- **Input Styling:** Highlights valid and invalid fields.
- **Password Visibility Toggle:** Allows users to show or hide their password.
- **Session Storage:** Temporarily saves form data in the browser session.
- **Form Submission Handling:** Prevents submission when validation errors exist.
- **Success Message:** Displays a confirmation after successful validation.
- **Responsive Design:** Works on desktop and mobile devices.

## 🛠️ Technologies Used

- React.js
- JavaScript (ES6+)
- HTML5
- CSS3
- Vite
- SessionStorage
- Vercel (Deployment)

## 📚 Concepts Covered

### 1. DOM Manipulation
- Dynamically displays and hides error messages.
- Updates input styles based on validation results.
- Changes the UI after successful form submission.

### 2. Events
- `onChange` – Updates input values and performs real-time validation.
- `onBlur` – Validates fields when users leave an input.
- `onSubmit` – Validates all fields before submission.

### 3. Error Handling
- Validates required fields.
- Checks email format.
- Checks password strength.
- Verifies password confirmation.
- Prevents form submission when errors are present.

### 4. SessionStorage
- Saves form data temporarily in the browser.
- Restores saved data after refreshing the page.
- Clears temporary data after successful submission.

## 🚀 Installation and Setup

Follow these steps to run the project locally.

**1. Clone the repository**

```bash
git clone https://github.com/Dhvani2458/Skytus/tree/main/React/Form_Validation
```

**2. Navigate to the project folder**

```bash
cd Form_Validation
```

**3. Install dependencies**

```bash
npm install
```

**4. Start the development server**

```bash
npm run dev
```

**5. Open in browser**

```text
http://localhost:5173
```

## 📁 Project Structure

```text
Form_Validation/
│
├── src/
│   ├── components/
│   │   ├── FormInput.jsx
│   │   └── PasswordStrength.jsx
│   │
│   ├── App.jsx
│   ├── App.css
│   ├── index.css
│   └── main.jsx
│
├── public/
├── index.html
├── package.json
├── package-lock.json
└── README.md
```

## 💻 How to Use

1. Open the Form Validation App.
2. Enter your full name.
3. Enter a valid email address.
4. Create a strong password.
5. Confirm your password.
6. Check the validation messages.
7. Click **Create Account** after completing all fields correctly.

## 🚀 Deployment

The application is deployed using Vercel.

**Live URL:** https://formvalidation-henna.vercel.app/

## 👩‍💻 Author

**Dhvani Tandel**

Developed as part of an internship practical assignment to understand form validation, React events, dynamic UI updates, error handling, and browser storage.
