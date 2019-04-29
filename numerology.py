import replit
import sqlite3

conn = sqlite3.connect('numbers.db')
print("Database Opened")
c = conn.cursor()

def CreateTable():
  c.execute('CREATE TABLE IF NOT EXISTS Numo(ID INTEGER PRIMARY KEY, Prediction TEXT)')
  conn.commit()
def WriteItems():
  c.execute("INSERT INTO Numo(ID,Prediction) VALUES(1,'Just as Aries, the first sign of the zodiac, is about action and initiation, in numerology, 1 is linked to forward motion. 1 symbolizes a pioneering spirit, independent nature, and innate leadership capabilities. On a bad day, 1 can be be a bit bossy or boastful, hiding any insecurities behind an over-developed self-importance. 1 must remember that although it is first, it can very quickly become the loneliest number. Even the most autonomous 1s need the support of their friends, family, and lovers.')")
  c.execute("INSERT INTO Numo(ID,Prediction) VALUES(2,'2 is linked to sensitivity, balance, and harmony. Within numerology, the 2 vibration assumes the role of the mediator, creating harmony by bringing together dissonant forces through compassion, empathy, and kindness. 2 is linked to psychic abilities and intuition, and if this number appears as a Life Path or Destiny Number, the individual will be astute to subtle energy shifts and emotional nuances. Because 2 is so sensitive, it is very conflict averse, and can end up feeling under-appreciated or unacknowledged. 2 must avoid seeking external validation and, instead, realize that perfect equilibrium needed already exists within.')")
  c.execute("INSERT INTO Numo(ID,Prediction) VALUES(3,'Communication is paramount for 3. Symbolically, 3 represents the output of two joined forces: It is the essence of creation. 3 is highly gifted at expression, seamlessly sharing innovative and pioneering concepts through art, writing, and oration. Your work inspires, motivates, and uplifts others, and 3 finds great joy making others smile. However, 3 is also known to be quite moody, and if 3 feels misunderstood, may withdraw entirely. The escapist tendencies of 3 are easily mitigated by practicing peaceful mindfulness: With such an active imagination, it’s important for 3 to find moments of quiet to reset, restore, and recharge.')")
  c.execute("INSERT INTO Numo(ID,Prediction) VALUES(4,'In numerology, 4 has an earthy-energy and is centered around fortifying its roots. 4 adamantly believes in the physical world, and knows that investing in a solid infrastructure is necessary for building a lasting legacy. Practical, hardworking, and responsible, the 4 vibration is focused on creating logical systems that can support scalable growth. There is a solidity to 4, however, that can quickly devolve into rigidity; 4 must remember that rules are meant to enhance, not inhibit. It’s easy for 4 to become stubborn, so 4 benefits from learning to loosen up and think outside-the-box. 4 will feel liberated and inspired by finding the bravery to take a few bold risks.')")
  c.execute("INSERT INTO Numo(ID,Prediction) VALUES(5,'Free-thinking, adventurous, and progressive, 5 is defined by freedom. 5 needs to experience the world by engaging its five senses: For 5, life lessons are acquired through spontaneous acts of bravery. Akin to Sagittarius energy within astrology, 5 is known for its playful, impuslive, and vivacious spirit. But on the other side of its signature joie de vivre, 5 can become restless and impatient. Since 5 is always seeking discovery, it has a difficult time accepting life’s day-to-day responsibilities — including professional and interpersonal commitments. 5 must remember that when it narrows its gaze, it will discover that the most rewarding exploration exists in its own backyard.')")
  c.execute("INSERT INTO Numo(ID,Prediction) VALUES(6,'6 is recognized for its nurturing, supportive, and empathic nature. A true healer, 6 has the ability to problem solve in both the emotional and physical realms, helping others through its straightforward, yet gentle, approach. 6 has a strong sense of responsibility, and cares deeply for its friends, family, and lovers. This number also can easily communicate with children and animals, displaying a soft tenderness and caretaker spirit. But not everything needs to be parented, and sometimes 6’s protective energy can become domineering and controlling. To avoid carrying the world on its shoulders, 6 must learn to build trust and understanding for others: Simply put, everyone must follow their own unique path.')")
  c.execute("INSERT INTO Numo(ID,Prediction) VALUES(7,'The detectives of numerology, 7 is known for its investigative abilities and analytical skills. Astrologically, the number 7 can be thought of as a blend of Virgo and Scorpio energy: 7 is extremely detail-oriented, but is driven by inner-wisdom as oppossed to tangible realities. 7 has a keen eye, and its astute observations fuel a quick-witted, inventive spirit. Because it can quickly find the flaws in almost any system, 7 is a bit of a perfectionist. 7 will often assume fault, so it’s important for this number to counterbalance its inherent skepticism with an open mind. Not everything will be foolproof — but that’s what makes life fun.')")
  c.execute("INSERT INTO Numo(ID,Prediction) VALUES(8,'8 is all about abundance. Within numerology, this number is linked to material wealth and financial success. Ambitious and goal-oriented, 8 can effortlessly assume leadership positions through its natural magnetism. 8 applies big-picture thinking to broaden its scope, racing up the top of any ladder to reach extraordinary heights. But with great power comes great responsibility: 8 breeds workaholics, and on a bad day, can become excessively controlling and possessive. However, its negative qualities can be lessen by giving back to the community. By using is success to help others, 8 realizes that there is nothing more valuable than contributing to the greater good.')")
  c.execute("INSERT INTO Numo(ID,Prediction) VALUES(9,'As the final single digit within numerology, 9 connotes an old soul. 9 is no stranger to the ups and downs of life — been there, done that. Accordingly, 9 can effortlessly synthesize large quantities of stimuli, psychically connecting the dots to form a cohesive whole. The mission for 9 is to reach its highest state of consciousness, and to help others also achieve this spiritual awareness. 9 isn’t afraid to transform, and its malleable spirit inspires others to explore their own ranges of motion. Since 9, in many ways, has transcended the physical plane, it must constantly remember to anchor itself. 9 must learn to balance the abstract with the tangible, ultimately finding its place at the intersection of fantasy and reality.')")
  c.execute("INSERT INTO Numo(ID,Prediction) VALUES(11,'Master Number 11 revs up the energy of Number 2; its purpose is to heal self and other through its elevated psychic abilities. Often times, Master Number 11''s intuitive gifts are a result of extreme life circumstances: Master Number 11 has no choice but to cultivate extrasensory talents. In numerology, Master Number 11 is connected to spiritual enlightenment, awareness, and philosophical balance.')")
  c.execute("INSERT INTO Numo(ID,Prediction) VALUES(22,'Master Number 22, often referred to as the Master Builder, expands on the vibrations of Number 4. Master Number 22 is inspired to create platforms in the physical realm that transcend immediate realities — by fusing the tangible and intangible, Master Number 22 cultivates a dynamic long-term legacy. Master Number 22''s skills are usually a byproduct of early childhood instability that fuels innovative thought. Industrious, creative, and dependable, Master Number 22 is always on a mission to transform.')")
  conn.commit()
