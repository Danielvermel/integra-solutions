import PyPDF2
from flask import jsonify

def analyze_file(file):
    try:
        file_extension = file.filename.split('.')[-1].lower()

        if file_extension == 'pdf':
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
        elif file_extension == 'docx':
            doc = docx.Document(file)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text
        else:
            return jsonify(message='Unsupported file type'), 400

        # Process the extracted text or form data here
        print('Extracted Text:', text)
        return jsonify(extracted_text=text)
    except Exception as e:
        return jsonify(message='Error extracting text'), 500
