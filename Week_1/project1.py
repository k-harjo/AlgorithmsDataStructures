# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 18:19:37 2023

@author: kharjo
"""

class MyString():
    
    def __init__(self, my_string=""):
        self.my_string = my_string
        self.char_array = [] 
        self.capacity = len(my_string)
    # This would act similar to a copy constructor    
    def __str__(self):
        return self.my_string
    
    #get len of array without using built-in len()
    def array_len(self, char_array):
        array_len = 0
        for data in char_array:
            array_len +=1
        return array_len
    
    # Private method to ensure capacity
    def _ensureCapacity(self, additional_length):
        new_capacity = self.capacity + additional_length
        self.capacity = new_capacity

    
    def concat(self, input_str):
        new_string = self.my_string + input_str.my_string
        return MyString(new_string)
    

    def equals_MyString(self, input_str):
        if input_str == self.my_string:
            return True
        else:
            return False
        
    def compare_MyString(self, input_str):
        a_count = 0
        b_count = 1
        while a_count < self.array_len(self.my_string) and b_count < self.array_len(input_str):
            if self.my_string[a_count] < input_str[b_count]:
                return -1
            elif self.my_string[a_count] > input_str[b_count]:
                return 1
            elif self.my_string[a_count] == input_str[b_count]:
                return 0
            
            a_count += 1
            b_count += 1
        
        while a_count < self.array_len(self.my_string):
            return 1
            a_count += 1
        while b_count < self.array_len(input_str):
            return -1
            b_count += 1
        while b_count == a_count:
            return 0
        
    def get_char_loc(self, index):
        if index < 0 or index >= self.array_len(self.my_string):
            raise IndexError("Index out of range.")
        count = 0
        for char in self.my_string:
            if count == index:
                return char
            count += 1
    
    #using the ASCII values
    def to_lower(self, input_str):
        lower_str = ""
        for char in input_str:
            if "A" <= char <= "Z":
                lower_str += chr(ord(char) + 32)
            else: 
                lower_str += char
        return lower_str
    
    #using the ASCII values
    def to_upper(self, input_str):
        upper_str = ""
        for char in input_str:
            if "a" <= char <= "z":
                upper_str += chr(ord(char) - 32)
            else: 
                upper_str += char
        return upper_str
    
    def substring(self, index):
        return self.my_string[index:]
    
    def slice_substring(self, a, b):
        return self.my_string[a:b]
    
    def indexOf(self, input_str):
        target = input_str.my_string
        target_len = self.array_len(target)
        for index in range(self.array_len(self.my_string) - target_len + 1):
            if self.my_string[index:index+target_len] == target:
                return index
        return -1

    def lastIndexOf(self, input_str):
        target = input_str.my_string
        target_len = self.array_len(target)
        for index in range(self.array_len(self.my_string) - target_len, -1, -1):
            if self.my_string[index:index+target_len] == target:
                return index
        return -1
    
if __name__ == "__main__":
    
    
    #Test C
    str1 = MyString("Iced Coffee")
    str2 = MyString("Iced Coffee")
    str3 = MyString("Iced Coffee")
    str4 = MyString("Iced Coffee")
    
    
    '''
    #Test B
    str1 = MyString("Good Vibes Only")
    str2 = MyString("Money, please!")
    str3 = MyString("Good job")
    str4 = MyString("Good")
    '''
    
    '''    
    #Test A
    str1 = MyString("Harry Potter")
    str2 = MyString("PigglyWiggly")
    str3 = MyString("Asarion")
    str4 = MyString("TheInquisition")
    '''    
    
    #######################
    #Run Tests
    #######################
    
    # Test __str__ method
    print(str1)
    '''
    #Test A: 
        Returned: Harry Potter
    #Test B: 
        Returned: Good Vibes Only
    #Test C:
        Returned: Iced Coffee
    '''
    
    
    # Test concat method
    concatenated = str1.concat(str2)
    print(concatenated) 
    '''
    #Test A:   
        Returned: Harry PotterPigglyWiggly
    #Test B: 
        Returned: Good Vibes OnlyMoney, please!
    #Test C:
        Returned: Iced CoffeeIced Coffee
    '''
    # Test equals_MyString method
    print(str1.equals_MyString(str2.my_string))  
    print(str1.equals_MyString(str3.my_string))
    '''
    #Test A:   
        Returned: False
                  False
    #Test B:
        Returned: False
                  False
    #Test C:
        Returned: True
                  True                
    '''

    # Test compare_MyString method
    print(str1.compare_MyString(str2.my_string)) 
    print(str1.compare_MyString(str3.my_string)) 
    '''
    #Test A:   
        Returned: -1
                  -1
    #Test B: 
        Returned: -1
                  -1
    #Test C:
        Returned: -1
                  -1    
    '''
    
    # Test get_char_loc method
    print(str1.get_char_loc(2))
    print(str3.get_char_loc(5))
    '''
    #Test A:   
        Returned: r
                  o
    #Test B:
        Returned: o
                  j
    #Test C:
        Returned: e
                  C                
    '''

    
    # Test to_lower and to_upper methods
    print(str2.to_lower(str2.my_string)) 
    print(str2.to_upper(str2.my_string)) 
    '''
    #Test A:   
        Returned: pigglywiggly
                  PIGGLYWIGGLY
    #Test B: 
        Returned: money, please!
                  MONEY, PLEASE!                 
    #Test C:
        Returned:
            iced coffee
            ICED COFFEE

    '''    
    #test substring and slice_substring methods
    print(str3.substring(2))
    print(str4.slice_substring(3, 5))
    '''
    #Test A:   
        Returned: arion
                  In
    #Test B: 
        Returned: od job
                  d                 
    #Test C:
        Returned: ed Coffee
                  d
            

    '''   
    
    # Test indexOf and lastIndexOf
    print(str1.indexOf(str4))  
    print(str1.lastIndexOf(str4)) 
    '''
    #Test A:   
        Returned: -1
                  -1
    #Test B: 
        Returned: 0
                  0
    #Test C:
        Returned: 0
                  0
                  
    '''
