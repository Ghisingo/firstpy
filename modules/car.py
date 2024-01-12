
class Car:
     def __init__(self, name , type, model, reg_no, owner, date_of_reg, doc_type, doc):
          self.name = name
          self.type =type
          self.model = model
          self.reg_no = reg_no
          self.owner = owner
          self.date_of_reg = date_of_reg
          self.doc_type = doc_type
          self.doc = doc
     
     def __str__(self):
          return str(f"{self.name} and {self.model}")


car1 = Car(
     name="Car1",
     type="Road",
     model="abcxyz",
     reg_no="22344",
     owner="Aasish Ghising",
     date_of_reg="01-12-2024",
     doc_type="paper",
     doc="Citizenship Card"
)

car2 = Car(
     name="Car2",
     type="Off-Road",
     model="abz",
     reg_no="1111",
     owner="Sajan Adhikari",
     date_of_reg="01-12-2024",
     doc_type="paper",
     doc="Citizenship Card"
)

print(car1)