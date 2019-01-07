from .models import Case, Profile, Passwords
from .encryption import decrypt
def main(inpUsername,inpPassword):

    objList = Case.objects.all()
    myObj = Case()
    for obj in objList:
        if obj.username == inpUsername and obj.password == inpPassword:
            myObj = obj
            break
    myProfile = Profile()
    myProfile = myObj.place

    PasswordObjects = Passwords.objects.all()

    myDict = []

    for obj in PasswordObjects:
        if obj.belongs_to == myProfile:
            myList = []
            myList.append(obj.website)
            myList.append(obj.email)
            password = decrypt(obj.eccrypted_password)
            myList.append(password)
            myDict.append(myList)

    return myDict



