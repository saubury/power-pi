from gpiozero import LightSensor, Buzzer
from signal import pause
import time
import sys
import Adafruit_DHT
import schedule
import argparse
import sqlite3

DATABASE = '/share/power-pi/database/power-sqlite.db'

l_temp_sensor_type = Adafruit_DHT.DHT22
l_gpio_ldr_1 = 4
l_gpio_ldr_2 = 23
l_gpio_temp = 22
l_cnt_1 = 0
l_cnt_2 = 0
l_out_file = "/share/power-pi/power-pi.txt"
l_poll_minutes = 5
l_hr_rate_multiply = (60 / l_poll_minutes)
l_verbosemode = False


def insert_row(measurement):
    sql = '''INSERT INTO measure_history (temperature, humidity, sensor_count_1, sensor_count_2) VALUES (?,?,?,?)'''
    conn = sqlite3.connect(DATABASE)
    with conn:
        cur = conn.cursor()
        cur.execute(sql, measurement)
    conn.close()

def do_purge():
    open(l_out_file, 'w')
    sql = '''delete from measure_history '''
    conn = sqlite3.connect(DATABASE)
    with conn:
        cur = conn.cursor()
        cur.execute(sql)
    conn.close()
    exit(0)

def logmsg(msg):
    msg_text = "{} {}".format(time.strftime("%d/%m/%Y %H:%M:%S"), msg)
    print(msg_text)
    with open(l_out_file,'a') as f:
        f.write("{}\n".format(msg_text))

def light_pulse_seen_1():
    global l_cnt_1
    global l_verbosemode
    l_cnt_1 = l_cnt_1 + 1
    if l_verbosemode:
        logmsg("      light_pulse_seen_1 {}".format(l_cnt_1))

def light_pulse_seen_2():
    global l_cnt_2
    global l_verbosemode
    l_cnt_2 = l_cnt_2 + 1
    if l_verbosemode:
        logmsg("      light_pulse_seen_2 {}".format(l_cnt_2))
        
def handle_time_event():
    global l_cnt_1
    global l_cnt_2
    l_humidity, l_temperature = Adafruit_DHT.read_retry(l_temp_sensor_type, l_gpio_temp)
    logmsg("Pulses={},{} Temp={:0.1f}C  l_humidity={:0.1f}%".format(l_cnt_1, l_cnt_2, l_temperature, l_humidity))
    measurement = (l_temperature, l_humidity, l_cnt_1, l_cnt_2)
    insert_row(measurement)
    l_cnt_1 = 0
    l_cnt_2 = 0

def main():
    global l_verbosemode
    parser = argparse.ArgumentParser(description='Power and temp monitor.')
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("-p", "--purge", help="purge file and database", action="store_true")
    args = parser.parse_args()

    if (args.purge):
        do_purge()

    l_verbosemode = args.verbose

    ldr_1 = LightSensor(l_gpio_ldr_1)  
    ldr_2 = LightSensor(l_gpio_ldr_2)  
    ldr_1.when_light = light_pulse_seen_1
    ldr_2.when_light = light_pulse_seen_2
    handle_time_event()
    schedule.every(l_poll_minutes).minutes.do(handle_time_event)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
