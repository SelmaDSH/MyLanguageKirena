# MyLanguageYumeko
# Yumeko Language - A Constructed Language Translator

A Japanese-inspired constructed language (conlang) with a bidirectional translator, grammar analyzer, and word generator.

**Try it:** Translate "I love you" → `zima yameri reka` 🌸

---

## What This Does

Yumeko is a completely invented language with:
- Japanese-inspired phonetics (soft, melodic sounds)
- Consistent grammar rules (suffixes modify meaning)
- 200+ word vocabulary
- Bidirectional translation (English ↔ Yumeko)

---

## Features

✅ **English → Yumeko Translation**
- Handles plurals, verb tenses, and adjectives
- Unknown words marked with brackets

✅ **Yumeko → English Translation**
- Reverse translation with grammar detection

✅ **Grammar Analyzer**
- Identifies word types (noun, verb, adjective, pronoun)
- Detects conjugations (plural, past tense, present tense)

✅ **Random Word Generator**
- Creates new words following Yumeko phonetic patterns

---

## Grammar Rules

| Type | Pattern | Example |
|------|---------|---------|
| **Nouns** | End in `-a` or `-o` | `pikuma` (cat), `tameno` (sun) |
| **Verbs** | End in `-ri` | `yameri` (love), `mokari` (eat) |
| **Adjectives** | End in `-ne` | `nokane` (cute), `yamane` (beautiful) |
| **Plural** | Add `-ko` | `pikuma` → `pikumako` (cats) |
| **Past Tense** | Replace `-ri` with `-ta` | `yameri` → `yameta` (loved) |
| **Present Tense** | Replace `-ri` with `-ru` | `yameri` → `yameru` (loves) |

---

## Usage Examples

### Example 1: Translate to Yumeko
```
Mode: 1
Enter English text: i love the beautiful flower
Output: zima yameri [the] yamane miruto
```

### Example 2: Translate to English
```
Mode: 2
Enter Yumeko text: nokane pikuma 
Output: cute cat
```

### Example 3: Analyze Grammar
```
Mode: 3
Enter Yumeko text: yameri pikuma nosane
Output:
yameri (verb: love)
pikuma (noun: cat)
nosane (adjective: happy)
```

### Example 4: Generate Random Words
```
Mode: 4
Output:
  Noun: tario
  Verb: yisiri
  Adjective: rerene
```

---

## Sample Vocabulary

### Common Words
```
English     Yumeko
-------------------
water       chiruka
sun         tameno
moon        kiraya
star        nosara
flower      miruto
cat         pikuma
love        yameri
beautiful   yamane
happy       nosane
```

### Pronouns
```
I           zima
you         reka
he          moro
she         tena
we          piku
they        yona
```

---

## Project Structure
```
yumeko-language/
├── Yumeko.py          # Main program
└── README.md          # This file
```

---

## Technologies Used

- **Python 3.8+** - Programming language
- **Standard library only** - No external dependencies
  - `random` - Word generation
  - Built-in string operations

---

## Why I Built This

Building on my academic background in linguistics, this project aims to bridge theoretical language analysis and computational implementation. 
it explores how linguistic structures can be formalized and modeled programmatically.


---

## Limitations & Future Work

**Current Limitations:**
- No handling of irregular verbs ("went", "ate")
- Limited to simple sentence structures
- No support for articles (a, the) or prepositions

**Future Improvements:**
- [ ] Add more vocabulary (500+ words) for a better translation
- [ ] Add text-to-speech for pronunciation
- [ ] Integration with NLP sentiment analysis project



