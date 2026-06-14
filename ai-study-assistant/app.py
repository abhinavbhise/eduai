from flask import Flask, render_template, request
from google import genai

app = Flask(__name__)

client = genai.Client(api_key="YOUR GENERATED_API_KEY")

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""

    if request.method == "POST":
        question = request.form["question"]

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=f"""
You are EduAI.

Rules:
- Maximum 80 words
- Use markdown
- Use headings
- Use bullet points
- No introductions
- No conclusions
- Be concise

Question:
{question}
"""
            )
            answer = response.text
        except Exception as e:
            answer = str(e)

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
