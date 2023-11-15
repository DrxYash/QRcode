while True:
    import qrcode as qr
    img= qr.make(input("Enter Your Link:-"))
    img.save("QRcode_by_yash.png")
    repeat = input("Do You Wann Again? ")
    if repeat =="no" or repeat == "No":
        break
