# translate the frequency list
from googletrans import Translator
import pprint
from main import top_99


translator = Translator()

pp = pprint.PrettyPrinter(indent=4)

# translate the words list to english
top_100_frequency_list_with_translation = []
for el in top_99:
    translation = translator.translate(el[1], des="en", src="fi")
    new_el = (el[0], el[1], translation.text)
    top_100_frequency_list_with_translation.append(new_el)

pp.pprint(top_100_frequency_list_with_translation)
