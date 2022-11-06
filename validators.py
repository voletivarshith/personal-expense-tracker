class UserValidator:
    def validate(self,firstName,lastName,userName,email,password):
        firstNameMsg = self.noneFieldValidator(firstName,"First Name")
        lastNameMsg = self.noneFieldValidator(lastName,"Last Name")
        userNameMsg = self.uniqueFieldValidator(userName,"username")
        emailMsg = self.uniqueFieldValidator(email,"Email")
        passwordMsg = self.noneFieldValidator(password,"Password")
        if self.isinstanceValidator(firstNameMsg,str):
            return firstNameMsg
        elif self.isinstanceValidator(lastNameMsg,str):
            return lastNameMsg
        elif self.isinstanceValidator(userNameMsg,str):
            return userNameMsg
        elif self.isinstanceValidator(emailMsg,str):
            return emailMsg
        elif self.isinstanceValidator(passwordMsg,str):
            return passwordMsg
        else:
            return True
    def isinstanceValidator(self,type,validator):
        if isinstance(type,validator):
            return True
        else:
            return False
    def uniqueFieldValidator(self,data,field):
        if data=="":
            return "* {0} required field".format(field)
        else:
            # Have to add the unique constraint for username
            pass
        return True
    def noneFieldValidator(self,data,field):
        if data=="":
            return "* {0} required field".format(field)
        return True