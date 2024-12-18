# Open the input file as a list





# Given an arrangement of stones, each with an engraved number. 
# After every blink of your eyes, certain rules are applied to each stone depending on the number engraved on it
# If the number engraved is 0, repalce it with a stone with the number 1 engraved
# If the stone has a number whose digits are an even number, the digits are cut in half and the stone is split
# maintaing its order, the left stone engraves the left half of the digits and the right stone contains the other
# for example: the number 1234 is engraved. The stone is split where the 12 is engraved to the left stone and 34 engraved on the right
# If none of the rules is applicable to the number engraved, multiply that number by 2024
# After 25 blinks, how many stones do we have in this arrangement