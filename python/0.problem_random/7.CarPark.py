hours_in = int(input()); minutes_in = int(input())
hours_out = int(input()); minutes_out = int(input())
time = int(0); prize = 0

# transforms times from hours to minute
transforms = (hours_out - hours_in) * 60
time = transforms + (minutes_out - minutes_in)

if time <= 15:
    print(0);
elif time <= 180:
    prize = (time//60)*10;
    if time % 60 != 0:
        prize += 10
    print(prize)
elif time <= 360:
    prize = (time//60)*20;
    if time % 60 != 0:
        prize += 20
    print(prize)
else:
    prize = 200
    print(prize)