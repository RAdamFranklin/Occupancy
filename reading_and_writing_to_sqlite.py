import serial
import sqlite3

ser =  serial.Serial(portname) #open serial port
sqlite3.connect('databasename.db') #connect to the database

# Request for data
ser.write('7E 00 10 17 01 00 13 A2 00 40 7A AC 88 FF FE 02 44 31 05 CB')

#read in data and save under variable s
#s = ser.read(144)
s = "7E009090013A200407AAC88763E0101010505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505050505DFDFD7"

Start_delimiter=s[0:1]
Length=s[2:5]
Frame_type=s[6:7]
sixtyfour_source_addr=s[8:23]
sixteen_source_addr=s[24:27]
Receiveoptions=s[28:29]
RF_Data=s[30:285]
Checksum=s[286:287]

# for loop counts every 4 numbers in RF_Data
# reading every 4 bytes and converts hexadecimal values to real tempurature values
# placing each tempurature value in array of the converted data
# if all values are converted and read into cd x=65 and data is placed in the sqlite database
x=0
for i in range(0, 252, 4):
x=x+1
Grid_Temp = (int(RF_Data[i:(i+3)],16))/16
# cd is converted data
cd[x]=Grid_Temp
x=x+1
if: x==65

c.execute('INSERT INTO data(t1,t2,...,t64) VALUES(cd[1],cd[2],...,cd[64])')







