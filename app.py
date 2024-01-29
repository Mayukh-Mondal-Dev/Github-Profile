from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



@app.route('/download_pdf', methods=['GET'])
def download_pdf():
    pdf_path = "static/img/Mayukh Resume Jan 2024.pdf"
    return send_file(pdf_path, as_attachment=True)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)