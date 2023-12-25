from flask import Flask, render_template, request, redirect, session, url_for, flash


app = Flask(__name__, static_url_path='', static_folder='templates')
app.secret_key = 'your_secret_key' 

menu_items = [
    {"name": "Plat 1", "price": 68.99},
    {"name": "Plat 2", "price": 30.99},
    {"name": "Dessert 1", "price": 24.99},
    {"name": "Dessert 2", "price": 19.99},
    {"name": "Boisson 1", "price": 12.99},
    {"name": "Boisson 2", "price": 16.99},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', menu_items=menu_items)

@app.route('/panier')
def panier_page():
    if 'panier' not in session:
        session['panier'] = []

    panier = session['panier']
    total_price = sum(item['price'] for item in panier)

    return render_template('panier.html', panier=panier, total_price=total_price)

@app.route('/add_to_panier', methods=['POST'])
def add_to_panier():
    item_name = request.form.get('item_name')
    item_price = float(request.form.get('item_price'))

    if 'panier' not in session:
        session['panier'] = []

    panier = session['panier']
    panier.append({"name": item_name, "price": item_price})
    session['panier'] = panier

    return redirect(request.referrer)

@app.route('/delete_from_panier', methods=['POST'])
def delete_from_panier():
    item_name = request.form.get('item_name')
    item_price = float(request.form.get('item_price'))
    if 'panier' not in session:
        session['panier'] = []

    panier = session['panier']
    panier = [item for item in panier if not (item['name'] == item_name and item['price'] == item_price)]
    session['panier'] = panier

    return redirect('/panier')

@app.route('/clear_panier', methods=['POST'])
def clear_panier():
    session['panier'] = []

    return redirect('/panier')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, port=8000)
