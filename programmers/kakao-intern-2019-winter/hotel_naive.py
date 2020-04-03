# k : total # of rooms
# room_number: list of room requests from clients
def give(status, room):
    if room in status:
        give(status, room + 1)
    else:
        status.append(room)

def solution(k, room_number):
    status = [room_number[0]]
    for room in room_number[1:]:
        give(status, room)

    return status
