def greet():
    print("Hi!!")


greet()
greet()


def greet_member(name, age):
    print(f"Hi {name}, you are {age} years old.")


greet_member("Sumaia", 21)
greet_member("Jannat", 20)


def enroll_member(name, club="Research", fee=500):
    print(f"{name} enrolled in {club} - Fee: {fee} BDT")


enroll_member("Sumaia")
enroll_member("Jannat", "AI")
enroll_member("Naima", "NLP")