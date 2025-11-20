numbers=[10,5,10,8,15,20,5]

unique_nums=list(set(numbers)) #remove duplicates

unique_nums.sort()

second_min=unique_nums[1]
second_max=unique_nums[-2]
print("second minimum:",second_min)
print("Second maxmum",second_max)
