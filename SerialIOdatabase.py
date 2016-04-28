import serial
import sqlite3
import datetime
import time

#open serialport and connect to database
ser =  serial.Serial('COM3',115200) #open serial port
sqlite3.connect('occupancy.db') #connect to the database
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS data (node real, hour real, minute real, second real, microsecond real, month real, day real, year real, t1 real, t2 real, t3 real, t4 real, t5 real, t6 real, t7 real, t8 real, t9 real, t10 real, t11 real, t12 real,\
t13 real, t14 real, t15 real, t16 real, t17 real, t18 real, t19 real, t20 real, t21 real, t22 real, t23 real, t24 real, t25 real, t26 real,\
t27 real, t28 real, t29 real, t30 real, t31 real, t32 real, t33 real, t34 real, t35 real, t36 real, t37 real, t38 real, t39 real, t40 real,\
t41 real, t42 real, t43 real, t44 real,t45 real, t46 real, t47 real, t48 real, t49 real, t50 real, t51 real, t52 real, t53 real, t54 real, \
t55 real, t56 real, t57 real, t58 real, t59 real, t60 real, t61 real, t62 real, t63 real, t64 real, CO2 real, temp real, humid real)')

#array declarations
data=[]
grideye=[]

#infinite loop


def reading1():
        ser.reset_input_buffer()
        ser.reset_output_buffer()

        grideye = []
        data = []

# Request for data
        ser.write(0x7E, 0x00, 0x10, 0x17, 0x01, 0x00, 0x13, 0xA2, 0x00, 0x40, 0x7A, 0xAC, 0x88, 0xFF, 0xFE, 0x02, 0x44, 0x31, 0x05, 0xCB)



#read in data and save under variable s and place in array data
        a = ser.read(1)
        if a != 0x7E:
                reading1()
                return
        a = ser.read(2)
        a = int.from_bytes(a, byteorder = 'big')
        b = ser.read(1)
        if b != 0x90:
                reading1()
                return
        data = ser.read(a-1)

#Break data into more manageable sections
        sixtyfour_source_addr=data[1:9]
        sixteen_source_addr=data[9:11]
        RF_Data=data[13:a]
        

# for loop counts every 2 elements in RF_Data
# joins two element to get complete data point in RF_Datapoint
# converts hexadecimal values to real tempurature values
# placing each tempurature value in array of the converted data(cd) 
        node = RF_Data[0]
        CO2 = RF_Data[1]
        Humid = ((RF_Data[2] << 8) | RF_Data[3])/10
        Temp = ((RF_Data[4] << 8) | RF_Data[5])/10
        
        for i in range(0, 64, 1):
                grideye[i] = (((RF_Data[2*i+6] << 8) | RF_Data[2*i+7])/16)
        
