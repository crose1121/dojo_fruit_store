from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(f"Charging customer {request.form['first_name']} {request.form['last_name']} for {request.form['strawberry']} strawberries")
    print(f"Charging customer {request.form['first_name']} {request.form['last_name']} for {request.form['raspberry']} raspberries")
    print(f"Charging customer {request.form['first_name']} {request.form['last_name']} for {request.form['apple']} apples")
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    