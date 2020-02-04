from flask import Flask, request
from models import db, ChargeNetwork

app = Flask(__name__)

POSTGRES = {
    'user': 'postgres',
    'pw': 'coderslab',
    'db': 'enelion',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def main():
    return 'Hello World!'


@app.route('/records', methods=['GET', 'POST'])
def handle_records():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_record = ChargeNetwork(lat=data['lat'], lng=data['lng'], unit_value=data['unit_value'])
            db.session.add(new_record)
            db.session.commit()
            return {
                "message": f"Record with Latitude {new_record.lat} and Longitude {new_record.lng} has been created "
                           f"successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        records = ChargeNetwork.query.all()
        results = [
            {
                "id": record.id,
                "lat": record.lat,
                "lng": record.lng,
                "unit_value": record.unit_value,
                "time_created": record.time_created,
                "time_updated": record.time_updated
            } for record in records]

        return {"count": len(results), "records": results}


@app.route('/records/<record_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_record(record_id):
    record = ChargeNetwork.query.get_or_404(record_id)

    if request.method == 'GET':
        response = {
            "lat": record.lat,
            "lng": record.lng,
            "unit_value": record.unit_value,
            "time_created": record.time_created,
            "time_updated": record.time_updated
        }
        return {"message": "success", "car": response}

    elif request.method == 'PUT':
        data = request.get_json()
        record.lat = data['lat']
        record.lng = data['lng']
        record.unit_value = data['unit_value']
        db.session.add(record)
        db.session.commit()
        return {"message": f"Record with Latitude {record.lat} and Longitude {record.lng} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(record)
        db.session.commit()
        return {"message": f"Car {record.name} successfully deleted."}


app.config['DEBUG'] = True
if __name__ == '__main__':
    app.run()
