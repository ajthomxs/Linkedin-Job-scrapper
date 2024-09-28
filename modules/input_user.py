# Getting input from User

def get_job():
    job=int(input("Enter Your Job Selection:\n"))
    if job==1:
        return "Machine Learning Engineer"
    elif job==2:
        return "Data Scientist"
    elif job==3:
        return "Data Analyst"
    else:
        print("Wrong choice")
        get_job()

def get_loc():
    loc=int(input("Enter the Location(Enter the option):\n"))
    if loc == 1:
        return "Bengaluru"
    elif loc==2:
        return "Chennai"
    elif loc==3:
        return "Mumbai"
    else:
        print("Wrong choice")
        get_loc()

def ponc():
    nc=int(input("Enter Your Choice: "))
    if nc ==2:
        return 2
    else:
        return 1