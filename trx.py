from translate import Translator
import xml.etree.ElementTree as ET

translator = Translator(to_lang="..") #use the language code you want to translate, for example "id" for Indonesian

# Membaca file XML
tree = ET.parse('..') #enter the directory of your xml file
root = tree.getroot()

for content in root.findall('content'):
    original_text = content.text
    translated_text = translator.translate(original_text)
    content.text = translated_text

tree.write('translated_data.xml', encoding='utf-8', xml_declaration=True)
print("The translation process is complete. Data is stored in Translated_data.xml")
