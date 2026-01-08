
def account_details(acc_number,holder_name,acc_type,balance):
    result = (
        f"acc_number:{acc_number}\n"
        f"holder_name:{holder_name}\n"
        f"acc_type:{acc_type}\n"
        f"balance:{balance}\n"
       
    )
    return result

if __name__ == "__main__":
    acc_number="123456789"
    holder_name="Vaishnavi"
    acc_type="Savings"
    balance=1000.50
    print(account_details(acc_number,holder_name,acc_type,balance))
