def work_with_phonebook():
    choice = show_menu()

phone_book = read_txt('phonebook.txt')

while (choice!=7):
    if choice==1:
        print_result(phone_book)
    elif choice==2:
last_name=input('lastname ')
print(find_by_lastname(phone_book,last_name))
elif choice==3:
last_name=input('lastname ')
new_number=input('new number ')
print(change_number(phone_book,last_name,new_number))
elif choice==4:
lastname=input('lastname ')
print(delete_by_lastname(phone_book,lastname))
elif choice==5:
number=input('number ')
print(find_by_number(phone_book,number))
elif choice==6:
user_data=input('new data ')
add_user(phone_book,user_data)
write_txt('phonebook.txt',phone_book)


choice=show_menu()