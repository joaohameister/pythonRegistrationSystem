class Pessoa:
    def __init__(self):
        self._nome = None
        self._idade = None
        self._email = None

    # Getter
    @property
    def nome(self):
        return self._nome if self._nome else "Em branco"

    # Setter
    @nome.setter
    def nome(self, entry):
        self._nome = entry

    # Getter

    @property
    def idade(self):
        return self._idade if self._idade else "Em branco"

    # Setter
    @idade.setter
    def idade(self, entry):
        self._idade = entry

    # Getter
    @property
    def email(self):
        return self._email if self._email else "Em branco"

    # Setter
    @email.setter
    def email(self, entry):
        self._email = entry
