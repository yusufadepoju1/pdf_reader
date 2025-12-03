import gradio as gr
import pdfplumber
import pandas as pd

def pdf_to_csv(file):
    data = []
    with pdfplumber.open(file.name) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            if tables:
                for table in tables:
                    for row in table:
                        data.append(row)
            else:
                text = page.extract_text()
                if text:
                    for line in text.split("\n"):
                        data.append([line])

    df = pd.DataFrame(data)

    csv_content = df.to_csv(index=False, header=False)
    return csv_content

ui = gr.Interface(
    fn=pdf_to_csv,
    inputs=gr.File(type="filepath", label="Upload PDF"),
    outputs=gr.File(label="CSV Output"),
    title="PDF to CSV Converter",
    description="Upload a PDF and get a CSV extracted from its tables or text."
)

ui.launch()
