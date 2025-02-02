def spy_game(nums):
    count=0
    for i in range(0,len(nums)):
    
        if nums[i]==0:
            count+=1
        if count>=2 and nums[i]==7:
            print("True")
            break
mylist=[1,2,4,0,0,7,5] 
spy_game(mylist)
