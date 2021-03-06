from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL
from flask_jwt import JWT, jwt_required, current_identity

app = Flask(__name__)
CORS(app)

#MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Syne@1234'
app.config['MYSQL_DB'] = 'sakila'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

# class User(object):
#     def __init__(self, id, name, email, username, password):
#         self.id = id
#         self.name = name
#         self.email = email
#         self.username = username
#         self.password = password

#     def __str__(self):
#         return "User (id='%s')" % self.id

# def authenticate(username, password):
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM users WHERE username = %s AND password = %s;", [username, password])
#     usr = cur.fetchone()
#     if usr is None:
#         return None
#     else:
#         return usr

# def identity(payload):
#     user_id = payload['identity']
#     cur = mysql.connect.cursor()
#     cur.execute("SELECT * FROM users WHERE id = %s;", [user_id])
#     usr = cur.fetchone()
#     if usr is None:
#         return None
#     else:
#         return usr

# #JWT configuration
# jwt = JWT(app, authenticate, identity)

# @app.route('/api/actor')
# def actors():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM actor")
#     actors = cur.fetchall()
#     cur.close()
#     return jsonify(actors)


# @app.route('/api/actor/<string:id>')
# def actor(id):
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM actor WHERE actor_id = %s", [id])
#     actor = cur.fetchone()
#     cur.close()
#     return jsonify(actor)


@app.route('/api/country')
def countries():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM country ORDER BY country;")
    c = cur.fetchall()
    cur.close()
    return jsonify(c)


@app.route('/api/country/<string:id>')
def country(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM country WHERE country_id = %s", [id])
    c = cur.fetchone()
    cur.close()
    return jsonify(c)


# @app.route('/api/customer')
# def customers():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM customer")
#     cust = cur.fetchall()
#     cur.close()
#     return jsonify(cust)


@app.route('/api/film', methods=['GET'])
def getFilm():
    args1 = int(request.args['limit'])
    cur = mysql.connection.cursor()
    cur.execute("SELECT film_id, title, description, release_year, language_id, rental_duration, rating, special_features, last_update FROM film limit %s;", [args1])
    films = cur.fetchall()
    cur.close()
    return jsonify(films)

@app.route('/api/city')
def cities():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM city")
    cit = cur.fetchall()
    cur.close()
    return jsonify(cit)

@app.route('/api/city/<string:id>')
def cityById(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM city WHERE city_id = %s', [id])
    cty = cur.fetchone()
    cur.close()
    return jsonify(cty)

@app.route('/api/city/country/<string:id>')
def getCityByCountryId(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM city WHERE country_id = %s", [id])
    country_cities = cur.fetchall()
    cur.close()
    return jsonify(country_cities)

# @app.route('/api/category')
# def categories():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM category")
#     cat = cur.fetchall()
#     cur.close()
#     return jsonify(cat)


# @app.route('/api/category/<string:id>')
# def category(id):
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM category WHERE category_id = %s", [id])
#     cat = cur.fetchone()
#     cur.close()
#     return jsonify(cat)


# @app.route('/api/language')
# def languages():
#     cur = mysql.connection.cursor()
#     cur.execute('SELECT * FROM language;')
#     lag = cur.fetchall()
#     cur.close()
#     return jsonify(lag)


# @app.route('/api/language/<string:id>')
# def language(id):
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM language WHERE language_id = %s", [id])
#     lag = cur.fetchone()
#     cur.close()
#     return jsonify(lag)


# @app.route('/api/language/add', methods=['POST'])
# def language_add():
#     n = request.form['name']
#     cur = mysql.connection.cursor()
#     result = cur.execute("INSERT INTO language(name) VALUES(%s)", [n])
#     mysql.connection.commit()
#     cur.close()
#     return jsonify(result)


# @app.route('/api/language/edit/<string:id>', methods=['POST'])
# def language_edit(id):
#     cur = mysql.connection.cursor()
#     n = request.form['name']
#     result = cur.execute(
#         'UPDATE language SET name = %s WHERE language_id = %s', (n, id))
#     mysql.connection.commit()
#     cur.close()
#     return jsonify(result)

# @app.route('/api/user')
# def allUsers():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM users;")
#     usrs = cur.fetchall()
#     cur.close()
#     return jsonify(usrs)

# @app.route('/api/user/<string:id>')
# def getUser(id):
#     cur = mysql.connection.cursor()
#     cur.execute('SELECT * FROM users WHERE id = %s', [id])
#     usr = cur.fetchone()
#     cur.close()
#     return jsonify(usr)

# @app.route('/api/user', methods=['POST'])
# def registerUser():
#     pass

if __name__ == "__main__":
    app.secret_key = 'secret123'
    app.run(debug=True)