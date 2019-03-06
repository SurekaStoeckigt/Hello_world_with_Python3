def fizzbuzz(num):
    if num % 3 == 0:
        return 'fizzbuzz' if (num % 5 == 0)  else 'fizz'
    if num % 5 == 0:
        return 'buzz'
    else:
        return num
def main():
    for i in range(1,101):
        print fizzbuzz(i)
