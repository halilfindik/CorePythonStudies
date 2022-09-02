note = float(input("Lütfen notunuzu giriniz (0-100): "))

if (note>=90 and note<=100):
    print("Notunuz AA'dır.")
elif note<90 and note>=85:
    print("Notunuz BA'dır.")
elif note<85 and note>=80:
    print("Notunuz BB'dir.")
elif note<80 and note>=75:
    print("Notunuz CB'dir.")
elif note<75 and note>=65:
    print("Notunuz CC'dir.")
elif note<65 and note>=60:
    print("Notunuz DC'dir.")
elif note<60 and note>=50:
    print("Notunuz DD'dir.")
elif note<50:
    print("Notunuz FF'dir.")
else:
    print("Tanımsız not!")