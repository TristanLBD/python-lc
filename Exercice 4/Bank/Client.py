class Client:
    def __init__(self, name: str, firstName: str, ID: str):
        self.name = name
        self.firstName = firstName
        self.ID = ID
    
    def __str__(self):
        return f"Client {self.name} {self.firstName} (ID: {self.ID})"