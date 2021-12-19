from datetime import date, timedelta

start_date = date(2545, 6, 1)
end_date = date(2548, 6, 1)
delta = timedelta(days=1)
while start_date <= end_date:
    print(start_date.strftime("%d/%m/%Y"))
    start_date += delta