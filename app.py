from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload_file():
   if request.method == 'POST':
       f = request.files['file']
       f.save('/backend/uploaded_file.pdf')
       return redirect("../",code=302)
if __name__ == '__main__':
   app.run(debug=True)