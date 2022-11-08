

import os
# from general import *


from flask import Flask, render_template
application = Flask(__name__)
application.config['SECRET_KEY']=''

@application.route('/')
@application.route('/home')
def home():
	return render_template('home.html')

@application.route('/about')
def about():
	return render_template('about.html')


# if not_execute_on_import:
application.run(debug=1)

# run(reloader=1,debug=1)


#
# animals = [{"name":'hector','type':'cougar'},
# 		   {'name':'alessandro','type':'lion'},
# 		   {'name':'maximo','type':'serpent'}]



# @route('/')
# def index():
# 	return template('index')
#
#
# @route('/static/<filename>')
# def server_static(filename):
# 	return static_file(filename,root='/files')
#
#
#
# @get('/animal')
# def get_all():
# 	return {'animals':animals}
#
#
# @get('/animal/<name>')
# def get_one(name):
# 	the_animal=[x for x in animals if x['name']==name]
# 	return {'animal': the_animal[0]}
#
# @post('/animal')
# def add_one():
# 	new_animal = {'name':request.json.get('name'),
# 				  'type':request.json.get('type')}
# 	animals.append(new_animal)
# 	return {'animals':animals}
#
# @delete('/animal/<name>')
# def remove_one(name):
# 	the_animal = [x for x in animals if x['name']==name]
# 	animals.remove(the_animal[0])
# 	return {'animals':animals}
#



#
#
# @route('/')
# def index():
# 	return template('index.tpl')

# run(host='localhost', port=8080,debug=True)

#
# app = Bottle()
#
# @app.get('/updateData') # For GET method
# def login_form():
# 	return template('index.tpl')
#
# @app.post('/updateData') #For POST method
# def submit_form():
# 	name = request.forms.get('name')
# 	print(name)
# 	return f'<h1>{name}</h1>'
#
#
#
#
# run(app, host='0.0.0.0', port=8000)
#
# app = Bottle()
#
# @app.route('/hello')
# def hello():
#     return "Hello World!"
#
# run(app, host='localhost', port=8080)


#
#
# @route('/querytest')
# def querytest():
# 	param1 = request.query.param1
# 	param2 = request.query.param2
# 	return 'The value of param1 is' + param1 + 'and the values of param2 is ' + param2
#
# @error(404)
# def error404(error):
# 	return '<h1> url does not exist </h1>'
#
#
# @error(405)
# def error405(error):
# 	return '<h1> you cant post</h1>'
#
#
# @error(500)
# def error500(error):
# 	return '<h1> our fault </h1>'
# #
# # @route('/',method='POST')
# # def index():
# # 	return 1/0
#
# @route('/zero')
# def zero():
# 	return 1/0





#
# @route('/login')
# def login():
#     return "<h1>On the login page</h1>"
#
# @route('/register')
# def register():
#     return "<h1>On the register page</h1>"
#
# @route('/article/<id>')
# def article(id):
# 	return '<h1>You are viewing article '+id+'</h1>'
#
# @route('/page/<id>/<name>')
# def page(id,name):
# 	return '<h1> You are viewing page ' +id+ ' with name of ' +name+ '</h1>'
#
# @route('/posted',method='GET')
# def posted():
# 	return '<h1>Posted</h1>'
#
# if not_execute_on_import:
# 	run(debug=0, reloader=1)



