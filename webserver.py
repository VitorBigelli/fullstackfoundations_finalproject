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
    print('Restaurants: %s' % restaurants)
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
        return redirect(url_for('showRestaurants'))
    
# Delete a restaurant
@app.route('/restaurants/<int:restaurant_id>/delete', methods=['GET', 'POST']) 
def deleteRestaurant(restaurant_id): 
    return render_template('deleteRestaurant.html', restaurant_id = restaurant.id )

# -------------------------------------------------------------------------------------------------------------

# Show a restaurant menu 
@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu') 
def showMenu(restaurant_id): 
    return render_template('menu.html', restaurant = restaurant, items = items )

# Create a new menu item 
@app.route('/restaurant/<int:restaurant_id>/menu/new', methods=['GET', 'POST'])
def newMenuItem(restaurant_id): 
    return render_template('newMenuItem.html', restaurant = restaurant )

# Edit a menu item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menuitem_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menuitem_id): 
    return render_template('editMenuItem.html', restaurant = restaurant, item = item )

# Delete a menu item 
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menuitem_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menuitem_id): 
    return render_template('deleteMenuItem.html', restaurant = restaurant, item = item )




if __name__ == '__main__':
    app.secret_key = '5BF6YNNDzKW9b8KqLFrlGKh97qrNQN2bs' 
    app.debug = True 
    app.run( host = '0.0.0.0', port = 5050 )