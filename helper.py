from flask import json

# this function will load all the 
# members from my members.json file
def load_members():
  with open("members.json") as file:
    MEMBERS = json.load(file)

  return MEMBERS

def get_member(email):
  """This function will check if a member exists and return their index
  and the member dict. If the member does not exist then it will return None"""
  MEMBERS = load_members() # get the current list of members
  #loop through the list of MEMBERS and look for a matching email
  for index, member in enumerate(MEMBERS):
    if member.get("email") == email: #found a matching email
      return index, member
  return -1, None # -1 for index, and None for member


def add_member(new_member):
  MEMBERS = load_members() # get the current list of members
  MEMBERS.append(new_member)  # add the new member to the list
  # update the json file with the new data
  with open("members.json", "w") as file:
    json.dump(MEMBERS, file, indent=2)
  return MEMBERS.index(new_member) # return the index of the new member