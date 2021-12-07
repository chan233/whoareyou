
file = open('access.log','r')
lines = file.readlines()
accepteds = list()
rejecteds = list()
for line in lines:
    value = line.split()
    if value[3] == 'accepted':
        map = {
            "date":value[0],
            "time":value[1],
            "src":value[2],
            "status":value[3],
            "dst":value[4],
            "protocl":value[5],
            "type":value[6],
            "tag":value[7]
            }
        accepteds.append(map)
    elif value[3] == 'rejected':
        map = {
            "date":value[0],
            "time":value[1],
            "src":value[2].split(':')[0],
            "status":value[3],
            "error_msg":line.split('  ')[1]     
            }
        rejecteds.append(map)
file.close()

for l in rejecteds:
    print('ipfrom ==>'+l["src"])
    print('problem ==>'+l["error_msg"])




