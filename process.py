#!/usr/bin/env python3

import os

def list_files():
    return [f for f in os.listdir('.') if f.endswith('-processed.txt')]

def avg_throughput():
    files = list_files()
    avg_thr = []
    for file in files:
        result = 0
        avg = 0
        sum = 0
        f = open(file, "r")
        lines = f.readlines()
        for line in lines:
            sum += float(line.split(' ')[0])
        avg = sum/30    
        result = round(avg, 3)
        avg_thr.append(result)
        f.close()
    return avg_thr

def avg_jitter():
    files = list_files()
    avg_jtr = []
    for file in files:
        result = 0
        avg = 0
        sum = 0
        f = open(file, "r")
        lines = f.readlines()
        for line in lines:
            sum += float(line.split(' ')[1])
        avg = sum/30    
        result = round(avg, 3)
        avg_jtr.append(result)
        f.close()
    return avg_jtr

def avg_packet_loss():
    files = list_files()
    avg_pls = []
    for file in files:
        result = 0
        percentage = 0
        total_lost = 0
        total_datagram = 0
        f = open(file, "r")
        lines = f.readlines()
        for line in lines:
            lost_packets = line.split(' ')[2].split('/')[0]
            datagram = line.split(' ')[2].split('/')[1]
            total_lost += float(lost_packets)
            total_datagram += float(datagram)
        percentage = (total_lost/total_datagram) * 100
        result = round(percentage, 3)
        avg_pls.append(result)
        f.close()
    return avg_pls

def avg_delay():
    files = list_files()
    avg_dly = []
    for file in files:
        result = 0
        delay = 0
        total_datagram = 0
        f = open(file, "r")
        lines = f.readlines()
        for line in lines:
            datagram = line.split(' ')[2].split('/')[1]
            total_datagram += float(datagram)
        delay = 30/total_datagram
        result = round(delay, 3)
        avg_dly.append(result)
        f.close()
    return avg_dly

def write_file(filename, lines):
    f = open(filename, "w")
    for line in lines:
        f.write(str(line))
        f.write('\n')
        f.close

avg_throughput = avg_throughput()
avg_jitter = avg_jitter()
avg_packet_loss = avg_packet_loss()
avg_delay = avg_delay()
print(f'Average Throughput: {avg_throughput} \n')
print(f'Average Jitter: {avg_jitter} \n')
print(f'Average Packet Loss: {avg_packet_loss} \n')
print(f'Average Delay: {avg_delay} \n')
write_file('average-throughput.txt', avg_throughput)
write_file('average-jitter.txt', avg_jitter)
write_file('average-packet-loss.txt', avg_packet_loss)
write_file('average-delay.txt', avg_delay)
