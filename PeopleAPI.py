from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample initial data
people = [
    {"id": 1, "name": "Dmitri"},
    {"id": 2, "name": "Yanno"}
    # {"id": 3, "name": "Mahayana"},
]


class People:
    @staticmethod
    def get_all():
        return people

    @staticmethod
    def get_one(person_id):
        person = next((person for person in people if person["id"] == person_id), None)
        if person:
            return person
        else:
            return {"error": "Person not found"}, 404

    @staticmethod
    def create(person_data):
        new_id = max(person["id"] for person in people) + 1
        new_person = {"id": new_id, "name": person_data["name"]}
        people.append(new_person)
        return new_person, 201

    @staticmethod
    def delete(person_id):
        person = next((person for person in people if person["id"] == person_id), None)
        if person:
            people.remove(person)
            return {"message": "Person deleted"}, 200
        else:
            return {"error": "Person not found"}, 404


@app.route('/people', methods=['GET', 'POST'])
def people_handler():
    if request.method == 'GET':
        return jsonify(People.get_all())

    if request.method == 'POST':
        data = request.get_json()
        return People.create(data)


@app.route('/people/<int:person_id>', methods=['GET', 'DELETE'])
def person_handler(person_id):
    if request.method == 'GET':
        return jsonify(People.get_one(person_id))

    if request.method == 'DELETE':
        return People.delete(person_id)


if __name__ == '__main__':
    app.run()
