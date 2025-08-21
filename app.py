# from flask import Flask, request, render_template, jsonify
# import PyPDF2
# import os

# app = Flask(__name__)
# UPLOAD_FOLDER = 'uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# pdf_text = ""

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload_pdf():
#     global pdf_text
#     file = request.files['pdf']
#     if file and file.filename.endswith('.pdf'):
#         filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#         file.save(filepath)

#         with open(filepath, 'rb') as f:
#             reader = PyPDF2.PdfReader(f)
#             pdf_text = ""
#             for page in reader.pages:
#                 pdf_text += page.extract_text()
#         return "PDF uploaded successfully"
#     return "Invalid file format", 400

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_input = request.json['message']
#     if not pdf_text:
#         return jsonify({'response': 'Please upload a manual first.'})
    
#     # Simulated response (replace with AI logic or RAG later)
#     if user_input.lower() in pdf_text.lower():
#         return jsonify({'response': '✅ This topic is found in the manual.'})
#     else:
#         return jsonify({'response': '❌ This topic is not found in the manual.'})

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, request, render_template, redirect, url_for
import os
from extractor import extract_text_from_pdf
from qa_model import get_answer

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Store extracted content in memory
manual_content = ""

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', response=None)

@app.route('/upload', methods=['POST'])
def upload_manual():
    global manual_content
    file = request.files['manual']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        manual_content = extract_text_from_pdf(filepath)
    return redirect(url_for('index'))

@app.route('/chat', methods=['POST'])
def chat():
    global manual_content
    user_input = request.form['user_input']
    response = get_answer(manual_content, user_input)
    return render_template('index.html', response=response)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
