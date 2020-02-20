name_list = ["Jack", "Joe", "Mike"]
message0 = "Would you like to come to the party, Mr. " + name_list[0]
message1 = "Would you like to come to the party, Mr. " + name_list[1]
message2 = "Would you like to come to the party, Mr. " + name_list[2]
print(message0)
print(message1)
print(message2)

absent_guest = name_list.pop(1)
absent_message = "Mr. " + absent_guest + " can't make it to the party."
print(absent_message)
name_list.insert(1, "Moe")
message0 = "Would you like to come to the party, Mr. " + name_list[0]
message1 = "Would you like to come to the party, Mr. " + name_list[1]
message2 = "Would you like to come to the party, Mr. " + name_list[2]
print(message0)
print(message1)
print(message2)

add_message = "I've found a bigger table."
print(add_message)
name_list.insert(0, "Bob")
name_list.insert(1, "Luke")
name_list.append("Zed")
print(name_list)
message0 = "Would you like to come to the party, Mr. " + name_list[0]
message1 = "Would you like to come to the party, Mr. " + name_list[1]
message2 = "Would you like to come to the party, Mr. " + name_list[2]
message3 = "Would you like to come to the party, Mr. " + name_list[3]
message4 = "Would you like to come to the party, Mr. " + name_list[4]
message5 = "Would you like to come to the party, Mr. " + name_list[5]
print(message0)
print(message1)
print(message2)
print(message3)
print(message4)
print(message5)

message_pity = "Sorry, I'm afraid only two of you could come."
guest_poped = name_list.pop()
message_poped = "Sorry, can't invite you to dinner, Mr. " + guest_poped
print(message_poped)
guest_poped = name_list.pop()
message_poped = "Sorry, can't invite you to dinner, Mr. " + guest_poped
print(message_poped)
guest_poped = name_list.pop()
message_poped = "Sorry, can't invite you to dinner, Mr. " + guest_poped
print(message_poped)
guest_poped = name_list.pop()
message_poped = "Sorry, can't invite you to dinner, Mr. " + guest_poped
print(message_poped)
message0 = "You're still in the invited list, Mr. " + name_list[0]
message1 = "You're still in the invited list, Mr. " + name_list[1]
print(message0)
print(message1)

del name_list[0]
del name_list[0]
print(name_list)
