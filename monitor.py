#!/usr/bin/env python3

import importlib
import argparse
import os
import pymysql
import threading
import json


am = importlib.import_module('apply-model')
rs = importlib.import_module('record-stream')


def load_tags():
    return ["Raúl Vargas", 'Mónica Delta', 'Helmer Huerta', 'Guillermo Rossinni', 'Patricia del Rio', 'Otro']


def load_stations(f_name):
    if not os.path.exists(f_name):
        print('Stations json file does not exist.')
        exit(1)

    with open(f_name) as f:
        return json.loads(f.read())


def load_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--stations', '-st', type=str, help='Json file with stations list', default='stations.json')
    parser.add_argument('--interval', '-i', type=int, help='Seconds', default=2)
    parser.add_argument('--model_dir', '-md', type=str, help='Model directory', default='./model')

    parser.add_argument('--db_host', type=str, default='127.0.0.1', help='Host of the mysql')
    parser.add_argument('--db_user', type=str, default='root', help='User of mysql')
    parser.add_argument('--db_name', type=str, default='ia', help='Db name')
    parser.add_argument('--db_pass', type=str, default='hola123', help='Password of the user')
    return parser.parse_args()


def save_event(args, station, tags, c):
    conn = pymysql.connect(host=args.db_host, user=args.db_user, password=args.db_pass,
                           db=args.db_name, cursorclass=pymysql.cursors.DictCursor)

    with conn.cursor() as cursor:
        sql = '''insert into `events` values(0, '{st}', '{desc}', now())'''
        cursor.execute(sql.format(st=station, desc=tags[c]))

    conn.commit()
    conn.close()


def main(args):
    tags = load_tags()
    stations = load_stations(args.stations)

    am.load_model(args.model_dir)

    stop_rec = threading.Event()
    while True:
        tmp_file = rs.record_interval(stop_rec, stations[0]['endpoint'], '/tmp', stations[0]['name'], 2)
        c = am.classify(tmp_file)
        if c != 5:
            save_event(args, stations[0]['name'], tags, c)
        print(tags[c], 'detected.')
        os.remove(tmp_file)


if __name__ == "__main__":
    args = load_args()
    main(args)
