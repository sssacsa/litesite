# so uhhh hi
# this code will be messed up so don't expect any clean code 
# love you w3schools, geeksforgeeks, and random ass forums <3

""" TODO
nothing
"""

import sys
import os

ver = 0.02

def openf(filename):
    ltst = open(filename, "r")
    return ltst

def translate(ltstf):
    tempstr = ""
    i = 0
    x = 1
    style = False
    imp = False
    while i <= (len(ltstf)-1):
        l = ltstf
        templn = l[i]

        if "#" and "%#" in l[i]:
            templn = templn.replace("%#", "</h1>")
            templn = templn.replace("#", "<h1>")
        if "!" and "%!" in l[i]:
            templn = templn.replace("%!", "</b>")
            templn = templn.replace("!", "<b>")
        if "\\" and "%\\" in l[i]:
            templn = templn.replace("%\\", "</i>")
            templn = templn.replace("\\", "<i>")
        if "*" and "%*" in l[i]:
            templn = templn.replace("%*", "</title>")
            templn = templn.replace("*", "<title>")
        if "~" and "%~" in l[i]:
            templn = templn.replace("%~", "</s>")
            templn = templn.replace("~", "<s>")
        if "*n*" in l[i]:
            templn = templn.replace("*n*", "<br>")
        if "*c*" and "%c*" in l[i]:
            templn = templn.replace("%c*", "</center>")
            templn = templn.replace("*c*", "<center>")
        if "*s*" in l[i]:
            templn = templn.replace("*s*", "<style>")
            style = True
            print("entering style mode")
        if "%s*" in l[i]:
            templn = templn.replace("%s*", "</style>")
            style = False
            print("exiting style mode")
        if "*l*" and "%l*" in l[i]:
            templn = templn.replace("%l*", "</a>")
            templn = templn.replace("*l*", "<a href=")
            templn = templn.replace("**", ">")
        if "d*"in l[i]:
            templn = templn.replace("%d*", "</div>")
            templn = templn.replace("*d*", "<div")
            templn = templn.replace("**", ">")    
        if "*r*" in l[i]:
            templn = templn.replace("*r*", "<hr>")
        if "*i*" in l[i]:
            i += 1
            templn = l[i]
            imp = True
            print("enter import mode")
        if "%i*" in l[i]:
            templn = ""
            imp = False
            print("exit import mode")
        if "--" in l[i]:
            templn = ""
        
        if style == True:
            if "bgc" in l[i]:
                templn = templn.replace("bgc", "background-color: ")
            if "txc" in l[i]:
                templn = templn.replace("txc", "color: ")
            if "ffa" in l[i]:
                templn = templn.replace("ffa", "font-family: ")
            if "fsz" in l[i]:
                templn = templn.replace("fsz", "font-size: ")
            if "fwg" in l[i]:
                templn = templn.replace("fwg", "font-weight: ")
            if "*imp" in l[i]:
                templn = templn.replace("*imp", "@import")
            if "$" in l[i]:
                templn = templn.replace("$", ";")
   
        if imp == True and "%i*" not in templn and "*i*" not in templn:
            ltstin = open(templn.strip(), encoding="utf-8")
            l = ltstin.readlines()
            ltstin.close()
            ltstin = open(templn.strip(), encoding="utf-8")
            ltst = ltstin.read()
            templn = translate(l)
        # else:
            # templn = templn.replace(templn, f"<p>{templn}</p>")
        templn = templn.replace("/<b>", "!")
        templn = templn.replace("/<i>", "\\")
        templn = templn.replace("/<s>", "~")
        templn = templn.replace("/<h1>", "#")
        templn = templn.replace("/<style>", "*s*")
        templn = templn.replace("/background-color:", "/bgc")

        print(f"Converting line {x}/{len(l)}")
        tempstr = tempstr+templn
        i += 1
        x += 1
    return tempstr
    
    
print(f"Litesite v{ver}\n"\
"https://github.com/sssacsa/lietsite")
if len(sys.argv) >= 2:
    for x in sys.argv:
        if not x == sys.argv[0]:
            ltstin = open(x, encoding="utf-8")
            l = ltstin.readlines()
            ltstin.close()
            ltstin = open(x, encoding="utf-8")
            ltst = ltstin.read()
            out = translate(l)
            folder = x.replace(".ltst", "")
            os.mkdir(folder)
            ltstout = open(f"{folder}/index.html", "w")
            ltstout.write(out)
            ltstout.close()
            print("Done!")
            
