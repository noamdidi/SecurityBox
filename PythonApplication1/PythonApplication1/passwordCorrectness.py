import os
import sys
import string

def numbersOnly(passwordStr, passwordLen):
    if passwordLen < 9:
        print("instantly")
    elif passwordLen == 9:
        print("4 sec")
    elif passwordLen == 10:
        print("40 sec")
    elif passwordLen == 11:
        print("6 min")
    elif passwordLen == 12:
        print("1 hour")
    elif passwordLen == 13:
        print("11 hours")
    elif passwordLen == 14:
        print("4 days")
    elif passwordLen == 15:
        print("46 days")
    elif passwordLen == 16:
        print("1 year")
    elif passwordLen == 17:
        print("12 years")
    elif passwordLen == 18:
        print("126 years")

def lowerAndUpper(passwordStr, passwordLen):
    if passwordLen < 6:
        print("instantly")
    elif passwordLen == 6:
        print("8 sec")
    elif passwordLen == 7:
        print("5 min")
    elif passwordLen == 8:
        print("3 hours")
    elif passwordLen == 9:
        print("4 days")
    elif passwordLen == 10:
        print("169 days")
    elif passwordLen == 11:
        print("16 years")
    elif passwordLen == 12:
        print("600 years")
    elif passwordLen == 13:
        print("21K years")
    elif passwordLen == 14:
        print("778K years")
    elif passwordLen == 15:
        print("28M years")
    elif passwordLen == 16:
        print("1B years")
    elif passwordLen == 17:
        print("36B years")
    elif passwordLen == 18:
        print("1TN years")

def lowerAndUpperAndNumber(passwordStr, passwordLen):
    if passwordLen < 5:
        print("instantly")
    elif passwordLen == 5:
        print("10 sec")
    elif passwordLen == 6:
        print("13 min")
    elif passwordLen == 7:
        print("17 hours")
    elif passwordLen == 8:
        print("57 days")
    elif passwordLen == 9:
        print("12 years")
    elif passwordLen == 10:
        print("928 years")
    elif passwordLen == 11:
        print("71K years")
    elif passwordLen == 12:
        print("5M years")
    elif passwordLen == 13:
        print("423M years")
    elif passwordLen == 14:
        print("5B years")
    elif passwordLen == 15:
        print("2TN years")
    elif passwordLen == 16:
        print("193TN years")
    elif passwordLen == 17:
        print("14QD years")
    elif passwordLen == 18:
        print("1QT years")

def lowerAndUpperAndNumberAndSymbol(passwordStr, passwordLen):
    if passwordLen < 5:
        print("instantly")
    elif passwordLen == 5:
        print("3 sec")
    elif passwordLen == 6:
        print("3 min")
    elif passwordLen == 7:
        print("3 hours")
    elif passwordLen == 8:
        print("10 days")
    elif passwordLen == 9:
        print("153 days")
    elif passwordLen == 10:
        print("1 years")
    elif passwordLen == 11:
        print("106 years")
    elif passwordLen == 12:
        print("6K years")
    elif passwordLen == 13:
        print("108K years")
    elif passwordLen == 14:
        print("25M years")
    elif passwordLen == 15:
        print("1B years")
    elif passwordLen == 16:
        print("97B years")
    elif passwordLen == 17:
        print("6TN years")
    elif passwordLen == 18:
        print("374TN years")

def main():
    password = '0505580322'
    passwordLenght = len(password)
    FirstRules = [lambda password: all(x.isupper() for x in password), # must have at least one uppercase
        lambda password: all(x.islower() for x in password) # must have at least one lowercase
        ]
    SecondRules = [lambda password: any(x.isupper() for x in password), # must have at least one uppercase
            lambda password: any(x.islower() for x in password),  # must have at least one lowercase
            lambda password: any(x.isdigit() for x in password) # must have at least one digit
            ]
    ThirdRules = [lambda password: any(x.isupper() for x in password), # must have at least one uppercase
            lambda password: any(x.islower() for x in password),  # must have at least one lowercase
            lambda password: any(x.isdigit() for x in password), # must have at least one digit
            lambda password: any(i in string.punctuation for i in password) # must have at least one symbol
            ]

    if passwordLenght < 5:
        print("instantly")
    elif passwordLenght > 18:
        print("more than 126 years")
    elif password.isdecimal():
        numbersOnly(password, passwordLenght)
    elif all(rule(password) for rule in FirstRules) or any(rule(password) for rule in FirstRules) or all(i in string.punctuation for i in password):
        lowerAndUpper(password, passwordLenght)
    elif all(rule(password) for rule in SecondRules):
        lowerAndUpperAndNumber(password, passwordLenght)
    elif all(rule(password) for rule in ThirdRules):
        lowerAndUpperAndNumberAndSymbol(password, passwordLenght)


main()