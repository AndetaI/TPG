# Targeted Password Generator

A web-based application built with **Python and Flask** that generates customized password wordlists using user-provided information, such as names, company names, and dates of birth.

The application demonstrates Python string manipulation, combinatorial generation, date parsing, Flask routing, HTML templating, and client-side file export.

## Live Demo

**Try the application here:**

[https://targetedpasswordgenerator.onrender.com/](https://targetedpasswordgenerator.onrender.com/)

The application is deployed using **Render** and is publicly accessible through a web browser.

## Features

- **Personalized Wordlist Generation:** Generates wordlist entries based on names and company names.
- **Date of Birth Variations:** Recognizes multiple date formats and generates different date representations.
- **Leetspeak Substitutions:** Supports common character substitutions, such as `a → @`, `e → 3`, `i → 1`, `o → 0`, and `s → $`.
- **Password Combinations:** Combines different keywords and generates variations with dates and special characters.
- **Customizable Options:** Allows users to enable or disable symbols and leetspeak substitutions.
- **TXT Export:** Downloads generated results as a `.txt` file directly from the browser.
- **Responsive Interface:** Uses Tailwind CSS for a clean, mobile-friendly interface.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Flask | Web framework and routing |
| HTML5 | Application structure |
| Tailwind CSS | Interface styling |
| JavaScript | Client-side TXT export |
| Jinja2 | Dynamic HTML rendering |
| Git & GitHub | Version control and source code management |
| Render | Application hosting and deployment |

## Project Structure

```text
password-wordlist-generator/
│
├── app.py
├── templates/
│   └── index.html
│
├── requirements.txt
└── README.md
```

## Local Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/AndetaI/TPG.git
```

### 2. Navigate to the project directory

```bash
cd TPG-main
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should contain:

```text
Flask
```

### 5. Run the application

```bash
python app.py
```

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

## How It Works

1. Enter a name and/or company name.
2. Optionally provide a date of birth.
3. Enable or disable symbol and leetspeak variations.
4. Click **Gjenero Fjalëkalime** to generate the wordlist.
5. Browse the generated results.
6. Click **Export .txt** to download the results as a text file.
7. Use **Fshij të gjitha** to clear the form and return to the initial page.

### Supported Date Formats

The application accepts the following date formats:

- `YYYY-MM-DD`
- `DD/MM/YYYY`
- `MM/DD/YYYY`
- `YYYY/MM/DD`
- `YYYYMMDD`
- `DDMMYYYY`

## Deployment

The application is hosted on **Render** and connected to a GitHub repository.

Live URL: [https://targetedpasswordgenerator.onrender.com/](https://targetedpasswordgenerator.onrender.com/)

### Updating the Deployed Application

When code changes are made locally, they can be published by pushing the updated files to GitHub:

```bash
git add .
git commit -m "Describe your changes"
git push origin main
```

With automatic deployment enabled, Render detects the new commit and redeploys the application.

Deployment status can be monitored from the Render Dashboard.

## Security Considerations

This application is intended for **authorized cybersecurity and password-strength assessments**.

- Only use information you are authorized to process.
- Do not use generated wordlists to attempt unauthorized access to accounts or systems.
- Avoid entering real personal information or sensitive data into publicly accessible deployments.
- Generated wordlists may contain sensitive information and should be handled securely.
