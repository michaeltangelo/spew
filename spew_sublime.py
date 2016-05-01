# Welcome to Spew
# Created by Michael Tan and Arvind Ragjpeom4k
# Text to Code Generator for the Java Programming Language
from six.moves import input

tags = {"for":["from", "to"],
        "create":["new","named"],
        "function":"st",
        "from":"st",
        "to":"st",
        "new":"st",
        "named":"st",
    }

# arguments: iterator, initialization value, length
def spew_for_loop(args):
    #print("FUCK YOU FAGGOT")
    print("Generated output: \n")
    print("for({0} = {1}; {0} < {2}; {0}++) {{\n\n}}".format(args[0],args[1],args[2]))

# arguments: object, name
def spew_new_object(args):
    print("{0} {1} = new {0}();".format(args[0],args[1]))
    #print("spewed new object", s)           

def spew_for_loop_pp(d):
    command = d[0]
    d = d[1:]
    split_words = tags["for"]
    #split_words = ["from","to"]
    args = []
    for i in d:
        if i not in split_words:
            args.append(i)
        else:
            continue
    #print(args)
    spew_for_loop(args)

def spew_new_object_pp(d):
    command = d[0]
    d = d[1:]
    split_words = tags["create"]
    #split_words = ["new","named"]
    args = []
    temp = []
    for i in d:
        if i not in split_words:
            temp.append(i.title())
        else:
            args.append(''.join(temp))
            temp = []
    args.append(''.join(temp))
    args = list(filter(None, args)) # gets rid of empty strings in list
    spew_new_object(args)

#MAIN
user_input = input("> ")
while user_input != "q":
    tag_dict = {"for":spew_for_loop_pp,
                "create":spew_new_object_pp,
                }

    split_input = user_input.split()
    # find which spew function user wants
    for i in split_input:
        i = i.strip()
        if i in tag_dict:
            spew_preprocess = tag_dict[i]
            temp = split_input[split_input.index(i)+1:]
            spew_preprocess(split_input)
            break
            
    user_input = input("> ")

# tests
#spew_for_loop("i","0","length")
