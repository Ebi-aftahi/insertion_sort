def insertion_sort(my_list):
	#i is index of sorted sublist
	for i in range(1, len(my_list)):
		#print(f"mylist in i={i}", mylist)
		temp = my_list[i]
		my_list.pop(i)
		j = i-1
		while(j >= 0 and temp < my_list[j]):
			j -= 1
		my_list.insert(j + 1, temp)
		

			
mylist = [1, 8, 6, 8, 6, 5, 0, 2, -1, 2, 3, 10, 7]
print(mylist)
insertion_sort(mylist)
print(mylist)
			

