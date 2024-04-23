#

"C:\Users\akopeikina\OneDrive\Desktop\Python_spcl\hometask7_files"
while True:
    try:
        with open(f'{directory}/{filename}.{extension}', 'x', encoding='utf-8') as f:
    f.write(text)
        except:
            filename = generate_text(name_length)
else:
    break
