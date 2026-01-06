class Baby:

    def __init__(self, _id, password, username, first_name, last_name, birth_date):
        self.id = _id
        self.password = password
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.date = birth_date


baby1 = Baby(1, "****", "luna.novak", "Luna", "Novak", "2023-02-15")
