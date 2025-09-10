Frist = int(input("คะแนนเก็บ: "))
Mit = int(input("คะแนนเก็บ: "))
Final = int(input("คะแนนเก็บ: "))

score = Frist + Mit + Final

if (0 <= Frist <= 30) and (0 <= Mit <= 30) and (0 <= Final <= 40):
    if score >= 80:
     print("A")
    elif score >= 75:
     print("B+")
    elif score >= 70:
     print("B")
    elif score >= 65:
     print("C+")
    elif score >= 60:
     print("C")
    elif score >= 55:
     print("D+")
    elif score >= 50:
     print("D") 
    elif score >= 0:
     print("F") 
    else:
     print("Fail")
else :
    print("input again")

  