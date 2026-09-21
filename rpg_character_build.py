full_dot = '●'
empty_dot = '○'
def create_character(name, strength, intelligence ,charisma):
    if not isinstance(name,str):
        return 'The character name should be a string'
    elif name == '':
        return 'The character should have a name'
    elif len(name) > 15:
        return 'The character name is too long'
    elif " " in name:
        return "The character name should not contain spaces"
    if not all(isinstance(x, int) for x in (strength, intelligence, charisma)):
        return 'All stats should be integers'
    elif any (x < 1 for x in (strength, intelligence, charisma)):
        return 'All stats should be no less than 1'
    elif any (x > 9 for x in (strength, intelligence, charisma)):
        return 'All stats should be no more than 9'
    elif sum((strength, intelligence, charisma)) != 15:
         return 'The character should start with 15 points'
    return (
        name + "\n" + "STR " + "●" * strength + "○" * (15 - strength) + "\n" + "INT " + "●" * intelligence + "○" * (15 - intelligence) + "\n" + "CHA " + "●" * charisma + "○" * (15 - charisma))     

input_name = input("Enter the character name: ")
input_strength = int(input("Enter the character strength (1-9): "))
input_intelligence = int(input("Enter the character intelligence (1-9): "))
input_charisma = int(input("Enter the character charisma (1-9): "))
print(create_character(input_name, input_strength, input_intelligence, input_charisma))