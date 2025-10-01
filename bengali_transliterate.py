# Define mappings
independent_vowels = {
    'অ': 'o', 'আ': 'a', 'ই': 'i', 'ঈ': 'i', 'উ': 'u', 'ঊ': 'u', 'ঋ': 'ri',
    'এ': 'e', 'ঐ': 'oi', 'ও': 'o', 'ঔ': 'ou'
}

consonants = {
    'ক': 'k', 'খ': 'kh', 'গ': 'g', 'ঘ': 'gh', 'ঙ': 'ng', 'চ': 'ch', 'ছ': 'ch',
    'জ': 'j', 'ঝ': 'jh', 'ঞ': 'n', 'ট': 't', 'ঠ': 'th', 'ড': 'd', 'ঢ': 'dh',
    'ণ': 'n', 'ত': 't', 'থ': 'th', 'দ': 'd', 'ধ': 'dh', 'ন': 'n', 'প': 'p',
    'ফ': 'ph', 'ব': 'b', 'ভ': 'bh', 'ম': 'm', 'য': 'j', 'র': 'r', 'ল': 'l',
    'শ': 'sh', 'ষ': 'sh', 'স': 's', 'হ': 'h', 'ড়': 'r', 'ঢ়': 'rh', 'য়': 'y',
    'ৎ': 't', 'ং': 'ng', 'ঃ': '', 'ঁ': ''
}

special_constants = {'ড': 'r', 'ঢ': 'r', 'য': 'y'}
dot = "়"

nasal_constant = {'ঙ': 'ng', 'ঞ': 'n', 'ণ': 'n', 'ন': 'n', 'ম': 'm', 'ৎ': 't', 'ং': 'ng', 'ঃ': '', 'ঁ': ''}

vowel_diacritics = {
    'া': 'a', 'ি': 'i', 'ী': 'i', 'ু': 'u', 'ূ': 'u', 'ৃ': 'ri', 'ে': 'e',
    'ৈ': 'oi', 'ো': 'o', 'ৌ': 'ou'
}

virama = '্'

# Split word into units (independent vowels or consonants with optional clusters/diacritics)
def split_into_units(word):
    units = []
    i = 0
    while i < len(word):
        if word[i] in independent_vowels:
            units.append(word[i])
            i += 1
        elif word[i] in consonants:
            unit = word[i]
            i += 1
            # Check speciality
            if i < len(word) and word[i-1] in special_constants and word[i] == dot:
                unit += dot
                i += 1
            # Handle virama for clusters
            while i < len(word) - 1 and word[i] == virama and word[i + 1] in consonants:
                unit += word[i] + word[i + 1]
                i += 2
            # Handle vowel diacritic
            if i < len(word) and word[i] in vowel_diacritics:
                unit += word[i]
                i += 1
            units.append(unit)
        else:
            units.append(word[i])
            i += 1
    return units

# Transliterate a single unit
def transliterate_unit(unit):
    if len(unit) == 1 and (unit in independent_vowels or unit in vowel_diacritics):
        if unit in independent_vowels:
            return independent_vowels[unit]
        elif unit in vowel_diacritics:
            return vowel_diacritics[unit]
    elif unit[0] in consonants:
        if len(unit) > 1 and unit[1] == dot:
            cluster = special_constants[unit[0]]
        else:
            cluster = consonants[unit[0]]
        i = 1
        # Handle cluster with virama
        while i < len(unit) - 1 and unit[i] == virama and unit[i + 1] in consonants:
            C2 = unit[i + 1]
            if unit[0] == 'ক' and C2 == 'ষ':
                cluster = 'kkh'
            elif C2 == 'ব' and unit[0] == 'শ':
                cluster = 'ssh'
            else:
                cluster += consonants[C2]
            i += 2
        # Handle vowel diacritic
        if i < len(unit) and unit[i] in vowel_diacritics:
            cluster += vowel_diacritics[unit[i]]
        return cluster
    elif unit in ["ড়", "ঢ়", "য়"]:
        if unit == "ড়" or unit == "ঢ়" :
            return "r"
        elif unit == "য়":
            return "y"
    else:
        return unit

# Transliterate a word
def transliterate_word(word):
    units = split_into_units(word)
    result = ""
    for idx, unit in enumerate(units):
        transliterated = transliterate_unit(unit)
        # Check if current unit is a consonant without vowel diacritic
        is_consonant_no_diacritic = (unit[0] in consonants and
                                     not any(c in vowel_diacritics for c in unit))
        #Check if current unit is nasal
        if unit in nasal_constant:
            is_nasal = True
        else:
            is_nasal = False

        # Check if next unit exists and is a consonant without vowel diacritic
        if idx + 1 < len(units):
            next_unit = units[idx + 1]
            next_is_consonant_no_diacritic = (next_unit[0] in consonants and
                                              not any(c in vowel_diacritics for c in next_unit))
        else:
            next_is_consonant_no_diacritic = False
        # Add 'a' if current unit is a consonant without diacritic and either it's the first unit or next unit is also a consonant without diacritic
        if is_consonant_no_diacritic and (idx == 0 or next_is_consonant_no_diacritic) and not is_nasal:
            transliterated += 'a'
        result += transliterated
    return result

# Transliterate full text with proper capitalization
def transliterate_text(text):
    words = text.split()
    transliterated_words = []
    for i, word in enumerate(words):
        transliterated = transliterate_word(word)
        # Capitalize first letter if it's the start of a sentence
        if i == 0 or (i > 0 and words[i - 1].endswith('।')):
            transliterated = transliterated[0].upper() + transliterated[1:]
        transliterated_words.append(transliterated)
    return ' '.join(transliterated_words)

if __name__ == "__main__":
    examples = ["আমার সোনার বাংলা"]
    for ex in examples:
        print(f"{ex} → {transliterate_text(ex)}")