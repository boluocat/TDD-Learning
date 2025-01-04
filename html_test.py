def attribute(kv):
    return f"{kv[0]}=\"{kv[1]}\""


def attribute_list(attributes):
    return " ".join(map(attribute, attributes.items())) if len(attributes) else ""


def closed_tag(name="div", content="", attributes={}):
    if attributes == {}:
        output = f"<{name}{attribute_list(attributes)}>{content}</{name}>"
    else:
        output = f"<{name} {attribute_list(attributes)}>{content}</{name}>"
    return output


def open_tag(name="div", attributes={}):
    if attributes == {}:
        output = f"<{name}{attribute_list(attributes)} />"
    else:
        output = f"<{name} {attribute_list(attributes)} />"
    return output


def tag(name="div", content="", attributes={}, is_closed=True):
    return closed_tag(name, content, attributes) if is_closed else open_tag(name, attributes)


def div(content="", attributes={}):
    return tag("div", content, attributes, True)


def br():
    return tag("br", "", {}, False)


def p(content="", attributes={}):
    return tag("p", content, attributes, True)


def img(attributes={}):
    return tag("img", "", attributes, False)

# TEST
print(
    div(
        div(
            f"Hello{br()}World"
        )
    )
)

def test_dom():
    assert div("Hello") == "<div>Hello</div>"
    assert div("Hello", {"class": "greeting"}) == "<div class=\"greeting\">Hello</div>" 
    assert img({"src": "image.jpg", "alt": "image"}) == "<img src=\"image.jpg\" alt=\"image\" />"
    assert p("Hello") == "<p>Hello</p>"
    assert p("Hello", {"class": "greeting"}) == "<p class=\"greeting\">Hello</p>"
    assert br() == "<br />"
    print("All tests pass")
    
    
test_dom()