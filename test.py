import json

class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)["data"]

def lf(file):
    path = (file)
    json_data = None

    with open(path) as json_file:
        json_data = json.load(json_file)

    return json_data

if __name__ == "__main__":
    f_template = lf("template.json")
    f_doc = lf("doc.json")

    # Convert file to json
    json_post = json.dumps(f_template)
    # Create Payload object
    template = Payload(json_post)
    
    # Convert file to json
    json_post = json.dumps(f_doc)
    # Create Payload object
    doc = Payload(json_post)

    #content = str(template.content)
    content = ''.join(template.content)

    for t in template.tokens:
        # Get the value from the doc section we want
        # to use to find and replace the token with
        value = str(doc.doc["vehicle"][t])
        # Format the token
        token = "{%s}" % t
        # Find the token and replace it with the value
        content = content.replace(token, value)
    print content
    #print doc
