hd = 10
hdb = 8
peoples = float(input('enter the number of peoples enter the party:'))
hd_each = float(input('how much hot dog for each persons' + str(peoples) + 'is: '))

hd_req = peoples * hd_each
print('number of hot dog required in party is:', hd_req)
hd_bun_req = hd_req
print('number of hot bog buns required in the party is:', hd_bun_req)

min_pack_hd = hd_req / hd
print('minimum hot dog packages required is:', min_pack_hd)
min_pac_hd_bun = hd_bun_req // hdb + 1
print('minimum hot dog bun packages required is:', min_pac_hd_bun)

hd_left_over = min_pack_hd * hd
min2 = hd_left_over - hd_bun_req
print('hot dog left over is:', min2)
hd_buns_left_over = min_pac_hd_bun * hdb
min1 = hd_buns_left_over - hd_left_over
print('hot dog buns left over is:', min1)
