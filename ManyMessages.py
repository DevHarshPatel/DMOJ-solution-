homework_starting = int(input())
interval = int(input())
larry_message_time = int(input())

if homework_starting + (interval*3) >= larry_message_time:
    for i in range(3):
        if (homework_starting + interval) >= larry_message_time:
            print(homework_starting + interval)   
            break
        else:
            homework_starting += interval
else:
    print("Who knows...")
