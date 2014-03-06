#-*- coding: utf-8 -*-

from pymongo import MongoClient

def get_db_info(host):
    client = MongoClient(host)
    #client = MongoClient('192.168.1.123')
    d = client.database_names()
    for i in xrange(len(d)):
        print str(i) + '. ' + d[i]

    num = raw_input('Choose the database number: ')
    db = client[d[int(num)]]
    collections = db.collection_names(include_system_collections=False)
    db_list = []
    for c in collections:
        print c
        connection = db[c]
        try:
            r = connection.find_one()
            if r['_id'] == 0:
                r = connection.find_one({'_id': {'$gt': 1}})
        except:
            pass
        db_list.append({'col_name': c, 'col_info': r})

    return db_list


def show_info(db_list):
    for l in db_list:
        if not l['col_info']:
            continue
        print ">==>", l['col_name']
        print " "*4 + "|"
        col_info = l['col_info']
        for key, value in col_info.iteritems():
            print " "*4 + "|==>  " + str(key)
        print ("-*-"*12 + "\n")*2

def main():
    host = raw_input('MongDB host: ')
    db_list = get_db_info(host)
    show_info(db_list)

if __name__ == "__main__":
    main()
