f = open("names.txt", "r")

lines = f.readlines()

for name in lines:
    print("""
<div class="name notitle">
    <p>"""+name.strip()+"""</p>
</div>
""")