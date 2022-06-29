from pprint import pprint





def revere_array(numbers):
    
   
    start_index = 0;
    end_index = len(numbers)-1; 
    while start_index < end_index:
        numbers[start_index], numbers[end_index] = numbers[end_index], numbers[start_index]
        start_index += 1
        end_index -= 1
        
    print(numbers)
numbers = [1,2,4,5,6,7]
revere_array(numbers);