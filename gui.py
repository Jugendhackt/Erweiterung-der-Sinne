#!/usr/bin/python3
import tkinter
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

root = tkinter.Tk()

width, height = root.winfo_screenwidth(), root.winfo_screenheight()

root.overrideredirect(1)

root.geometry("%dx%d+0+0" % (width, height))


root.config(background='black')

def getSerialInput():
       return ser.readline().decode()

def close():
	root.quit()

closeButton = tkinter.Button(root, text="X", command=close)
closeButton.config(fg='red')
closeButton.pack()

tempVar = tkinter.StringVar()
tempVar.set("Temp: ")
tempLabel = tkinter.Label(root, textvariable=tempVar, relief=tkinter.RAISED)
tempLabel.config(font=("Courier", 30), fg='green', bg='black')
tempLabel.pack()

hPaVar = tkinter.StringVar()
hPaVar.set("hPa: ")
hPaLabel = tkinter.Label(root, textvariable=hPaVar, relief=tkinter.RAISED)
hPaLabel.config(font=("Courier", 30), fg='green', bg='black')
hPaLabel.pack()

altitudeVar = tkinter.StringVar()
altitudeVar.set("Altitude: ")
altitudeLabel = tkinter.Label(root, textvariable=altitudeVar, relief=tkinter.RAISED)
altitudeLabel.config(font=("Courier", 30), fg='green', bg='black')
altitudeLabel.pack()

humidityVar = tkinter.StringVar()
humidityVar.set("Humidity: ")
humidityLabel = tkinter.Label(root, textvariable=humidityVar, relief=tkinter.RAISED)
humidityLabel.config(font=("Courier", 30), fg='green', bg='black')
humidityLabel.pack()

gasSensorVar = tkinter.StringVar()
gasSensorVar.set("Gas: ")
gasSensorLabel = tkinter.Label(root, textvariable=gasSensorVar, relief=tkinter.RAISED)
gasSensorLabel.config(font=("Courier", 30), fg='green', bg='black')
gasSensorLabel.pack()

def mainloop():
	root.after(100, mainloop)
	inputRaw = getSerialInput().strip()
	print(inputRaw) 
	inputArray = inputRaw.split(",")
	for input in inputArray:
		if input.find(":") == -1:
			return
		inputSplit = input.split(":")
		type = inputSplit[0]
		value = inputSplit[1]
		if type == "temp":
			tempVar.set("Temp: " + value)
		elif type == "hPa":
			hPaVar.set("hPa: " + value)
		elif type == "altitude":
			altitudeVar.set("Alitutde: " + value + " m")
		elif type == "humidity":
			humidityVar.set("Humidity: " + value + " %")
		elif type == "gassensor":
			gasSensorVar.set("Gas: " + value)
	root.update_idletasks()
root.after(100, mainloop)
root.mainloop()

