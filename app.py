from flask import Flask, request, render_template, send_file
from summarizer import summarize_rp
from fpdf import FPDF
from io import BytesIO
import markdown

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    summary_html = ""
    url = ""
    email = ""
    error = ""

    if request.method == "POST":
        url = request.form.get("url")
        email = request.form.get("email")
        if url:
            try:
                summary = summarize_rp(url)
                summary_html = markdown.markdown(summary)
                # TODO: You can implement sending email using SMTP or SendGrid if needed
            except Exception as e:
                error = f"Error: {str(e)}"
        else:
            error = "Please enter a valid URL."

    return render_template(
        "index.html",
        summary=summary,
        summary_html=summary_html,
        url=url,
        email=email,
        error=error
    )

@app.route("/download", methods=["POST"])
def download_pdf():
    summary = request.form.get("summary", "No summary provided")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in summary.split("\n"):
        pdf.multi_cell(0, 10, line)

    pdf_output = BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)

    return send_file(
        pdf_output,
        as_attachment=True,
        download_name="summary.pdf",
        mimetype="application/pdf"
    )

if __name__ == "__main__":
    app.run(debug=True)