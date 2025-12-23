from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# Route untuk memproses form (POST)
@app.route('/submit', methods=['POST'])
def submit():
    # Parsing parameter dari form
    nama = request.form.get('nama')
    pesan = request.form.get('pesan')
    
    # Menampilkan hasil
    return f"""
    <h2>Data yang Anda kirim:</h2>
    <p><strong>Nama:</strong> {nama}</p>
    <p><strong>Pesan:</strong> {pesan}</p>
    <br>
    <a href="/">Kembali ke Form</a>
    """

if __name__ == '__main__':
    app.run(debug=True)