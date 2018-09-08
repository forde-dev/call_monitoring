# Imports
import serial
import pymysql as db
from datetime import date

# serial connector, ttyUSB0 is the default on linux
ser = serial.Serial('/dev/ttyUSB0', 9600)

# this is the id of the user
user = 'user'
# this is the id of the system that this is hooked up to
system_id = '000000000'

# init thr variables
logs = []
number = ''
incoming_call = ''
ext = ''
ring = ''
duration = ''
answered = ''
call_type = ''
ddi = ''

# while to log each call
try:
    while 1:
        # this reads the raw serial input
        serial_line = ser.readline()
        # this decodes the raw input to ASCII
        serial_line = serial_line.decode("ASCII")
        # names the input as logs
        logs = serial_line.split()

        #print(serial_line)
        print(logs)


        call_date_time = logs[0]

        call_date_raw = call_date_time[:8]
        call_time = call_date_time[8:]

        call_date = str(date.today())

        line = logs[1]

        call_range = ['0', '1', '2']

        if logs[3] in call_range:
            call = logs[3]
        else:
            call = logs[4]

        if call == '0':
            call_type = 'incoming'
            ext = logs[2]
            incoming_call = logs[3]
            ddi = logs[5]
            print('Incoming number:', incoming_call, ' ext:', ext)

        elif call == '1':
            call_type = 'end'
            call_data = logs[2]
            ext = call_data[:3]
            ring = call_data[3:8]
            duration = call_data[8:16]
            number = call_data[16:]
            ddi = logs[4]

            if duration == '00:00:00':
                answered = 'no'
            else:
                answered = 'yes'

            print('number called:', number, ' ext:', ext, ' ring:', ring, ' duration', duration, ' answered:',
                  answered)


        elif call == '2':
            call_type = 'outgoing'
            call_data = logs[2]
            ext = call_data[:3]
            ring_length = call_data[3:8]
            duration = call_data[8:16]
            number = call_data[16:]

            if duration == '00:00:00':
                answered = 'no'
            else:
                answered = 'yes'

            print('number called:', number, ' ext:', ext, ' ring:', ring, ' duration', duration, ' answered:',
                  answered)
        # connect to database and add calls
        try:
            connection = db.connect(host='localhost', user='root', passwd='password', db='call_monitoring')
            cursor = connection.cursor()
            if call_type == 'incoming':
                cursor.execute("""
                INSERT INTO call_incoming(system_id, user, call_date, time, line, incoming_num, ext, ddi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (system_id, user, call_date, call_time, line, incoming_call, ext, ddi))
                connection.commit()
            elif call_type == 'end':
                cursor.execute("""
                INSERT INTO call_logs(system_id, user, call_date, time, line, answered, number, ring, duration, ext, ddi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (system_id, user, call_date, call_time, line, answered, number, ring, duration, ext, ddi))
                connection.commit()
            elif call_type == 'outgoing':
                cursor.execute("""
                INSERT INTO call_outgoing(system_id, user, call_date, time, line, answered, number, ext) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (system_id, user, call_date, call_time, line, answered, number, ext))
                connection.commit()

            cursor.close()
            connection.close()
            print('Successfully added to database.')
        except db.Error:
            print('Sorry! We are experiencing problems at the moment.')

        logs = []
except KeyboardInterrupt:
    print('finished')
