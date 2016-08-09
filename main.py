from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/',methods=['POST'])
def indes():

    name = str(request.form)
    #name = id
    with open('test.txt', 'w') as f:
        f.write(name)


    return render_template('index.html', name=name)


app.run()