import itertools
from datetime import datetime
from flask import Flask, render_template, request, Response, redirect, url_for

app = Flask(__name__)

SUBS = {
    'a': ['a', '4', '@'],
    'e': ['e', '3'],
    'i': ['i', '1', '!'],
    'o': ['o', '0'],
    's': ['s', '5', '$'],
    't': ['t', '7'],
}

def ekstakt_variante_ditelindjesh(dob_str):
    dob_str = dob_str.strip()
    if not dob_str:
        return []

    date_object = None
    formats = ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d", "%Y%m%d", "%d%m%Y"]
    for fmt in formats:
        try:
            date_object = datetime.strptime(dob_str, fmt)
            break
        except ValueError:
            continue
    if not date_object:
        return [dob_str] if dob_str.isdigit() else []
    day = f"{date_object.day:02d}"
    month = f"{date_object.month:02d}"
    year_full = str(date_object.year)
    year_short = year_full[-2:]

    variants = {
        year_full,
        year_short,
        f"{day}{month}",
        f"{day}{month}{year_full}",
        f"{day}{month}{year_short}",
        f"{month}{day}",
    }
    return list(variants)

def gjenero_variante(word):
    if not word:
        return []

    word = word.strip()
    char_options = []

    for char in word:
        char_lower = char.lower()
        if char_lower in SUBS:
            options = SUBS[char_lower]
            if char.isupper():
                options = [opt.upper() if opt.isalpha() else opt for opt in options]
            char_options.append(options)
        else:
            char_options.append([char])


    variante = set()
    for combination in itertools.product(*char_options):
        fjale_variante = ''.join(combination)
        variante.add(fjale_variante)
        variante.add(fjale_variante.capitalize())
    return list(variante)


def create_wordlist(emer, kompani, dtl, simbole):

    inpute = [emer, kompani]
    keywords = []
    for item in inpute:
        if item:
            keywords.extend([w for w in item.split() if w])
    if not keywords:
        return []
    variante_dtl = ekstakt_variante_ditelindjesh(dtl)

    base_words = set()
    for kw in keywords:
        if simbole:
            base_words.update(gjenero_variante(kw))
        else:
            kw_cleaned = kw.strip()
            base_words.update({kw_cleaned, kw_cleaned.lower(), kw_cleaned.capitalize(), kw_cleaned.upper()})

    wordlist = set()
    specials = ["!", "@", "#", "123"] if simbole else [""]


    for word in base_words:
        wordlist.add(word)
        for sc in specials:
            if sc:
                wordlist.add(f"{word}{sc}") 

    for d_var in variante_dtl:
        wordlist.add(f"{word}{d_var}")
        wordlist.add(f"{word}_{d_var}")
        for sc in specials:
            if sc:
                wordlist.add(f"{word}{d_var}{sc}")


    if len(keywords) > 1:
        for w1, w2 in itertools.permutations(base_words, 2):
            wordlist.add(f"{w1}{w2}")

            for sc in specials:
                if sc:
                    wordlist.add(f"{w1}{w2}{sc}")
            for d_var in variante_dtl:
                wordlist.add(f"{w1}{w2}{d_var}")
                for sc in specials:
                    if sc:
                        wordlist.add(f"{w1}{w2}{d_var}{sc}")

    return sorted(list(wordlist))

@app.route("/", methods=["GET", "POST"])
def index():
    passwords = []
    form_data = {"emer": "", "kompani": "", "dtl": "", "simbole": True}

    if request.method == "POST":
        form_data["emer"] = request.form.get("emer", "").strip()
        form_data["kompani"] = request.form.get("kompani", "").strip()
        form_data["dtl"] = request.form.get("dtl", "").strip()
        form_data["simbole"] = request.form.get("simbole") == "on"

        passwords = create_wordlist(
            form_data["emer"], 
            form_data["kompani"], 
            form_data["dtl"], 
            form_data["simbole"]
        )

    return render_template("index.html", passwords=passwords, form_data=form_data)
    
@app.route("/clear")
def clear():
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)