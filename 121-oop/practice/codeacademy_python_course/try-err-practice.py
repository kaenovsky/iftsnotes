numbers = [2, 5, 57, 8, 2] # not err
# numbers = [8, 'x', 'z', 4] # err

try:
    avg = sum(numbers) / len(numbers)
    print('the average of the list is ', avg)
except:
    print('Cannot print avg! Those are not numbers.')
finally:
    print('Good luck :)')