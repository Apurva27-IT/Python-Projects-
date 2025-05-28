import qrcode 

# Taking UPI ID as an input 
upi_id = input("Enter the UPI ID : ")

#upi://pay?pa=UPI_ID&pn=Name&am=Amount&cu=CURRENCY&tn=MESSAGE 

#Defining the payment URL based on the UPI ID and the payment app 
#You can modify these URLs based on the  payment apps you want to support 

phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
google_pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

# Create QR Codes for each payment App 
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#Save the QRcode to image file (Optional)
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay.png")

#Diaplay the QR Codes(You may need to install PIL ?PILLOW Library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()


