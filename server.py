from flask import Flask , render_template, redirect, request, url_for
import data_manager

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/products')
def products():
    dicti = data_manager.read_csv('Data/products.csv')
    fieldnames = ["ID", "Product Name", "Product description", "Price", "Currency", "Available units"]
    return render_template("products.html", file=dicti, fieldnames=fieldnames)

@app.route('/our_stores')
def our_stores():
    return render_template("our_stores.html")

@app.route('/products/<id>', methods=['GET', 'POST'])
def show_product(id):
    if request.method == "GET":
        product = data_manager.get_id(id)
        return render_template('product.html', to_display=product, id=id)
    elif request.method == "POST":
        order_id = data_manager.generate_value('order_id', 'Data/orders.csv')
        product_id = id
        quantity = request.form['quantity']
        total_price = int(quantity) * 800
        currency = "USD"
        list_to_write = [order_id, product_id, quantity, total_price, currency]
        data_manager.append_to_csv('Data/orders.csv', list_to_write)
        return redirect(url_for('products'))


@app.route('/admin')
def admin():
    dict = data_manager.read_csv('Data/orders.csv')
    fieldnames = ["Order ID","Product ID","Quantity","Total price","Currency"]
    return render_template("admin.html", file=dict, fieldnames=fieldnames)


if __name__ == "__main__":
    app.run(debug=True)