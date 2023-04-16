import random,string
def create_new(): 
    with open(file_name,'a') as f:
        web_site=input("Enter website name:")
        user_name=input("Enter user name:")
        length=int(input('Enter the length of password:'))
        if length<=4:
            print('password too weak,choose greater length')
        else:    
            res=string.punctuation+string.ascii_letters+string.digits
            a=random.sample(res, length)
            password=''.join(a)
            f.write(f"Website:{web_site}  User_Name:{user_name}  Password:{password}\n")
            print("Created successfully")
def search():
    with open(file_name) as f:
        search=input('Account to be searched: ')
        read=f.readlines()
        if len(read)>0:
            for i in read:
                value1=i.split("  ")
                if search in value1[1]:
                    for j in value1:
                        print(j)
                else:
                    print("Account not found!")
        else:
             print("File is empty")
        
def delete_acc():
    delete=input('Account name to delete: ')
    with open(file_name) as f:
        reads=f.readlines()
        for i in reads:
            lines=i.split("  ")
            if delete in lines[1]:
                reads.remove(i)
                print("Delected successfull...")
                break
        else:
            print("Account not found!")
    with open(file_name,'w') as f1:
        for i in reads:
            f1.write(i)
        
if __name__=="__main__":
    try:
        while(True):
            file_name="password_manager.txt" 
            choice=input("\tPassword Manager\n1> Create account\n2> Search account\n3> Delete account\n4> Exit\nEnter Choice:")
            if choice == "1":
                create_new()
            elif choice == "2":
                search()
            elif choice == "3":
                delete_acc()
            elif choice == "4":
                exit()
            else:
                print("Enter valid choice!")
    except IOError: 
        print("\nERROR!!!") 