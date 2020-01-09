from flask import Flask, render_template, request, redirect, url_for, flash, jsonify 

from sqlalchemy.engine import create_engine 
from sqlalchemy.orm import sessionmaker 
from database_setup import Base, MenuItem, Restaurant 


engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine 
DBSession = sessionmaker( bind = engine ) 

session = DBSession() 

app = Flask(__name__) 

# Show all restaurants
@app.route('/') 
@app.route('/restaurants') 
def showRestaurants(): 
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants = restaurants)

# Create a new restaurant
@app.route('/restaurants/new', methods=['GET', 'POST']) 
def newRestaurant(): 

    if request.method == 'GET':
        return render_template('newRestaurant.html')
    else: 
        if request.form['name']: 
            newRestaurant = Restaurant(name = request.form['name']) 
        session.add(newRestaurant) 
        session.commit() 
        flash('New restaurant has been created!')
        return redirect(url_for('showRestaurants'))

# Edit a restaurant
@app.route('/restaurants/<int:restaurant_id>/edit', methods=['GET', 'POST']) 
def editRestaurant(restaurant_id):

    restaurantToEdit = session.query(Restaurant).filter_by( id = restaurant_id).one()
    if request.method == 'GET': 
        return render_template('editRestaurant.html', restaurant = restaurantToEdit )
    else: 
        if request.form['name']: 
            restaurantToEdit.name = request.form['name']
        session.add(restaurantToEdit)
        session.commit()
        flash('Restaurant has been edited!')
        return redirect(url_for('showRestaurants'))
    
# Delete a restaurant
@app.route('/restaurants/<int:restaurant_id>/delete', methods=['GET', 'POST']) 
def deleteRestaurant(restaurant_id): 
    restaurantToDelete = session.query(Restaurant).filter_by( id = restaurant_id).one() 
    if request.method == 'GET': 
        return render_template('deleteRestaurant.html', restaurant = restaurantToDelete )
    else:
        session.delete(restaurantToDelete)
        session.commit() 
        flash('Restaurant has been deleted!')
        return redirect(url_for('showRestaurants'))

# -------------------------------------------------------------------------------------------------------------

# Show a restaurant menu 
@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu') 
def showMenu(restaurant_id): 
    restaurant = session.query(Restaurant).filter_by( id = restaurant_id).one()
    items = session.query(MenuItem).filter_by( restaurant_id = restaurant.id).all() 

    return render_template('menu.html', restaurant = restaurant, items = items )

# Create a new menu item 
@app.route('/restaurant/<int:restaurant_id>/menu/new', methods=['GET', 'POST'])
def newMenuItem(restaurant_id): 
    restaurant = session.query(Restaurant).filter_by( id = restaurant_id).one()
    if request.method == 'GET':
        return render_template('newMenuItem.html', restaurant = restaurant )
    else: 
        if request.form['name'] and request.form['description'] and request.form['price'] and request.form['course']: 
            newItem = MenuItem(
                name = request.form['name'], 
                price = request.form['price'], 
                description = request.form['description'], 
                course = request.form['course'],
                restaurant_id = restaurant_id 
            )
            session.add(newItem)
            session.commit()
            flash('New menu item has been created!')
            return redirect(url_for('showMenu', restaurant_id = restaurant_id))

# Edit a menu item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menuitem_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menuitem_id): 
    restaurant = session.query(Restaurant).filter_by( id = restaurant_id).one()
    itemToEdit = session.query(MenuItem).filter_by( id = menuitem_id).one()
    if request.method == 'GET': 
        return render_template('editMenuItem.html', restaurant = restaurant, item = itemToEdit )
    else: 
        if request.form['name']: 
            itemToEdit.name = request.form['name'] 
        if request.form['description']:
            itemToEdit.description = request.form['description']
        if request.form['price']: 
            itemToEdit.price = request.form['price']
        if request.form['course']: 
            itemToEdit.price = request.form['course']
        session.add(itemToEdit)
        session.commit() 
        flash('Menu item has been edited!')
        return redirect(url_for('showMenu', restaurant_id = restaurant_id))

# Delete a menu item 
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menuitem_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menuitem_id): 
    restaurant = session.query(Restaurant).filter_by( id = restaurant_id).one()
    itemToDelete = session.query(MenuItem).filter_by( id = menuitem_id).one() 
    if request.method == 'POST': 
        session.delete(itemToDelete)
        session.commit()
        flash('Menu item has been deleted!')
        return redirect(url_for('showMenu', restaurant_id = restaurant_id))
    return render_template('deleteMenuItem.html', restaurant = restaurant, item = itemToDelete )




if __name__ == '__main__':
    app.secret_key = '5BF6YNNDzKW9b8KqLFrlGKh97qrNQN2bs' 
    app.debug = True 
    app.run( host = '0.0.0.0', port = 5050 )