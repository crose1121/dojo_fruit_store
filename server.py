from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():

    x = int(request.form['strawberry']) #Do it like this
    y = int(request.form['raspberry'])
    z = int(request.form['apple'])

    sum = x + y + z

    print(f"Charging customer {request.form['first_name']} {request.form['last_name']} for {sum} fruits")

    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    