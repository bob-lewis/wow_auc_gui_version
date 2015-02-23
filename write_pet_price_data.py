__author__ = 'Bob'

import json,httplib2,os
from get_pet_price_data import gold_only

PET_QUALITY = [ 'Poor', 'Common', 'Uncommon', 'Rare', 'Epic', 'Legendary','unknown']
def pet_checker():
    pass

def pet_quality(grade):
    return PET_QUALITY[grade]

def petid_get_new(id):
    request = str('http://eu.battle.net/api/wow/battlePet/species/' + id)
    h = httplib2.Http(".cache",timeout = 60)
    content_headers, content = h.request(request)
    content = content.decode()
    obj = json.loads(content)

    if 'creatureId' in obj:

        return (obj['name'])
    else:
        return 'unknown pet'


def pet_auction_get(auc_api):
    auc_list = []
    print('Calculating ,please wait')
    h = httplib2.Http(".cache", timeout = 60)
    content_headers, content = h.request(auc_api,"GET")
    content = content.decode()
    obj = json.loads(content)
    print('got json object')
    x=( obj['auctions'])
    y=x['auctions']
    for i in y:
        if  (i['item'])==82800:
            print('found pet number '+ str(len(auc_list)),end='\r')
            temp_list=[]
            temp_list.append(i['owner'])
            temp_list.append(i['ownerRealm'])
            temp_list.append(gold_only(i['buyout']))
            check=str(i['petSpeciesId'])
            id = petid_get_new(check)
            x=int((i['petQualityId']))
            quality = PET_QUALITY[x]
            petname = str(id + ' of ' + quality + ' quality.')
            temp_list.append(petname)
            temp_list.append(i['petBreedId'])
            #print(temp_list)
            auc_list.append(temp_list)
    print('list complete')
    return auc_list

def write_to_master(auc_list):
	with open('temp.txt', 'a') as master:
		for line in auc_list:
			master.write(str(line))
	print('details written to bargains.txt')

def clean_up():
	try:
		os.remove("bargains.txt")
	except:
		os.rename("temp.txt", "bargains.txt ")
	os.rename("temp.txt", "bargains.txt ")

