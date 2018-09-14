from django.shortcuts import render
from django.http import JsonResponse
import pymysql as db
from datetime import date, datetime, timedelta
import time

def index(request):

    incoming_result = []
    log_result = []
    outgoing_result = []
    missed = ''
    all_calls = ''
    voice_mail = ''

    try:
        connection = db.connect('localhost', 'root', 'fordemc2', 'call_monitoring')
        cursor = connection.cursor(db.cursors.DictCursor)

        cursor.execute("""SELECT * FROM call_incoming ORDER BY call_date DESC, time DESC""")

        for row in cursor.fetchall():
            incoming_result.append("""
                    <tr>
                      <td>%s</td>
                      <td>%s</td>
                      <td>%s</td>
                      <td>%s</td>
                      <td>%s</td>
                    </tr>
                    """ % (row['incoming_num'], row['ext'], row['line'], row['call_date'], row['time']))


        cursor.execute("""SELECT * FROM call_logs ORDER BY call_date DESC, time DESC""")

        for row in cursor.fetchall():
            log_result.append("""
                    <tr>
                      <td>%s</td>
                      <td>%s</td>
                      <td>%s</td>
                      <td>%s</td>
                      <td>%s</td>
                      <td>%s</td>
                      <td>%s</td>
                    </tr>
                    """ % (row['number'], row['ext'], row['answered'], row['ring'], row['duration'], row['call_date'], row['time']))

        cursor.execute("""SELECT count(*) FROM call_logs WHERE answered = 'no'""")

        missed = cursor.fetchone()
        missed = str(missed['count(*)'])

        today_date = str(date.today())

        cursor.execute("""SELECT count(*) FROM call_logs WHERE call_date = %s""", today_date)

        all_calls = cursor.fetchone()
        all_calls = str(all_calls['count(*)'])

        cursor.execute("""SELECT count(*) FROM call_incoming WHERE ext = '200'""")

        voice_mail_f = cursor.fetchone()
        voice_mail = str(voice_mail_f['count(*)'])

        cursor.close()
        connection.close()
    except db.Error:
        incoming_result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'
        log_result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'
        outgoing_result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'


    data = {'incoming': incoming_result, 'logs': log_result, 'outgoing': outgoing_result, 'missed': missed, 'all_calls': all_calls, 'voice_mail': voice_mail}

    return render(request, 'index.html', data)

#        #
#        #
## Pages ##
#        #
#        #

def missed_calls(request):
    return render(request, 'missed_calls.html')


def today_calls(request):
    return render(request, 'today_calls.html')


def current_calls(request):
    return render(request, 'current_calls.html')

def voicemail_calls(request):
    return render(request, 'voicemail_calls.html')

def outgoing_calls(request):
    return render(request, 'outgoing_calls.html')

def callreports(request):
    return render(request, 'callreports.html')

#        #
#        #
## AJAX ##
#        #
#        #


def ajax_incoming(request):
    result = []
    try:
        connection = db.connect('localhost', 'root', 'fordemc2', 'call_monitoring')
        cursor = connection.cursor(db.cursors.DictCursor)

        cursor.execute("""SELECT * FROM call_incoming ORDER BY call_date DESC, time DESC""")

        for row in cursor.fetchall():
            result.append([row['incoming_num'], row['ext'], row['line'], row['call_date'], row['time']])

    except db.Error:
        result = []

    data = {
        "data" : result
    }
    return JsonResponse(data)

def ajax_logs(request):
    result = []
    try:
        connection = db.connect('localhost', 'root', 'fordemc2', 'call_monitoring')
        cursor = connection.cursor(db.cursors.DictCursor)

        cursor.execute("""SELECT * FROM call_logs ORDER BY call_date DESC, time DESC""")

        for row in cursor.fetchall():
            result.append([row['number'], row['ext'], row['answered'], row['ring'], row['duration'], row['call_date'], row['time']])

    except db.Error:
        result = []

    data = {
        "data" : result
    }
    return JsonResponse(data)

def ajax_missed(request):
    result = []
    try:
        connection = db.connect('localhost', 'root', 'fordemc2', 'call_monitoring')
        cursor = connection.cursor(db.cursors.DictCursor)

        cursor.execute("""SELECT * FROM call_logs WHERE answered = 'no' ORDER BY call_date DESC, time DESC""")

        for row in cursor.fetchall():
            result.append([row['number'], row['ext'], row['answered'], row['ring'], row['duration'], row['call_date'], row['time']])

    except db.Error:
        result = []

    data = {
        "data" : result
    }
    return JsonResponse(data)

def ajax_today(request):
    result = []
    try:
        connection = db.connect('localhost', 'root', 'fordemc2', 'call_monitoring')
        cursor = connection.cursor(db.cursors.DictCursor)

        today_date = str(date.today())

        cursor.execute("""SELECT * FROM call_logs WHERE call_date = %s ORDER BY call_date DESC, time DESC""", today_date)

        for row in cursor.fetchall():
            result.append([row['number'], row['ext'], row['answered'], row['ring'], row['duration'], row['call_date'], row['time']])

    except db.Error:
        result = []

    data = {
        "data" : result
    }
    return JsonResponse(data)

def ajax_current(request):
    result = []
    try:
        connection = db.connect('localhost', 'root', 'fordemc2', 'call_monitoring')
        cursor = connection.cursor(db.cursors.DictCursor)

        today_date = str(date.today())
        now_time = str(datetime.now() - timedelta(minutes=2))
        time = now_time[:6]
        cursor.execute("""SELECT incoming_num FROM call_incoming WHERE incoming_num not = (SELECT number FROM call_logs WHERE time > %s AND call_date = %s ) ORDER BY call_date DESC, time DESC""", (time ,today_date))

        for row in cursor.fetchall():
            result.append([row['incoming_num'], row['ext'], row['line'], row['call_date'], row['time']])

    except db.Error:
        result = []

    data = {
        "data" : result
    }
    return JsonResponse(data)

def ajax_voicemail(request):
    result = []
    try:
        connection = db.connect('localhost', 'root', 'fordemc2', 'call_monitoring')
        cursor = connection.cursor(db.cursors.DictCursor)

        today_date = str(date.today())

        cursor.execute("""SELECT * FROM call_logs WHERE ext = '200' ORDER BY call_date DESC, time DESC""")

        for row in cursor.fetchall():
            result.append([row['number'], row['ext'], row['answered'], row['ring'], row['duration'], row['call_date'], row['time']])

    except db.Error:
        result = []

    data = {
        "data" : result
    }
    return JsonResponse(data)

def ajax_outgoing(request):
    result = []
    try:
        connection = db.connect('localhost', 'root', 'fordemc2', 'call_monitoring')
        cursor = connection.cursor(db.cursors.DictCursor)


        cursor.execute("""SELECT * FROM call_outgoing ORDER BY call_date DESC, time DESC""")

        for row in cursor.fetchall():
            result.append([row['number'], row['ext'], row['answered'], row['call_date'], row['time']])

    except db.Error:
        result = []

    data = {
        "data" : result
    }
    return JsonResponse(data)
