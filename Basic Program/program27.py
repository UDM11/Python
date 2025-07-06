def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

districts = ("sindhuli","ramechaap","kathmandu","bhaktapur")
print_list(districts)