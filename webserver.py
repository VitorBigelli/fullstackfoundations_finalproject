from flask import Flask, render_template, request, redirect, url_for, flash, jsonify 

from sqlalchemy.engine import create_engine 
from sqlalchemy.orm import sessionmaker 
from database_setup import Base, MenuItem, Restaurant 


engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine 
DBSession = sessionmaker( bind = engine ) 

sessions = DBSession() 

app = Flask(__name__) 


#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}


# Show all restaurants
@app.route('/') 
@app.route('/restaurants') 
def showRestaurants(): 
    return render_template('restaurants.html', restaurants = restaurants)

# Create a new restaurant
@app.route('/restaurants/new', methods=['GET', 'POST']) 
def newRestaurant(): 
    return '<html><body> This page will be for making a new restaurant </body></html>'

# Edit a restaurant
@app.route('/restaurants/<int:restaurant_id>/edit', methods=['GET', 'POST']) 
def editRestaurant(restaurant_id): 
    return '<html><body> This page will be for editing restaurant %s </body></html>' % restaurant_id

# Delete a restaurant
@app.route('/restaurants/<int:restaurant_id>/delete', methods=['GET', 'POST']) 
def deleteRestaurant(restaurant_id): 
    return '<html><body> This page will be for editing restaurant %s </body></html>' % restaurant_id

# -------------------------------------------------------------------------------------------------------------

# Show a restaurant menu 
@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu') 
def showMenu(restaurant_id): 
    return '<html><body> This page will show menu for restaurant %s </body></html>' % restaurant_id 

# Create a new menu item 
@app.route('/restaurant/<int:restaurant_id>/menu/new', methods=['GET', 'POST'])
def newMenuItem(restaurant_id): 
    return '<html><body> This page will be for making a new menu item for restaurant %s </body></html>' % restaurant_id 

# Edit a menu item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menuitem_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menuitem_id): 
    return '<html><body> This page will be for editing menu item %s </body></html>' % menuitem_id 

# Delete a menu item 
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menuitem_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menuitem_id): 
    return '<html><body> This page will be for deleting menu item %s </body></html>' % menu_menuitem_iditem 




if __name__ == '__main__':
    app.secret_key = '5BF6YNNDzKW9b8KqLFrlGKh97qrNQN2bs' 
    app.debug = True 
    app.run( host = '0.0.0.0', port = 5050 )