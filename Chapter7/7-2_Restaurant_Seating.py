# May 15.2022

prompt = input("How many people will be dining tonight?: ")
prompt = int(prompt)

if prompt > 8:
    print(f"\nPlease have a seat, a table will be available shortly.")
else:
    print(f"\nRight this way to your table.")
