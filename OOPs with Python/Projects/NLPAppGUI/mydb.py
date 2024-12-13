import json

class Database:
    
    def __init__(self) -> None:
        pass

    def add_user(self, name, email, password):
        with open(r'OOPs with Python\Projects\NLPAppGUI\db.json', 'r') as rf:
            data = json.load(rf)

        if email in data:
            return False
            
        data[email] = [name, password]
        with open(r'OOPs with Python\Projects\NLPAppGUI\db.json', 'w') as wf:
            json.dump(data, wf)
        return True
    
    def search_and_validate_user(self, email, password):
        with open(r'OOPs with Python\Projects\NLPAppGUI\db.json', 'r') as rf:
            data = json.load(rf)
        
        if email in data:
            if password == data[email][1]:
                return True
            else:
                raise ValueError('Password Mismatch.')
        else:
            raise ValueError('Email is not registered with us.')