battleField = [  
                 [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
              ]

def validate_battlefield(field):
    
    inventory = []

    total_ships = 4 * 1 + 3 * 2 + 2 * 3 + 4 * 1
    
    def battlefield_sum(field):
        return sum(j for i in field for j in i)

    if battlefield_sum(field) != total_ships:
        return False

    for i, row in enumerate(field):

        for j, pos in enumerate(row):
            
            if pos==1:
            
                horz = field[i][j:j+4]
                vert = [n[j] for n in field[i:i+4]]
                
                hlist = []
                vlist = []
                
                for h in horz:
                    if h==0:
                        break
                    hlist.append(h)
                
                for v in vert:
                    if v==0:
                        break
                    vlist.append(v)
                
                if sum(vlist) == sum(hlist) == 1:
                    inventory.append([1])
                    field[i][j] = 0

                elif sum(vlist) > sum(hlist):
                    inventory.append(vlist)
                    for n in field[i:i+len(vlist)]:
                        n[j] = 0                    
                else:
                    inventory.append(hlist)
                    for n in range(j, j+len(hlist)):
                        if n<=9:
                            field[i][n] = 0

    ship_count = []

    for ship in inventory:
        ship_count.append(len(ship))

    ship_check = sorted([1,1,1,1,2,2,2,3,3,4])
    final_count = sum(j for i in inventory for j in i)
    
    verify_ships = ship_check == sorted(ship_count)
    verify_ship_count = final_count == 20

                
    return verify_ships == verify_ship_count


validate_battlefield(battleField)