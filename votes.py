from users import User

class VotingSystem:
    parties = {"PTI" : 0, "MQM" : 0, "PLMN" : 0, "PPP" : 0, "JI" : 0}

    def vote(self):
        username = input("Enter your username to vote: ")
        password = input("Enter your password to vote: ")
        user = User.authenticate_user(username, password)
        if user: 
            if user.has_voted:
                print("You already voted.")
                return
            print("Parties: PTI, MQM, PMLN, PPP, JI")
            choice = input("Enter the party name you want to vote for: ").upper()
            if choice in self.parties:
                self.parties[choice] += 1
                user.has_voted = True
                print("Vote cast Successfully.")
            else:
                print("Invalid party choose.")
        else:
            print("Invalid username or password.")

    def view_results(self):
        print("\n Voting Results: ")
        for party, votes in self.parties.items():
            print(f"Party {party} : {votes} votes")