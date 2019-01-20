from flask import Flask,request from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG']=True

form="""
<!DOCTYPE html>

<html>
    <head>
        <style>
            form{
                background-color: #eee;
                padding: 20px;
                margin:0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin:10px 0;
                width: 540px;
                height:120px;
            }
        </style>
    </head>
    <body>
    <!-- create your form here-->

        <form method="POST">
            <label for="rot_num"> Rotate by:</label>
            <input id="rot_num" type= "text" name="rot" value="0"/>
            <input name="text" type="textarea"/>
            <input type="Submit"/>
        </form>
</body>
</html>
"""
def encrypt():
    




@app.route('/')
def index():
    return form
app.run()