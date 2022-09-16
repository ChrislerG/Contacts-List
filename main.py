contacts_name = ['Cristina','Izabelle','Jenny','Jack'] 

contacts_number = ['617-770-5481','617-000-6789','617-495-9990','617-770-5481']  



print('Press 1 to Search By Name or Press 2 to Search By Phone Number') 
answer = input()  


if answer == '1': 
  print('Search by name') 
  name_search = input()  
  if name_search in contacts_name: 
   position = contacts_name.index(name_search) 
   print(contacts_number[position])
  else: 
    print('Couldnt find this contact.')  
    print('Create a new contact:') 
    new_contact = input() 
    print('Enter the contacts number') 
    new_number = input() 
    contacts_name.append(new_contact) 
    contacts_number.append(new_number) 
    print(contacts_name) 
    print(contacts_number)

elif answer == '2': 
  print('Search by number') 
  number_search = input()  
  if number_search in contacts_number: 
    position = contacts_number.index(number_search)  
    print(contacts_name[position])

  else: 
    print('You do not have this number saved. Please search by name instead.') 

else: 
  print('Sorry, I do not understand. Please try again.')






