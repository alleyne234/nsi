import copy

l1_ = [["Emma",2007],["Tom", 2009] ,["Maxence", 2005]]
l2_ = copy.copy(l1_)
l3_ = copy.deepcopy(l1_)
l1_[0][0]= "Jean"
print(l1_,l2_,l3_)
