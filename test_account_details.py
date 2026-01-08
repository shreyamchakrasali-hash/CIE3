from account_details import account_details
def account_details():
    output=(
        "acc_number:123456789\n"
        "holder_name:vaishnavi\n"
        "acc_type:savings\n"
        "balance:55000"
    )
    assert account_details("123456789","vaishnavi","savings",55000)==output
