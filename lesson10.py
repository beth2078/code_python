#Telemarketer or Not? 
#String indexing ******

#1. Input
phone = input("Enter the last 4 digits of the phone number: ")

#2. processing
if phone[0] in {'8','9'}:
    #if you have a string, list, or a tuple. We can access the collection's individual items
    # at a certian location, by doing indexing with quare brackets [] ... first item is at location 0.
    if phone[-1] in {'8', '9'}:
        if phone[1] == phone[2]:
            print(f"The phone number with {phone} as it's last fout digits is a telemarketer.")
        else:
            print(f"The phone number with {phone} as it's last fout digits is not a telemarketer.")
    else: 
        print(f"The phone number with {phone} as it's last fout digits is not a telemarketer.")
else:
    print(f"The phone number with {phone} as it's last fout digits is not a telemarketer.")
