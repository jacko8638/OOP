class Member:
    surname
    firstname
    annualFee
    def new(self, mySurname, myFirstName, myAnnualFee):
    surname = mySurname
    firstname = myFirstName
    annualFee = myAnnualFee



    def amendDetails(self, mySurname, myfirstname, myAnnualFee):
    (leave this procedure incomplete)

    (other procedures – do not complete)


class JuniorMember(Member):
    dateOfBirth

    def new1(self, mySurname, myFirstname, myAnnualFee, myDateOfBirth):
        dateOfBirth = myDateOfBirth


    def ammendFee(self, myAnnualFee):
        AnnualFee = myAnnualFee


    def getDoB():
        return dateOfBirth




Jmember1 = JuniorMember(“Mason”, “Harry”, 25.00, “12/12/2004”)

