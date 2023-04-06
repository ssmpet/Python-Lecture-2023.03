PI = 3.1415926535

def number_input():
    return float(input('숫자 입력> '))

def get_circumference(radius):
    return 2 * PI * radius

def get_area(radius):
    return PI * radius * radius

def print_name():
    print(__name__)

# python test_module.py와 같이 돌릴 경우에는 아래 코드가 실행됨
if __name__ == '__main__':
    print('원의 반지름: 10')
    print(f'둘레: {get_circumference(10):.4f}, 면적: {get_area(10):.4f}')


