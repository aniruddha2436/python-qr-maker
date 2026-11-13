import qrcode
while True:
    print("\n ---QR CODE MAKER---")
    print("1. link or text")
    print("2. content card")
    print("3. wifi")
    print("4.exit")

    choice = input("Choose an option (1–4): ").strip()
    if choice == "1":
        text = input("Enter link or text:")
        file = input("File name:")
        img = qrcode.make(text)
        img.save(file + ".png")
        print("saved:",file  + ".png")

    elif choice == "2":
        first = input("Enter first name:")
        last = input("Enter last name:")
        phone = input("Enter phone number:")
        email = input("Enter email:")

        full = first+" " +last 
        card = ["Begin:Vcard","VERSION:3.0"]
        card.append("N:"+last+";"+first)
        card.append("FN:"+full)
        card.append("TEL:"+phone)
        card.append("EMAIL:"+email)
        card.append("END:VCARD")
        vcard = "\n".join(card)

        img = qrcode.make(vcard)
        img.save("contact_qr.png")
        print("saved: contact_qr.png")

    elif choice == "3":
        ssid = input("Enter wifi name:")
        pas = input("Enter wifi password:")

        wifi = "WIFI:T:WPA;S:"+ssid+";P:"+pas+";;"
        img = qrcode.make(wifi)
        img.save("wifi_qr.png")
        print("saved:")

    elif choice == "4":
        print("Exiting...")
        break    
    else:
        print("Invalid choice")
        
# requirements:
# run this on terminal: & "$env:LOCALAPPDATA\Python\pythoncore-3.14-64\python.exe" -m pip install qrcode