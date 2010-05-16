

#  and_or.py  


def andp(iter1, iter2): 
   if iter1 == iter2: 
      return iter2
   else: 
      return "Failed parse" 
      
def orp(iter1, iter2): 
   count = 0 
   retval = []
   for x in iter2: 
     if x in iter1: 
        count += 1
        retval.append(x)
     else: 
        pass 
   return retval 
   
   
print andp(["just", "a", "small", "test"], ["just", "a", "small", "test"]) 

print orp(["just", "a", "small", "test"], ["just", "test"]) 
     
   
        
                 


