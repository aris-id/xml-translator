from translate import Translator
import xml.etree.ElementTree as ET

translator = Translator(to_lang="..") #use the language code you want to translate, for example "id" for indonesian

tree = ET.parse('..') #enter the directory of your xml file
root = tree.getroot()

batch_size = 100000  # Batch size in letters
current_batch = 1
current_text = ""

def save_batch_to_file(text, batch_number):
    root = ET.Element("data")
    content_element = ET.SubElement(root, "content")
    content_element.text = text
    tree = ET.ElementTree(root)
    filename = f'translated_data_{batch_number}.xml'
    tree.write(filename, encoding='utf-8', xml_declaration=True)
    print(f"Batch {batch_number} disimpan ke {filename}")

for content in root.findall('content'):
    original_text = content.text
    translated_text = translator.translate(original_text)
    if len(current_text) + len(translated_text) > batch_size:
        save_batch_to_file(current_text, current_batch)
        current_batch += 1
        current_text = translated_text
    else:
        current_text += translated_text

if current_text:
    save_batch_to_file(current_text, current_batch)

print("The translation process is complete. All data is saved to file.")

with open('final_translated_data.xml', 'w', encoding='utf-8') as final_file:
    final_file.write('<?xml version="1.0" encoding="utf-8"?>\n<data>\n')
    for i in range(1, current_batch + 1):
        with open(f'translated_data_{i}.xml', 'r', encoding='utf-8') as batch_file:
            content = batch_file.read()
            content = content.replace('<?xml version="1.0" encoding="utf-8"?>\n', '').replace('<data>', '').replace('</data>', '')
            final_file.write(content)
    final_file.write('</data>')

print("All batches are combined into one file: final_translated_data.xml")
