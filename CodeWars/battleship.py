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

bad_field = [   [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def validate_battlefield(field):
    
    # Will track the identified ships.
    inventory = []
    
    # The total number of ships we are expecting.
    total_ships = 4 * 1 + 3 * 2 + 2 * 3 + 4 * 1
    
    # Flattens nested lists.
    def flatten(nest):
        return [j for i in nest for j in i]

    # Sums the total number of ships on the starting field.
    def battlefield_sum(field):
        return sum(j for i in field for j in i)

    # Check to see if the field has more or less ships than
    # the required twenty. 
    if battlefield_sum(field) != total_ships:
        return False

    # Looping through each row in the field.
    for i, row in enumerate(field):
        
        # Looping through each position in the row.
        for j, pos in enumerate(row):
            
            # If pos equals 1 then we have identified a ship.
            if pos==1:
            
                # Here we look for the largest possible ship in 
                # both the horizontal and vertical positions.
                # In this case, the largest ship is of size 4.

                horz = field[i][j:j+4]
                vert = [n[j] for n in field[i:i+4]]

                # These are place holders to properly identify the
                # ship size. Since there can be multiple ships in the
                # horz or vert variable, i.e., [1,1,0,1] could be two ships,
                # We will loop through each array until we hit 0. This will 
                # be the 'true' size of the ship.

                hlist = []
                vlist = []
                
                # Identifying the 'true' size of the horz ship.
                for h in horz:
                    if h==0:
                        break
                    hlist.append(h)
                
                # Identifying the 'true' size of the vert ship.
                for v in vert:
                    if v==0:
                        break
                    vlist.append(v)
                
                # Checking the surroundings.
                # Each ship must be surrounded by zeros, unless 
                # the ship is on the edge. In which case, it must
                # be surrounded by zeroes on the non-edge side.

                #single ship case

                if sum(vlist) == sum(hlist) == 1:
                    
                    # Adding identified ship to the inventory.
                    inventory.append([1])
                    
                    # Here, we change the ship to 0's because we
                    # will verify our ship is surrounded by 0's
                    # by summing the surroundings and the actual
                    # ship position. If the sum is 0, then we know
                    # that there are no other ships that are in 
                    # contact.
                    field[i][j] = 0

                    # check surroundings for all zeroes
                    temp = []
                    # The if statement checks to see if i, the row, is on an
                    # edge. If so then we only care about the 0's on the non-edge
                    # side.
                    for r in field[i if i==0 else i-1 : i+1 if i==0 else i+2]:
                        temp.append(r[j if j==0 else j-1 : j+2 if j==0 else j+1])
                    
                    # If the sum is 0 we know that there are no other ships making
                    # contact.
                    if sum(flatten(temp)):
                        return False
                    
                    

                # vlist...
                # here we can identify which ship takes precedence by its length.
                # The longer ship always wins.
                elif sum(vlist) > sum(hlist):
                    inventory.append(vlist)
                    for n in field[i:i+len(vlist)]:
                        n[j] = 0      

                    # check surroundings for all zeroes...see above notes for single ship.
                    temp = []
                    for r in field[i if i==0 else i-1 : i+len(vlist)+1 if i==0 else i+len(vlist)+1]:
                        temp.append(r[j if j==0 else j-1 : j+1 if j==0 else j+2])
                    
                    if sum(flatten(temp)):
                       return False

                    

                # hlist
                # see above comments for single ship and vlist.
                else:
                    inventory.append(hlist)
                    for n in range(j, j+len(hlist)):
                        if n<=9:
                            field[i][n] = 0
                    
                    # check surroundings for all zeroes
                    temp = []
                    for r in field[i if i==0 else i-1 : i+2 if i==0 else i+2]:
                        temp.append(r[j if j==0 else j-1 : j+len(hlist)+0 if j==0 else j+len(hlist)+1])

                    if sum(flatten(temp)):
                       return False 

    # Used to store the lengths of the ships.    
    ship_count = []

    for ship in inventory:
        ship_count.append(len(ship))

    # The number of ships we expect. We expect 10.
    ship_check = sorted([1,1,1,1,2,2,2,3,3,4])
    
    # The number of 1's on the board. We expect 20.
    final_count = sum(j for i in inventory for j in i)
    
    # Check to see if the ships found on the board equal the ships we expected to see.
    verify_ships = ship_check == sorted(ship_count)

    # Check to see if the total count of 1's on the board is equal to 20. 
    verify_ship_count = final_count == 20
                
    return verify_ships == verify_ship_count


print(validate_battlefield(bad_field))
# print(validate_battlefield(battleField))