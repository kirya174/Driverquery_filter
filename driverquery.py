import os
os.system('cmd /c driverquery > drivers.txt')

filter_query = "File System"

with open('drivers.txt', encoding='utf8') as drivers:
    print("Module Name  Display Name           Driver Type   Link Date\n"
          "============ ====================== ============= ======================")
    for row in drivers:
        if filter_query in row:
            print(row.strip())
