def batao(n):
	if(n%2!=0):
    	return 1
	else:
    	if(n%2==0):
        	if(n in range(2,5)):
            	return 0
        	else:
            	if(n in range(6,20)):
                	return 1
            	else:
                	return 0
            	
n=int(input())            	
if(batao(n)==1):
	print("Weird")
else:
	print("Not Wierd")
