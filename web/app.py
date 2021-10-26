from flask import Flask,render_template,request
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        img = request.form['image']
        
        img = img.replace("data:image/jpeg;base64,", "")
        decoded_img = base64.b64decode(img)
        img = Image.open(BytesIO(decoded_img))

        file_name = "img.jpg"
        img.save(file_name, "jpeg")
           

    return render_template('index.html')

if __name__ == '__main__':
   print("-- DEBUG MODE ----")
   app.run(debug=True, port='5000')
   