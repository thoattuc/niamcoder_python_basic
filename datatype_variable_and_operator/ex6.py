"""
    Đội Manchester United tham gia giải ngoài hạng anh.
    Yêu cầu người dùng nhập vào lần lượt 3 số tự nhiên
    tương ứng với số trận thắng, hòa, thua của đội.
    Quy tắc tính điểm như sau:
    - Mỗi trận thắng đội sẽ được 3 điểm
    - Mỗi trận hòa đội sẽ được 1 điểm
    - Mỗi trận thua đội sẽ không được điểm nào
    Tính số điểm đội có được
"""

win = int(input('Enter the number of the win: '))
draw = int(input('Enter the number of the draw: '))
lost = int(input('Enter the number of the lost:'))

points = 3 * win + 1 * draw + 0 * lost
print ("Total points: ", points)