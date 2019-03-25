def is_column_sorted(input_data):
    for index in range(len(input_data)-1):
        if not input_data[index] <= input_data[index+1]:
            return 0
    return 1

def is_last_column_sorted(previous_column, current_column):
    for index in range(len(current_column)):
        if not previous_column[index] <= current_column[index]:
            return 0
    return 1

if __name__== '__main__':
    sorted_column_index=[]
    stack=[]
    input_data = raw_input()
    input_data = input_data.split(' ')
    n,m = map(int, input_data)
    
    matrix_data= []
    for i in range(n):
        matrix_data.append(raw_input())
    if not matrix_data:
        print 0
    
    else:
        for row_index in range(len(matrix_data[0])):
            column_data= [row_data[row_index] for row_data in matrix_data]
            if stack==[]:
                is_sorted = is_column_sorted(column_data)
                sorted_column_index.append(is_sorted)
                if is_sorted:
                    stack.append(column_data)

            else:
                previous_column=stack[-1]
                is_sorted = is_column_sorted(column_data) and is_last_column_sorted(previous_column, column_data)
                sorted_column_index.append(is_sorted)
                if is_sorted:
                    stack[-1]=column_data

        print sorted_column_index.count(0)
