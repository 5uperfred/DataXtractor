import pdftotext


def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, "rb") as file:
        pdf = pdftotext.PDF(file)
        for page in pdf:
            text += page
    return text
