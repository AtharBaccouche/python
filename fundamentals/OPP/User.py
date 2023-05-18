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
        return self

    def enrroll(self):
        # NINJA BONUS
        # Add logic in the enroll method to check if 
        # they are a member already, and if they are, 
        # print "User already a member." and return False, otherwise return True.
        # if self.is_rewards_member:
        #     print("User is a member")
        #     return self
        # Have this method change the user's member
        # status to True and 
        self.is_rewards_member = True
        self.gold_card_points=200
        return self
    
    def spend_points(self, amount):
        self.gold_card_points=self.gold_card_points-amount
        return self

        


user1=User("athar", "baccouche","baccouche.athar@gmail.com",23 )
# user1.display_info()
# user1.enrroll()
# user1.display_info()
# user1.spend_points(100)
# user1.display_info()

user1.display_info().enrroll().display_info().spend_points(100).display_info()

