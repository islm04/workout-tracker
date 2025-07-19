# 🏋️‍♂️ Exercise Logger with Nutritionix and Sheety APIs

This project is a simple Python app that helps you log your workouts.  
It takes your exercise description in **natural language** (like "I ran 2 km and did 20 push-ups"), calculates the burned calories using **Nutritionix API**, and automatically logs the data into a **Google Sheet** using **Sheety API**.

---

## 🧠 Concept Overview

This app demonstrates how to integrate APIs and manage data using Python. It brings together real-world development concepts such as:

### 1. 🌱 Environment Variables & Security

Instead of hardcoding sensitive information (like API keys), this app stores them in a `.env` file and loads them using the `python-dotenv` library.

- ✅ Protects your credentials
- ✅ Makes your code cleaner

### 2. 🔗 Using External APIs (Nutritionix)

The app sends the user's exercise input to the **Nutritionix API**, which uses NLP to understand what exercises were performed. It returns detailed data such as:

- Exercise name
- Duration (in minutes)
- Calories burned

This means **you don’t need to calculate calories yourself** — the API handles that for you.

### 3. 🧾 Logging to Google Sheets (Sheety API)

The structured data from Nutritionix is then sent to **Sheety**, which acts like a backend by writing the data to a **Google Sheet**.

You log:

- 📅 Date
- 🕒 Time
- 💪 Exercise Name
- ⏱️ Duration
- 🔥 Calories Burned

Sheety accepts this data through a `POST` request, and the spreadsheet gets updated instantly.

### 4. 🕒 Time & Date Tracking

Python’s `datetime` module is used to add the **current date and time** to each exercise log. This helps you track when exactly you did the workout.

- Example:
  - Date: `18/07/2025`
  - Time: `16:30:22`

### 5. 🔐 Basic Authentication

The Sheety API requires a token for authentication, which is passed in the request headers. This keeps your sheet **private and secure**.

---

## 🧰 Technologies Used

| Tool/Library     | Purpose                              |
|------------------|--------------------------------------|
| Python           | Core programming language            |
| `requests`       | To make HTTP requests to APIs        |
| `dotenv`         | Load environment variables from `.env`|
| Nutritionix API  | Process and interpret exercise input |
| Sheety API       | Log data into Google Sheets          |

---

## 🔄 Workflow Summary

1. User inputs exercises in natural language.
2. Nutritionix API returns structured workout data.
3. Python script adds current date & time.
4. Workout data is sent to Sheety to log into a spreadsheet.

---

## 🚨 Best Practices

- **Don’t commit `.env` file** to GitHub. Add it to `.gitignore`.
- Keep your API keys and tokens secret.
- Use virtual environments to manage dependencies.

---

## 📦 Install Requirements

```bash
pip install requests python-dotenv
