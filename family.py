from random import randint

class Family:
    def __init__(self, last_name):
        self._last_name = last_name
        self._members = []

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["id"] = self._generateId() 
        member["_last_name"] = self._last_name
        self._members.append(member)
        return member
    
    def delete_member(self, id):
        pass

    def update_member(self, id, member):
        pass

    def get_member(self, id):
        member = list(filter(lambda member: member if member["id"] == id else None, self._members)) #filtre member y me de el member segun id si exite
        return member

    def get_all_members(self):
        return self._members