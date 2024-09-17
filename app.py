from flask import Flask,jsonify,request
from models import db,weather
from config import Config
app=Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
#Routes
@app.route('/',methods=['GET'])
def home():
    locations=weather.query.all()
    return jsonify([{
        'id':w.id,
        'city':w.city,
        'temp':w.temperature,
        "description":w.description,
        "icon":w.icon
    } for w in locations])
@app.route('/weather',methods=['GET'])
def get_weather():
     locations=weather.query.all()
     return jsonify([{
        'id':w.id,
        'city':w.city,
        'temp':w.temperature,
        "description":w.description,
        "icon":w.icon
    } for w in locations])
@app.route('/weather/<int:id>',methods=['GET'])
def getById(id):
    idLocation=weather.query.get(id)
    if idLocation:
        return jsonify({ 'id':idLocation.id,
        'city':idLocation.city,
        'temp':idLocation.temperature,
        "description":idLocation.description,
        "icon":idLocation.icon}),200
    return jsonify({'error':"NOT FOUND"}),404
@app.route('/weatherbyName',methods=['GET'])
def getByName():
    name=request.args.get('name')
    LocationName= weather.query.filter(weather.city.ilike(f'%{name}%')).all()
    if(LocationName):
        return jsonify([{'id':n.id,
                        'city':n.city,
                        'temp':n.temperature}for n in LocationName]),200
    return jsonify({'error':'NOT FOUND'}),404
@app.route('/addCity',methods=['POST'])
def add():
    data=request.get_json()
    new_Weather=weather(
        city=data['city'],
        temperature=data['temperature'],
        description=data['description'],
        icon=data['icon']
    )
    db.session.add(new_Weather)
    db.session.commit()
    return "ADDED"
if __name__ == '__main__':
    app.run(debug=True)
