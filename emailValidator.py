import MailboxValidator
from decouple import config
import os

API_KEY = config('KEY')
mbv = MailboxValidator.EmailValidation(API_KEY)


def single():
    email = input('Please enter an email address:')
    results = mbv.validate_email(email)
    if results is None:
        os.system('cls||clear')
        print("Error connecting to API.")
    elif results['error_code'] == '':
        if float(results['mailboxvalidator_score']) > 0.5 and results['is_verified'] == 'True' and results['status'] == 'True':
            print(f'{email} is a valid email')
    else:
        print(results['error_code'])
        print(results['error_message'])


def bulk():
    file = input('Please enter the name of the file:')
    print('Please wait...')
    with open(file, 'r') as f:
        for line in f:
            results = mbv.validate_email(line)
            if results is None:
                os.system('cls||clear')
                print("Error connecting to API.")
            elif results['error_code'] == '':
                if float(results['mailboxvalidator_score']) > 0.5 and results['is_verified'] == 'True' and results['status'] == 'True':
                    with open('valid_emails.txt', 'a') as f:
                        f.write(line)
                else:
                    with open('invalid_emails.txt', 'a') as f:
                        f.write(line)
            else:
                print(results['error_code'])
                print(results['error_message'])
                with open('invalid_emails.txt', 'a') as f:
                    f.write(line)
    print('Done!')


def menu():
    print('Do you wish to check a single email address or a file with a list of email addresses?')
    print('1. Single email address')
    print('2. File with list of email addresses')
    answer = input('Please enter 1 or 2:')
    return answer


def main():
    answer = menu()

    if answer == '1':
        os.system('cls||clear')
        single()
        print('\nDo you wish to check another email address?')
        print('1. Yes')
        print('2. No')
        answer = input('Please enter Y or N:')
        if answer == 'Y':
            main()
        else:
            print('Goodbye!')

    if answer == '2':
        os.system('cls||clear')
        bulk()
        print('\nDo you wish to check another email address?')
        print('1. Yes')
        print('2. No')
        answer = input('Please enter Y or N:')
        if answer == 'Y':
            main()
        else:
            print('Goodbye!')


main()
