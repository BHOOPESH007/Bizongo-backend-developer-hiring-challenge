def lcs(first_string_len, second_string_len, count) : 
    
    if (first_string_len == 0 or second_string_len == 0) : 
        return count 
        
    if (first_string[first_string_len - 1] == second_string[second_string_len - 1]) : 
        count = lcs(first_string_len - 1, second_string_len - 1, count + 1) 
    
    count = max(count, max(lcs( first_string_len, second_string_len - 1, 0), 
                        lcs( first_string_len - 1, second_string_len, 0))) 

    return count 

if __name__ == "__main__" : 
    first_string = raw_input()
    second_string = raw_input()

    first_string_len= len(first_string) 
    second_string_len = len(second_string) 

    print lcs(first_string_len, second_string_len, 0)


