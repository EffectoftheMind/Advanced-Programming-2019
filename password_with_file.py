print("--- Password Reset ---")

pass_verify = True

while pass_verify == True:
  newPass = input('''Enter Your New Password
  Cannot Be The Same as Original Password,

  Must Contain:
  1. 6 Characters
  2. 1 Capital Letter
  3. 2 Numbers
  4. 1 Special Character (!&$#@)

  Password: ''')
  print()

  confirmPass = input("Re-Enter The Password: ")
  print()

  lstSpecial = ['!','@',"#","$","%","^","&","*","(",")"]
  lstNums = ['1','2','3','4','5','6','7','8','9','0']
  lstSpecial=["!","@","#","$","%","^","&","*","(",")"]
  lstUppers = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  lstLowers = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  
  #file creation and old passwords
  newFile = open('passwords.txt', 'w')
  newFile.write("abcdeF!23"+"\n")
  newFile.write("zxcbhK#44"+"\n")
  newFile.write("poiuyT&11"+"\n")
  newFile.close()
  
  def appendPass(password):
    newFile = open('passwords.txt', 'a')
    newFile.write(password + "\n")
    newFile.close()

  def hasNums(password):
    digitInPass = 0
    for item in lstNums:
      if item in password:
        digitInPass += 1
    if digitInPass >= 2:
      return True
    else:
      return False
      
  def hasUppers(password):
    capInPass = 0
    for item in lstUppers:
      if item in password:
        capInPass += 1
    if capInPass >= 1:
      return True
    else:
      return False
      
  def hasSpecial(password):
    specInPass = 0
    for item in lstSpecial:
      if item in password:
        specInPass += 1
    if specInPass >= 1:
      return True
    else:
      return False
      
  def passMatch(password):
    newFile = open("passwords.txt", "r")
    for item in newFile:
      if item == password:
        newFile.close()
        return True
      else:
        newFile.close()
        appendPass(password)
        return False
        
  def letterCount(password):
    countChar = 0
    for item in lstUppers:
      if item in password:
        countChar +=1
    for item in lstLowers:
      if item in password:
        countChar +=1
    if countChar >= 6:
      return True
    else:
      return False
      
  def confirmMatch(newPass, passConfirm):
    if newPass == passConfirm:
      return True
    else:
      return False
        
  if letterCount(newPass) == True:
    if hasUppers(newPass) == True:
      if hasNums(newPass) == True:
        if passMatch(newPass) == False:
          if hasSpecial(newPass) == True:
            if confirmMatch(newPass, confirmPass) == True:
              print()
              print("Verified!")

  print()
  print('Error!')
  print()
