class User:
    def __init__(self, first_name, last_name,email,age):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print("======================")
        print(f"First name is {self.first_name}")
        print(f"Last name is {self.last_name}")
        print(f"email is {self.email}")
        print(f"age is {self.age}")
        print(f"Rewards is {self.is_rewards_member}")
        print(f"Gold card is {self.gold_card_points}")
        print("==================")
    def enrroll(self):
        # self.is_rewards_member = False
        # self.gold_card_points=200
        if self.is_rewards_member==True:
            print("User is a member")
            return False
        self.is_rewards_member = True
        self.gold_card_points=200
    def spend_points(self, amount):
        self.gold_card_points=self.gold_card_points-amount

        


user1=User("athar", "baccouche","baccouche.athar@gmail.com",23 )
user1.display_info()
user1.enrroll()
user1.display_info()
# user1.spend_points(100)
# user1.display_info()
