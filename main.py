from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string("""
    <html>
      <head>
        <title>User Manual Assistant</title>
      </head>
      <body style="font-family: Arial; background-color: #f9f9f9; padding: 20px;">
        <div style="max-width: 800px; margin: auto; padding: 30px; background: white; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
          <h2 style="text-align: center; color: #2c3e50;">📘 User Manual Chat Assistant</h2>
          <form method="post" action="/ask" style="margin-top: 30px;">
            <label for="question" style="font-weight: bold;">Enter your question:</label><br>
            <textarea id="question" name="question" rows="5" cols="60" required
                      style="width: 100%; padding: 10px; margin-top: 10px; font-size: 16px;"></textarea><br>
            <input type="submit" value="Ask" 
                   style="margin-top: 15px; padding: 10px 20px; background-color: #2c3e50; color: white; border: none; cursor: pointer;">
          </form>
          {% if answer %}
            <div style="margin-top: 30px; padding: 20px; background-color: #ecf0f1; border-radius: 8px;">
              <strong>Answer:</strong><br>{{ answer }}
            </div>
          {% endif %}
        </div>
      </body>
    </html>
    """, answer=None)

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.form["question"]
    
    # Simulated response (replace with your AI/ML logic)
    answer = "This is a sample answer for: " + user_question

    return render_template_string("""
    <html>
      <head>
        <title>User Manual Assistant</title>
      </head>
      <body style="font-family: Arial; background-color: #f9f9f9; padding: 20px;">
        <div style="max-width: 800px; margin: auto; padding: 30px; background: white; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
          <h2 style="text-align: center; color: #2c3e50;">📘 User Manual Chat Assistant</h2>
          <form method="post" action="/ask" style="margin-top: 30px;">
            <label for="question" style="font-weight: bold;">Enter your question:</label><br>
            <textarea id="question" name="question" rows="5" cols="60" required
                      style="width: 100%; padding: 10px; margin-top: 10px; font-size: 16px;">{{ question }}</textarea><br>
            <input type="submit" value="Ask Again" 
                   style="margin-top: 15px; padding: 10px 20px; background-color: #2c3e50; color: white; border: none; cursor: pointer;">
          </form>
          <div style="margin-top: 30px; padding: 20px; background-color: #ecf0f1; border-radius: 8px;">
            <strong>Answer:</strong><br>{{ answer }}
          </div>
        </div>
      </body>
    </html>
    """, question=user_question, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
2