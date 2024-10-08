# Quiz App

Welcome to the **Quiz App** – a dynamic and user-friendly platform designed for creating, managing, and taking quizzes across various categories.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The Quiz App is developed to offer an engaging way for users to learn and test their knowledge on different topics. This project is created and maintained by [Diyorbek Qodirboyev](https://github.com/diyorbekqodirboyev863).

## Features

- **Multiple Categories**: Supports various categories for quizzes.
- **Easy Quiz Creation**: Admins can effortlessly create quizzes with multiple questions and choices.
- **Real-time Results**: Users can immediately see their quiz results upon submission.
- **User-friendly Interface**: Designed with a simple and intuitive UI for better user experience.

## Screenshots

### Portfolio

![Portfolio](demo/portfolio.png)

### Home Page

![Home Page](demo/home.png)

### Quiz Page

![Quiz Page](demo/quiz.png)

### Submit Quiz

![Submit Quiz](demo/submit-quiz.png)

### Result Page

![Result Page](demo/result.png)

## Installation

To run the Quiz App locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/diyorbekqodirboyev863/quiz-app.git
   ```
   
2. **Navigate to the project directory:**
   ```bash
   cd quiz-app
   ```

3. **Install pipenv if not already installed:**
   ```bash
   pip install pipenv
   ```

4. **Install dependencies:**
   Use pipenv to install all required dependencies.
   ```bash
   pipenv install
   ```

5. **Activate the virtual environment:**
   ```bash
   pipenv shell
   ```

6. **Source code:**
   ```bash
   cd src
   ```

7. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

8. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

9. **Access the app:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

- **Create a Quiz**: Admin users can create quizzes by adding questions and choices through the admin panel.
- **Take a Quiz**: Users can browse available quizzes, select one, and answer the questions.
- **View Results**: After submitting a quiz, users can view their score and correct answers.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For more information or queries, please contact [Diyorbek Qodirboyev](https://github.com/diyorbekqodirboyev863).

---

Thank you for using the Quiz App!