# [1,2,3,4,5,5]

#  0 1 2 3 4
# [1,2,3,4,3]
# a[1] = -2 , i = 0, val 1 index , refval = -2 -a[abs(a[i])]
# a[2] = -3 , i = 1 , val 2  index , refval = -3
# a[3] = -4 , i = 2, val 3 index, refval = -4
# a[4] = -3  , i = 3, val 4 index, refval = -3
# a[4]       , i = 4 , val 3 index, refval = -4


# a[abs(a[i])] = -a[abs(a[i])]

idea here is to look for a key (which is actually an array item) that
previously modified an item (making the item negative)