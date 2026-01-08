import pytest
def account_details(acc_number,holder_name, acc_type, balance, ):
    result = (
        f"Account_Number:{acc_number}\n"
        f"Holder_Name:{holder_name}\n"
        f"Account_Type:{acc_type}\n"
        f"Balance:{balance}\n"
       
    )
    return result

if __name__ == "__main__":
    acc_number="123456789"
    holder_name="Vaishnavi"
    acc_type="Savings"
    balance=1000.50
    print(account_details(acc_number, holder_name, acc_type, balance))