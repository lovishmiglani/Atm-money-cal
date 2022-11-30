notes = int(input("Enter the number of notes : "))
notes_2k = int(input("enter number of 2000 notes"))
note_500 = int(input("enter the number of 500 notes"))
note_200 = int(input("enter the number of 200 notes"))
note_100 = int(input("enter the number of 100 notes"))
notes_user = notes_2k + note_500 + note_200 + note_100
total_amount = 2000*notes_2k + 500*note_500 + 200*note_200 + 100*note_500
if notes_user!=notes:
    print("there is some errors")
    exit()
print("Total amount of the user : ",total_amount)
