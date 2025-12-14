from validations.validators import not_null

class UserRequestDto:
    def __init__(self, name, email, password):
        self._data = {}
        self.name = name
        self.email = email
        self.password = password

    @property
    def name(self):
        return self._data.get("name")

    @name.setter
    def name(self, value):
        not_null(value, 'nome') #Verifica se o valor é nulo ou vazio e lança uma exceão
        self._data['name'] = value

