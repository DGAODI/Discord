def fizz_buzz(begin, end):
    list_of_count = list(range(begin, end+1))
    result = ''
    for i in list_of_count:
        if i % 3 == 0 and i % 5 == 0:
                result += 'FizzBuzz '
        elif i % 3 == 0:
            result += 'Fizz '

        elif i % 5 == 0:
                result += 'Buzz '
        else:
            result += (str(i) + ' ')

    return  result.strip()

print (fizz_buzz(1, 20))


