from jinja2 import Environment, FileSystemLoader

yaasaOfTheDay = {"title": "అంబటి బీరకాయల",
"meaning": "నేతిబీరకాయల్ని ‘అంబటి బీరకాయలు’, అంబలి తాగేవేళని అంబటాల్ల అని అంటార",
"ety":"నెయ్యిలాగే అంబలి కూడా ద్రవరూప ఆహారపదార్థం. నెయ్యి మాదిరిగానే స్నిగ్ధంగా ఉంటుంది. అందుకే అదిక్కడ నెయ్యి స్థానంలోకి వచ్చింది. నీ కడుపున అంబలివడ (నీ కడుపులో అంబలి పడనీ) మొదలైన మాటలూ కూడా ఉన్నాయి.",
"example":"ఈ రోజు అంబటి బీరకాయల పచ్చడి ఎలా చేయాలో చూద్దాము.ఊరి నుండి వచ్చేసరికి అంబటాల్ల దాటింది",
"regions":["తెలంగాణ","రాయలసీమ"]}

theme = {"bgtheme":"bg-light", "font":"text-dark", "bgthemeContrast":"bg-dark", "fontContrast":"text-white"}



file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)

template = env.get_template('card.html')
output = template.render(yaasaOfTheDay = yaasaOfTheDay,darkTheme = theme )

template = env.get_template('index.html')
index = template.render(card = output )

print(index)

