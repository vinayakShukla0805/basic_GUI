import json

class Database:

    def add_data(self, name, email, password):

        with open('db.json', 'r') as rf:
            database = json.load(rf)
        
        if email in database:
            print("This user already exist in Database")
            return 0
        else:
            database[email] = [name, password]
            with open('db.json', 'w') as wf:
                json.dump(database, wf)
            print("Registration Successfully")
            return 1