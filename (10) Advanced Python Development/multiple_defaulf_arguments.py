# AVOID THIS

def create_account(name: str, holder: str, account_holders: list = []):
    account_holders.append(holder)

    return{
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders
    }

a1 = create_account('checking', 'Rolf')
a2 = create_account('savings', 'Jen')

print(a2)

# Solution:

def _create_account(name: str, holder: str, account_holders = None):
    if not account_holders:
        account_holders = []
    
    account_holders.append(holder)

    return{
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders
    }

a1 = _create_account('checking', 'Rolf')
a2 = _create_account('savings', 'Jen')

print(a2)
