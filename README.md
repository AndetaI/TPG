# Targeted Password Generator

A web-based application built with **Python and Flask** that generates customized password wordlists from user-provided information, such as names, company names, and dates of birth.

The application demonstrates Python string manipulation, combinatorial generation, date parsing, Flask routing, HTML templating, and client-side file export.

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

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

### 2. Navigate to the project directory

```bash
cd password-wordlist-generator
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

If you do not have a `requirements.txt` file yet, create one containing:

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
4. Click **Generate Passwords**.
5. Browse the generated wordlist.
6. Click **Export .txt** to download the results.

### Supported Date Formats

The application accepts the following date formats:

- `YYYY-MM-DD`
- `DD/MM/YYYY`
- `MM/DD/YYYY`
- `YYYY/MM/DD`
- `YYYYMMDD`
- `DDMMYYYY`

## Security Considerations

This application is intended for **authorized cybersecurity education and password-strength assessments**.

- Only use information you are authorized to process.
- Do not use generated wordlists to attempt unauthorized access to accounts or systems.
- Avoid entering real personal information or sensitive data into publicly accessible deployments.
- Generated wordlists may contain sensitive information and should be handled securely.

**Note:** This is an educational project, not a production-ready password auditing solution.

## License

This project is available for educational and personal use. Add a license file to the repository if you wish to specify formal reuse and distribution permissions.
