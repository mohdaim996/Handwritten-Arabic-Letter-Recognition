from flask import Flask,render_template,request
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home():
    mobile = "Mobile" in request.user_agent.string
    if request.method == 'POST' and 'image' in request.form:
        img = request.form['image']
        
        img = img.replace("data:image/jpeg;base64,", "")
        decoded_img = base64.b64decode(img)
        img = Image.open(BytesIO(decoded_img))

        file_name = "img.jpg"
        img.save(file_name, "jpeg")
    elif request.method == 'POST' and not 'image' in request.form:
        print(request.form['cam'])

    return render_template('index.html',mobile = mobile)
@app.route('/mob', methods=['POST','GET'])
def mob():
    mobile = "Mobile" in request.user_agent.string
    if request.method == 'POST':
        print(request.form)
        print(request.data)
    return render_template('index.html',mobile = mobile)
if __name__ == '__main__':
   print("-- DEBUG MODE ----")
   app.run(debug=True, port='5000')
   