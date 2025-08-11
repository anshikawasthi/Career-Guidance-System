
# 🎓 Career Guidance System

The **Career Guidance System** is an intelligent web-based platform designed to assist students in identifying suitable career paths based on their academic performance, skill assessments, and interests. Using Machine Learning algorithms, the system predicts ideal career options and provides valuable resources like related courses, scholarships, and career guidance material.

---

## 📌 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Modules](#modules)
- [Machine Learning Models](#machine-learning-models)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Project Structure](#project-structure)

---

## 🚀 Features

- ✨ Career prediction based on test scores and academic profile.
- 🧠 Machine Learning models (Decision Tree, SVM, XGBoost) for recommendation.
- 💬 Integrated chatbot for student interaction.
- 📚 View and explore recommended courses after 10th and 12th.
- 🎯 Soft skills assessment.
- 🎓 Scholarship suggestions based on eligibility.
- 🔍 Admin dashboard for managing tests, questions, and students.

---

## 🧰 Tech Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Python, Django
- **Database**: SQLite3
- **Machine Learning**: Scikit-learn, pandas, NumPy
- **Chatbot**: Dialogflow / Custom Python-based NLP
- **APIs**: (Optional) Real-time job/career trend APIs

---

## 🧩 Modules

1. **User Authentication** – Login/Register functionality for students and admins.
2. **Skill Assessment** – Objective tests for aptitude, interests, and soft skills.
3. **Career Prediction** – ML-based recommendation based on inputs.
4. **Courses After 10th/12th** – Course suggestions with details and scope.
5. **Scholarship Info** – State/central level scholarship listings.
6. **Chatbot Assistance** – Instant help and guidance through chat.
7. **Admin Panel** – Manage students, test questions, and view statistics.

---

## 🤖 Machine Learning Models

- **Decision Tree Classifier**
- **Support Vector Machine (SVM)**
- **XGBoost Classifier**

The model with the highest accuracy is used in production (accuracy measured using confusion matrix and classification report).

---

## 🛠️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/career-guidance-system.git
cd career-guidance-system

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Run the development server
python manage.py runserver
```

---

## ▶️ Usage

1. Register as a student.
2. Take the skill and interest tests.
3. View predicted careers based on your results.
4. Explore course and scholarship suggestions.
5. Chat with the virtual career counselor for help.

---

## 📁 Project Structure

```
career-guidance-system/
│
├── core/                  # Django app with views, models, urls
├── templates/             # HTML templates
├── static/                # Static files (CSS, JS)
├── ml_models/             # Trained ML model files (.pkl)
├── chatbot/               # Chatbot logic (optional)
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
└── requirements.txt       # Project dependencies
`
