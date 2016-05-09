# Welcome to Spew
# Created by Michael Tan and Arvind Ragjpeom4k
# Text to Code Generator for the Java Programming Language
from six.moves import input

tags = {"for":["from", "to"],
        "create":["new","named"],
        "function":["params"],
        "classes":["car"],
        "access":["private","public","protected","static"],
        "types":["void","int","long","string","double","float","boolean","char","short","byte"],
        "from":"st",
        "to":"st",
        "new":"st",
        "named":"st",
    }

all_keys = ["everything in java"]

def parse_dot(args):
    for i in range(len(args)):
        if args[i] == "dot":
            args[i-1:i+2] = [args[i-1]+"."+args[i+1]]
            break
    return args

def parseDot(args):
    temp = ""
    dotarr.append(args[0])
    for i in range(0,len(args)-1):
        if(i>len(args)-1):
            break
        if args[i] == "dot":
            temp = args[i-1] + "." + args[i+1]
            del args[i-1]
            del args[i-1]
            del args[i-1]
            args.insert(i-1, temp)

# arguments: iterator, initialization value, length
def spew_for_loop(args):
    # concat dot
    args = parse_dot(args)
    if "size" in args[2].lower():
        args[2] += "()"
    o = "for({0} = {1}; {0} < {2}; {0}++) {{}}".format(args[0],args[1],args[2])
    #print(o)
    return o

# arguments: object, name
def spew_new_object(args):
    o = "{0} {1} = new {0}();".format(args[0],args[1])
    #print(o)
    return o          

# arguments: access modifier, return type, name, parameters
def spew_new_function(args):
    args[2] = args[2][0].lower() + args[2][1:]
    if args[1] == "string":
        args[1] = "String"
    o = "{0} {1} {2}({3}) {{}}".format(args[0],args[1],args[2],args[3])
    #print(o)
    return o

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
    return spew_for_loop(args)

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
    return spew_new_object(args)

def spew_new_function_pp(d):
    command = d[0]
    d = d[1:]
    classes = tags["classes"]
    access = tags["access"]
    types = tags["types"]
    exclude_words = tags["function"]
    include_words = classes + access + types
    args = []
    temp = []
    # parse / merge d pre-parameters
    for i in d:
        if i in exclude_words:
            args.append(''.join(temp))
            temp=[]
            d = d[d.index(i)+1:]
            break
        else:
            if i in include_words:
                if i in classes:
                    args.append(i.title())
                else:
                    args.append(i)
            else:
                temp.append(i.title())
    args.append(''.join(temp))
    args = list(filter(None, args))
    if len(args) > 3:
        args[0:2] = [' '.join(args[0:2])]

    # parse / merge parameters
    plist = []
    temp = []
    for i in d:
        if i in types:
            plist.append(''.join(temp))
            temp = []
            plist.append(i)
        if i in classes:
            plist.append(''.join(temp))
            temp = []
            plist.append(i.title())
        elif i not in types and i not in classes:
            temp.append(i)
    plist.append(''.join(temp))
    plist = list(filter(None,plist))           

    # add comma to every other arg
    for i in range(1, len(plist)-2,2):
        plist[i] = plist[i]+","
        
    args.append(' '.join(plist))
    return spew_new_function(args)

def choose_demo(s):
    init = ""
    if s == "demo1":
        file = open("demo1.txt", "r")
        init = file.read()
        file.close()
    if s == "demo2":
        file = open("demo2.txt","r")
        init = file.read()
        file.close()
    if s == "demo3":
        file = open("demo3.txt", "r")
        init = file.read()
        file.close()
    init = init.replace("\t","    ")
    return init

#MAIN
init = ""
while True:
    demo = input("Select a demo: (demo1 | demo2 | demo3)\n>> ")
    init = choose_demo(demo)
    if not init:
        print("Not a valid demo. Try again.")
        continue
    file = open("SpewDemo.java","w")
    file.write(init)
    file.close()
    break

user_input = ""
while user_input != "q":
    demo = open("SpewDemo.java","r")
    display = demo.read()
    demo.close()
    print("SpewDemo.java\n-------------")
    print(display)
    print("--------")
    
    user_input = input(">> ")
    switch = choose_demo(user_input)
    file = open("SpewDemo.java","w")
    if switch:
        init = switch
        file.write(switch)
        file.close()
        continue
    else:
        file.write(init)
        file.close()

    tag_dict = {"for":spew_for_loop_pp,
                "create":spew_new_object_pp,
                "function":spew_new_function_pp,
                }

    split_input = user_input.split()
    # find which spew function user wants
    for i in split_input:
        i = i.strip()
        if i in tag_dict:
            spew_preprocess = tag_dict[i]
            temp = split_input[split_input.index(i)+1:]
            break
    o = ""
    try:
        o = spew_preprocess(split_input)
    except:
        print("Error: unable to parse line. Retry.")
    finally:
        file = open("SpewDemo.java","a")
        file.write(o)
        file.close()
