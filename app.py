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
    try:
        file = request.files['manual']
        if file:
            # Save to /tmp (the only writable dir on Vercel)
            filepath = os.path.join("/tmp", file.filename)
            file.save(filepath)

            # Extract text
            manual_content = extract_text_from_pdf(filepath)

        return redirect(url_for('index'))
    except Exception as e:
        app.logger.error(f"Upload failed: {e}")
        return f"Error: {e}", 500

@app.route('/chat', methods=['POST'])
def chat():
    global manual_content
    user_input = request.form['user_input']
    response = get_answer(manual_content, user_input)
    return render_template('index.html', response=response)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