#
#
#
#CreateTable()
#WriteItems()

replit.clear()

reComp = True

sUserBirthday = input("Birthday (MM-DD-YYYY): ")
lstUserBirthday = sUserBirthday.split("-")

sBirthMonth = lstUserBirthday[0]
sBirthDay = lstUserBirthday[1]
sBirthYear = lstUserBirthday[2]

lstBirthMonth = []
lstBirthDay = []
lstBirthYear = []

for char in sBirthMonth:
  lstBirthMonth.append(char)
for char in sBirthDay:
  lstBirthDay.append(char)
for char in sBirthYear:
  lstBirthYear.append(char)
  
iBirthMonthDigit1 = int(lstBirthMonth[0])
iBirthMonthDigit2 = int(lstBirthMonth[1])
  
iBirthDayDigit1 = int(lstBirthDay[0])
iBirthDayDigit2 = int(lstBirthDay[1])

iBirthYearDigit1 = int(lstBirthYear[0])
iBirthYearDigit2 = int(lstBirthYear[1])
iBirthYearDigit3 = int(lstBirthYear[2])
iBirthYearDigit4 = int(lstBirthYear[3])

iMonthAddition = iBirthMonthDigit1 + iBirthMonthDigit2
iDayAddition = iBirthDayDigit1 + iBirthDayDigit2
iYearAddition = iBirthYearDigit1 + iBirthYearDigit2 + iBirthYearDigit3 + iBirthYearDigit4

iCompAddition = iMonthAddition + iDayAddition + iYearAddition

def funStrFormat(UserInfo):
  UserInfo = str(UserInfo)
  strFor1 = UserInfo.replace("(", "")
  strFor2 = strFor1.replace(")", "")
  strFor3 = strFor2.replace("'", "")
  
  print(strFor3)
  
print()

while reComp == True:
  if iCompAddition < 10:
    c.execute("SELECT Prediction FROM Numo")
    pull = c.fetchall()
    tUserInfo = pull[iCompAddition-1]
    funStrFormat(tUserInfo)
    break
  elif iCompAddition == 11:
    c.execute("SELECT Prediction FROM Numo")
    pull = c.fetchall()
    tUserInfo = pull[9]
    funStrFormat(tUserInfo)
    break
  elif iCompAddition == 22:
    c.execute("SELECT Prediction FROM Numo")
    pull = c.fetchall()
    tUserInfo = pull[10]
    funStrFormat(tUserInfo)
    break
  else:
    lstComp = []
    for char in str(iCompAddition):
      lstComp.append(char)
    iCompDigit1 = lstComp[0]
    iCompDigit2 = lstComp[1]
    iCompAddition = int(lstComp[0]) + int(lstComp[1])
