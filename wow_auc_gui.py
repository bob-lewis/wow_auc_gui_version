__author__ = 'Bob'
from get_pet_price_data import *
from get_realm_data import *
from write_pet_price_data import *
from realm_list import update_realm_list

import random,os
server1_complete = False
server2_complete = False
r1_hi = {}
r1_lo = {}
r2_hi = {}
r2_lo = {}
realm_list=list(update_realm_list())
selection=random.randrange(0,(len(realm_list)),1)

def generate_testrealm():
    selection=random.randrange(0,(len(realm_list)),1)
    return realm_list[selection]

def tester():
    server1=generate_testrealm()
    server2=generate_testrealm()
    testprice=127162214
    print('test pet quslity is',pet_quality(3))
    x=str('%s and %s'% (server1,server2))
    print ('two realms being tested  are %s .' % (x))
    print ('test price is %s'% (gold_only(testprice)))
    process_server(server1,1)
    server1_complete=True
    process_server(server2,2)
    server2_complete=True
    compare_prices(server1,server2)


def compare_prices(server1,server2):
    write_to_master(bargain_hunter(r1_hi, r1_lo, r2_lo, server2, server1))
    write_to_master(bargain_hunter(r2_hi, r2_lo, r1_lo, server1, server2))
    clean_up()

def compare_pricess_check(server1,server2):
    if server1_complete and server2_complete:
        compare_prices(server1,server2)

def process_server(server,order):
    api_page= (api_page_get(server))
    print (api_page)
    working_list=list(pet_auction_get(api_page))
    create_pet_auction_lists(working_list,order)

def create_pet_auction_lists(working_list,order):
	if order == 1:
		hi = r1_hi
		lo = r1_lo
	else:
		hi = r2_hi
		lo = r2_lo

	for line in working_list:
		name = str(line[3])
		price = int(line[2])
		if name in hi:
			if price > hi[name]:
				hi[name] = price
			else:
				pass
		else:
			hi[name] = price
		if name in lo:
			if price < lo[name]:
				lo[name] = price
			else:
				pass
		else:
			lo[name] = price


def main():
    tester()
    pet_checker()
    price_checker()

main()