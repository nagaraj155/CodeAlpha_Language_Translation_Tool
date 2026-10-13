# CodeAlpha Language Translation Tool

A beginner-friendly Python web application built for **CodeAlpha AI Internship — Task 1: Language Translation Tool**.

## Features

- Simple web interface built with Streamlit
- Source language selection, including automatic language detection
- Target language selection
- Translation using `deep-translator` and the Google Translate service
- Copyable result area and download as a `.txt` file
- Input validation and friendly error messages
- Supports a selection of common languages, including English, Tamil, Hindi, Telugu, Malayalam, Kannada, French, Spanish, and more

## Requirements

- Python 3.10 or newer recommended
- Internet connection
- Visual Studio Code (recommended)

## Run locally

### 1. Open the project folder

Open this folder in VS Code.

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Start the app

```bash
python -m streamlit run app.py
```

Streamlit will print a local address (usually `http://localhost:8501`). Open it in your browser.

## Test checklist

1. Open the app and confirm that the title and language selectors appear.
2. Enter `Hello, how are you?`, choose English as the source and Tamil as the target, then click **Translate**.
3. Confirm that translated text appears in the result area.
4. Test an empty input and confirm that a warning appears.
5. Try a different language pair.
6. Test the download button.
7. Test with the internet disconnected and confirm the app shows a helpful error.

Translation service responses can vary, and internet access is required.

## Project structure

```text
CodeAlpha_Language_Translation_Tool/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## GitHub repository

Create a public repository named:

`CodeAlpha_Language_Translation_Tool`

Then run the Git commands in the submission instructions. Do not upload your `.venv` folder.

## Internship task mapping

- User interface to enter text and choose source/target languages: implemented
- Send input to a translation service and display the response: implemented
- Optional download feature: implemented

## Limitations

- Requires internet access.
- Uses the Google Translate service through `deep-translator`; availability and results depend on that external service.
- This educational demo is not an official Google product and should not be used to translate confidential information.

## Author

Add your name, internship details, and project date here before submission.