# finds the time
        now = datetime.datetime.now()
        year=now.year
        month=now.month
        day=now.day
        hour=now.hour
        minute=now.minute
        second=now.second
        microsec=now.microsecond

        c.execute('INSERT INTO data(node, hour, minute, second, microsecond, month, day, year, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13,\
        t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, t26, t27, t28, t29, t30, t31, t32, t33, t34, t35, t36, t37, t38, t39, t40, t41, t42,\
        t43, t44, t45, t46, t47, t48, t49, t50, t51, t52, t53, t54, t55, t56, t57, t58, t59, t60, t61, t62, t63, t64, CO2, temp, humid) VALUES(?, ?, ?, ?,\
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,\
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(node, hour, minute, second, microsec, month, day, year, grideye[0], grideye[1],\
        grideye[2], grideye[3], grideye[4], grideye[5], grideye[6], grideye[7], grideye[8], grideye[9], grideye[10], grideye[11], grideye[12], grideye[13],\
        grideye[14], grideye[15], grideye[16], grideye[17], grideye[18],grideye[19], grideye[20], grideye[21], grideye[22], grideye[23], grideye[24],\
        grideye[25], grideye[26], grideye[27], grideye[28], grideye[29], grideye[30], grideye[31], grideye[32], grideye[33], grideye[34], grideye[35],\
        grideye[36], grideye[37], grideye[38], grideye[39], grideye[40], grideye[41], grideye[42], grideye[43], grideye[44], grideye[45], grideye[46],\
        grideye[47], grideye[48], grideye[49], grideye[50], grideye[51], grideye[52], grideye[53], grideye[54], grideye[55], grideye[56], grideye[57],\
        grideye[58], grideye[59], grideye[60], grideye[61], grideye[62], grideye[63], CO2, temp, humid))
        conn.commit

def reading2()
        ser.reset_input_buffer()
        ser.reset_output_buffer()

        grideye = []
        data = []

# Request for data
        ser.write(0x7E, 0x00, 0x10, 0x17, 0x01, 0x00, 0x13, 0xA2, 0x00, 0x40, 0x7A, 0xAC, 0x88, 0xFF, 0xFE, 0x02, 0x44, 0x31, 0x05, 0xCB)



#read in data and save under variable s and place in array data
        a = ser.read(1)
        if a != 0x7E:
                reading2()
                return
        a = ser.read(2)
        a = int.from_bytes(a, byteorder = 'big')
        b = ser.read(1)
        if b != 0x90:
                reading2()
                return
        data = ser.read(a-1)

#Break data into more manageable sections
        sixtyfour_source_addr=data[1:9]
        sixteen_source_addr=data[9:11]
        RF_Data=data[13:a]
        

# for loop counts every 2 elements in RF_Data
# joins two element to get complete data point in RF_Datapoint
# converts hexadecimal values to real tempurature values
# placing each tempurature value in array of the converted data(cd) 
        node = RF_Data[0]
        CO2 = RF_Data[1]
        Humid = ((RF_Data[2] << 8) | RF_Data[3])/10
        Temp = ((RF_Data[4] << 8) | RF_Data[5])/10
        
        for i in range(0, 64, 1):
                grideye[i] = (((RF_Data[2*i+6] << 8) | RF_Data[2*i+7])/16)
        
# finds the time
        now = datetime.datetime.now()
        year=now.year
        month=now.month
        day=now.day
        hour=now.hour
        minute=now.minute
        second=now.second
        microsec=now.microsecond

        c.execute('INSERT INTO data(node, hour, minute, second, microsecond, month, day, year, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13,\
        t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, t26, t27, t28, t29, t30, t31, t32, t33, t34, t35, t36, t37, t38, t39, t40, t41, t42,\
        t43, t44, t45, t46, t47, t48, t49, t50, t51, t52, t53, t54, t55, t56, t57, t58, t59, t60, t61, t62, t63, t64, CO2, temp, humid) VALUES(?, ?, ?, ?,\
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,\
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(node, hour, minute, second, microsec, month, day, year, grideye[0], grideye[1],\
        grideye[2], grideye[3], grideye[4], grideye[5], grideye[6], grideye[7], grideye[8], grideye[9], grideye[10], grideye[11], grideye[12], grideye[13],\
        grideye[14], grideye[15], grideye[16], grideye[17], grideye[18],grideye[19], grideye[20], grideye[21], grideye[22], grideye[23], grideye[24],\
        grideye[25], grideye[26], grideye[27], grideye[28], grideye[29], grideye[30], grideye[31], grideye[32], grideye[33], grideye[34], grideye[35],\
        grideye[36], grideye[37], grideye[38], grideye[39], grideye[40], grideye[41], grideye[42], grideye[43], grideye[44], grideye[45], grideye[46],\
        grideye[47], grideye[48], grideye[49], grideye[50], grideye[51], grideye[52], grideye[53], grideye[54], grideye[55], grideye[56], grideye[57],\
        grideye[58], grideye[59], grideye[60], grideye[61], grideye[62], grideye[63], CO2, temp, humid))
        conn.commit

def reading3()
        ser.reset_input_buffer()
        ser.reset_output_buffer()

        grideye = []
        data = []

# Request for data
        ser.write(0x7E, 0x00, 0x10, 0x17, 0x01, 0x00, 0x13, 0xA2, 0x00, 0x40, 0x7A, 0xAC, 0x88, 0xFF, 0xFE, 0x02, 0x44, 0x31, 0x05, 0xCB)



#read in data and save under variable s and place in array data
        a = ser.read(1)
        if a != 0x7E:
                reading3()
                return
        a = ser.read(2)
        a = int.from_bytes(a, byteorder = 'big')
        b = ser.read(1)
        if b != 0x90:
                reading3()
                return
        data = ser.read(a-1)

#Break data into more manageable sections
        sixtyfour_source_addr=data[1:9]
        sixteen_source_addr=data[9:11]
        RF_Data=data[13:a]
        

# for loop counts every 2 elements in RF_Data
# joins two element to get complete data point in RF_Datapoint
# converts hexadecimal values to real tempurature values
# placing each tempurature value in array of the converted data(cd) 
        node = RF_Data[0]
        CO2 = RF_Data[1]
        Humid = ((RF_Data[2] << 8) | RF_Data[3])/10
        Temp = ((RF_Data[4] << 8) | RF_Data[5])/10
        
        for i in range(0, 64, 1):
                grideye[i] = (((RF_Data[2*i+6] << 8) | RF_Data[2*i+7])/16)
        
# finds the time
        now = datetime.datetime.now()
        year=now.year
        month=now.month
        day=now.day
        hour=now.hour
        minute=now.minute
        second=now.second
        microsec=now.microsecond

        c.execute('INSERT INTO data(node, hour, minute, second, microsecond, month, day, year, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13,\
        t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, t26, t27, t28, t29, t30, t31, t32, t33, t34, t35, t36, t37, t38, t39, t40, t41, t42,\
        t43, t44, t45, t46, t47, t48, t49, t50, t51, t52, t53, t54, t55, t56, t57, t58, t59, t60, t61, t62, t63, t64, CO2, temp, humid) VALUES(?, ?, ?, ?,\
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,\
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(node, hour, minute, second, microsec, month, day, year, grideye[0], grideye[1],\
        grideye[2], grideye[3], grideye[4], grideye[5], grideye[6], grideye[7], grideye[8], grideye[9], grideye[10], grideye[11], grideye[12], grideye[13],\
        grideye[14], grideye[15], grideye[16], grideye[17], grideye[18],grideye[19], grideye[20], grideye[21], grideye[22], grideye[23], grideye[24],\
        grideye[25], grideye[26], grideye[27], grideye[28], grideye[29], grideye[30], grideye[31], grideye[32], grideye[33], grideye[34], grideye[35],\
        grideye[36], grideye[37], grideye[38], grideye[39], grideye[40], grideye[41], grideye[42], grideye[43], grideye[44], grideye[45], grideye[46],\
        grideye[47], grideye[48], grideye[49], grideye[50], grideye[51], grideye[52], grideye[53], grideye[54], grideye[55], grideye[56], grideye[57],\
        grideye[58], grideye[59], grideye[60], grideye[61], grideye[62], grideye[63], CO2, temp, humid))
        conn.commit

while 1:
        reading1()
        time.sleep(2)
        







