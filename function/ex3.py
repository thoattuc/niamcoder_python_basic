"""
    Viết 1 hàm nhận vào 2 tham số đầu vào
    1. Cân nặng của 1 người (đơn vị: kg)
    2. Chiều cao của người đó (đơn vị: mét)
    Hàm trả về 3 thông tin sau:
    1. Chỉ số cân đối cơ thể BMI = cân nặng/chiều cao^2
    2. Thể trạng của người đó
    3. Nguy cơ phát triển bệnh
    2. và 3. được kết luận dựa vào bảng sau:
    BMI             Status (Thể trạng)  Disease risk (Nguy cơ phát triển bệnh)
    < 18.5          Underweight         Low
    18.5-24.9       Normal              Medium
    25.0-29.9       Overweight          High
    30.0-34.9       Obese               High
    > 35.0          Extremely Obese     Very High
"""


def estimate_infor(height, weight):
    bmi = round((weight / (height ** 2)), 1)
    if bmi < 18.5:
        status = "Underweight"
        risk = "Low"
    elif 18.5 <= bmi <= 24.9:
        status = "Normal"
        risk = "Medium"
    elif 25 <= bmi <= 29.9:
        status = "Overweight"
        risk = "High"
    elif 30 <= bmi <= 34.9:
        status = "Obese"
        risk = "High"
    else:
        status = "Ex Obese"
        risk = "Very high"
    return bmi, status, risk


if __name__ == '__main__':
    height = float(input("Enter the height (m): "))
    weight = float(input("Enter the weight (kg): "))
    bmi, status, risk = estimate_infor(height, weight)
    print("BMI:", bmi)
    print("Status:", status)
    print("Disease risk:", risk)
