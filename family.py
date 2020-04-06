from random import randint #para tener los numeros aleatorios del ID

class Family:
    def __init__(self, last_name):
        self._last_name = last_name
        self._members = []
        self._name = ""
        self._age = []
        self._lucky_number = []

    def _generateId(self):
        return randint(0, 5)
    
    def add_member(self, member):
        member["id"] = self._generateId() # para generar un id random 
        member["last_name"] = self._last_name
        #member["lucky_number"] = self._lucky_number
        #member["age"] = self._age
        self._members.append(member) # le agrega a cada member un id y las name
        return member
    

    def delete_member(self, id):
        obj = self.get_member(id)
        self._members.remove(obj)


    def update_member(self, id, member):
        obj = self.get_member(id)
        obj.update(member)
        return obj


    def get_member(self, id):
        member = list(filter(lambda member: member if member["id"] == id else None, self._members)) #filtre member y me de el member segun id si exite
        return member


    def get_all_members(self):
        return self._members