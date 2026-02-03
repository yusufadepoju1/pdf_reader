
# PDF to CSV Converter

A lightweight web application built with **Python** and **Flask** that allows users to upload a PDF file, extract its tabular or textual data, and download the results as a structured **CSV file**.

## Features

* **Table Extraction:** Automatically identifies and extracts tables from PDF pages using `pdfplumber`.
* **Fallback Text Extraction:** If no tables are found, it extracts raw text line-by-line to ensure no data is lost.
* **Clean Web Interface:** Simple upload/download flow.
* **Secure File Handling:** Uses `werkzeug` to sanitize filenames and manage uploads safely.

---

## Prerequisites

Before running the application, ensure you have Python 3.x installed. You will also need the following libraries:

* **Flask:** The web framework.
* **pdfplumber:** For advanced PDF data extraction.
* **pandas:** For data structuring and CSV generation.

---

##  Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

```


2. **Install dependencies:**
```bash
pip install flask pdfplumber pandas

```


3. **Project Structure:**
Ensure your directory looks like this:
```text
.
├── app.py              # The Python code provided
├── uploads/            # Created automatically to store files
└── templates/
    └── index.html      # Your HTML upload form

```


4. **Run the application:**
```bash
python app.py

```


The app will be available at `http://127.0.0.1:5000`.

---

## How It Works

1. **Upload:** The user selects a `.pdf` file via the web interface.
2. **Processing:** * The app saves the file to the `/uploads` folder.
* `pdfplumber` iterates through each page.
* It prioritizes `extract_tables()`. If a table exists, it preserves the row/column structure.
* If no table is detected, it falls back to `extract_text()`.


3. **Export:** The data is converted into a Pandas DataFrame and saved as a `.csv`.
4. **Download:** The browser automatically prompts the user to download the generated CSV file.

---
