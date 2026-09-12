grade: int = input("Input a grade (as a percentage, without the % sign): ")

if grade >= 90:
   print('A')
elif grade >= 80:
   print('B')
elif grade >= 70:
   print('C')
elif grade >= 60:
   print('D')
else:
   print('F')