import webbrowser
from flask import Flask,render_template
from dieselandpetrolprice import price
app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():   
    return render_template('home.html')

@app.route('/help')
def help():   
    return render_template('help.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():   
    return render_template('register.html')

@app.route('/about')
def about():   
    return render_template('about.html')

@app.route('/contact')
def contact():   
    return render_template('contact.html')

@app.route('/petrolprice')
def petrolprice():
    fg=price(wiki = "https://www.sify.com/finance/today-petrol-price/")
    return render_template('dieselpetrolprice.html',fuelcamelcase='Petrol',fuel='PETROL',today=fg[0],n=fg[1],A=fg[2],B=fg[3],C=fg[4],D=fg[5])


@app.route('/dieselprice')
def dieselprice():
    fg=price(wiki = "https://www.sify.com/finance/today-diesel-price/")
    return render_template('dieselpetrolprice.html',fuelcamelcase='Diesel',fuel='DIESEL',today=fg[0],n=fg[1],A=fg[2],B=fg[3],C=fg[4],D=fg[5])
if __name__ == '__main__':
    app.run(debug=True,port=2323)

