__author__ = 'Bob'
bronze=100
silver=100

def price_checker():
    pass

def gold_only(price):
    return(int(round(price/(bronze*silver),2)))


def bargain_hunter(sell_server_hi, sell_server_lo, buy_server, cheap_server, exp_server):
	bargains = []
	for auction in sell_server_lo:
		if auction in buy_server:
			if buy_server[auction] < sell_server_lo[auction]:
				sell_cost = sell_server_lo[auction]
				buy_cost = buy_server[auction]
				low_profit = (sell_server_lo[auction] - buy_server[auction])
				high_profit = (sell_server_hi[auction] - buy_server[auction])
				line = (' \nPossible bargain: ' + auction + ' on ' + str(cheap_server) + ' costs ' + str(
					buy_cost) + ' and on ' + str(exp_server) + ' costs at least ' + str(
					sell_cost) + ' \n...a potential profit of between ' + str(low_profit) + ' up to possibly ' + str(
					high_profit) + ' \n' + '*' * 20)
				bargains.append(line)
	return (bargains)
