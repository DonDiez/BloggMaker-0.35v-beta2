print("DIY Blogg MAKER 0.3v BETA")
print("§-----------------------------------------------§")
print()

site = open("index.html","w")
style = open("style.css","w")
style.write("html { \n")
site.write("<!DOCTYPE html> \n")
site.write("<html> \n")
site.write("<head> \n")
site.write('<link rel="stylesheet" type="text/css" href="style.css"> \n')
navn=str(input("Navnet ditt: "))
data=str(input("Navnet på bloggen: "))
site.write("<h1> \n")
site.write(data)
site.write("</h1> \n")
site.write("</head> \n")
site.write("<body> \n")
site.write("<p> \n")
data=str(input("Blogg-innlegg: "))
while data!="":
    site.write(data)
    data=str(input(">>> "))
    site.write("<br>")
    
site.write("</p> \n")
site.write("</body> \n")
print("Hva skal fargen på siden være? (I hex) ")
farge=input(">>> ")
style.write("   background-color:")
style.write(farge)
style.write(";")
style.write("\n")
style.write("   width:600px; \n")
style.write("   margin:auto; \n")
style.write("} \n")
style.write("p { \n")
style.write("   text-align:center; \n")
style.write("} \n")
site.write("<footer> \n")
site.write("</body> \n")
site.write("&#169 ")
site.write(navn)
site.write("</footer> \n")
site.write("</html> \n")
site.close()
style.close()
