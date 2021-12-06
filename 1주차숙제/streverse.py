input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    if string.count('0')>string.count('1'):
      count = 0
      for str in string:
        if(str =='1'):
          str = '0'
          count +=1
    else:
      count = 0
      for str in string:
        if(str == '0'):
          str = '1'
          count +=1
    return count


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)