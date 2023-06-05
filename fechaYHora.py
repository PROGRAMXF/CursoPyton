import datetime as d

HH =d.datetime.now()
print(HH)


H = HH.hour
m = HH.minute

print("Son las: ", H, " : ", m)
if(H >= 0 and m <= 59) and  (H <= 11 and m <= 59):
    print("Buenos dias")

elif(H >= 12 and m <= 59) and (H <= 18 and m <= 59):
    print("Buenas tardes")

else:
    print("Buenas noches")