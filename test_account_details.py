from account_details import account_details
def account_details():
    output=(
        "Account number: 123456789\n"
        "Account holder: vaishnavi\n"
        "Account type: savings\n"
        "Balance: 55000"
    )
    assert account_details("123456789","vaishnavi" "savings", 55000) == output
