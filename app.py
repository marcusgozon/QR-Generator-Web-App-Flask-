from flask import Flask, render_template, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_qr", methods=["POST"])
def generate_qr():
    url = request.form.get("url")
    file_name = request.form.get("file_name", "qr_code.png")

    if not file_name.lower().endswith(".png"):
        file_name += ".png"

    qr = qrcode.QRCode()
    qr.add_data(url)
    img = qr.make_image()

    # Save to memory instead of Downloads
    img_io = io.BytesIO()
    img.save(img_io, "PNG")
    img_io.seek(0)

    return send_file(img_io, mimetype="image/png", as_attachment=True, download_name=file_name)

if __name__ == "__main__":
    app.run(debug=True)
