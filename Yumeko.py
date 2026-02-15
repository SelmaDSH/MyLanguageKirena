"""
YUMEKO LANGUAGE - A Constructed Language for NLP Practice
Created by ME

Linguistic Features:
- Japanese-inspired phonetics (but completely invented vocabulary)
- Agglutinative morphology (add suffixes to modify meaning)
"""

import random

# ============================================================
# 1. CORE VOCABULARY 
# ============================================================

YUMEKO_DICT = {
    # Nouns (end in -a or -o)
    "water": "chiruka",
    "sun": "tameno",
    "moon": "kiraya",
    "star": "nosara",
    "sky": "hakema",
    "flower": "miruto",
    "tree": "sabeno",
    "rain": "yorika",
    "snow": "fumano",
    "wind": "teraka",
    "cloud": "morisa",
    "rainbow": "pikuno",
    "mountain": "zareto",
    "river": "himona",
    "ocean": "nokura",
    "forest": "yemito",
    "garden": "risaka",
    "leaf": "tetano",
    "grass": "wiruma",
    "seed": "pokira",
    "person": "sanowa",
    "child": "nuriko",
    "friend": "yameto",
    "family": "kosena",
    "mother": "tiruma",
    "father": "benako",
    "sister": "fokina",
    "brother": "zemuro",
    "baby": "chiruno",
    "girl": "mikasa",
    "boy": "yorano",
    "cat": "pikuma",
    "dog": "teruno",
    "bird": "waseka",
    "fish": "norima",
    "butterfly": "himeka",
    "dragon": "zaruko",
    "house": "tenoma",
    "door": "kiruno",
    "window": "yemara",
    "book": "pokusa",
    "pen": "mirena",
    "paper": "fumito",
    "food": "soraka",
    "bread": "terima",
    "cup": "nokura",
    "plate": "hikesa",
    "light": "yamura",
    "fire": "chiroka",
    "stone": "teteno",
    "gold": "miraka",
    "silver": "yoruno",
    "peace": "sanuma",
    "dream": "kirena",
    "hope": "pokusa",
    "heart": "terima",
    "soul": "nosaka",
    "life": "hikora",
    "death": "fumena",
    "time": "yorika",
    "memory": "miruta",
    "magic": "zaruma",
    "power": "tetano",
    "strength": "nokesa",
    "wisdom": "yameka",
    "beauty": "chiruma",
    
    # Colors (nouns)
    "red": "pirako",
    "blue": "tenuma",
    "green": "miroka",
    "yellow": "sorena",
    "white": "hikuma",
    "black": "yorano",
    "pink": "kiruma",
    "purple": "nosaka",
    
    # Verbs (all end in -ri)
    "love": "yameri",
    "like": "teruri",
    "see": "nokari",
    "look": "chiruri",
    "speak": "fumari",
    "say": "pokuri",
    "hear": "miranri",
    "walk": "hikeri",
    "run": "sorari",
    "fly": "yemuri",
    "jump": "kirari",
    "dance": "tetari",
    "sing": "nosuri",
    "play": "yoruri",
    "work": "zamuri",
    "sleep": "pikari",
    "wake": "teruri",
    "eat": "mokari",
    "drink": "chiruri",
    "cook": "fumeri",
    "make": "hikari",
    "create": "yorami",
    "write": "nokuri",
    "read": "mirasri",
    "learn": "teraki",
    "teach": "yamuri",
    "know": "pokari",
    "think": "soruri",
    "feel": "kiremi",
    "understand": "tetari",
    "remember": "nosuri",
    "forget": "yoraki",
    "give": "hikumi",
    "take": "chirari",
    "help": "fumori",
    "open": "yameki",
    "close": "terumi",
    "come": "nokari",
    "go": "miruki",
    "stay": "pikuri",
    "leave": "sorami",
    "arrive": "yemari",
    "begin": "kiruki",
    "end": "tetori",
    "live": "nosari",
    "die": "yorumi",
    "laugh": "hikori",
    "cry": "chirami",
    "smile": "fumuri",
    "bloom": "yamaki",
    "grow": "terori",
    "shine": "nokumi",
    "sparkle": "mirari",
    "wish": "pikori",
    "hope": "soruki",
    "dream": "yemari",
    "protect": "kiromi",
    "fight": "tetori",
    "win": "nosuki",
    "lose": "yorari",
    
    # Adjectives (all end in -ne)
    "beautiful": "yamane",
    "pretty": "terune",
    "cute": "nokane",
    "good": "chirune",
    "bad": "fumane",
    "big": "hikone",
    "small": "porane",
    "long": "mirane",
    "short": "sorune",
    "tall": "yemane",
    "low": "kirane",
    "wide": "tetone",
    "narrow": "nosune",
    "thick": "yorane",
    "thin": "pikune",
    "heavy": "zamane",
    "light": "terune",
    "strong": "nokune",
    "weak": "hikane",
    "fast": "chirane",
    "slow": "fumone",
    "hot": "yamune",
    "cold": "pokane",
    "warm": "mirone",
    "cool": "sorune",
    "new": "yemane",
    "old": "kirone",
    "young": "tetune",
    "happy": "nosane",
    "sad": "yorune",
    "angry": "hikone",
    "scared": "pirane",
    "brave": "terune",
    "gentle": "nokane",
    "kind": "yamone",
    "cruel": "chirune",
    "bright": "fumane",
    "dark": "mirane",
    "clean": "pokune",
    "dirty": "sorane",
    "sweet": "yemane",
    "bitter": "kirane",
    "delicious": "tetone",
    "precious": "nosune",
    "important": "yorane",
    "wonderful": "hikune",
    "amazing": "pikane",
    "soft": "zamune",
    "hard": "terune",
    "smooth": "nokane",
    "rough": "mirone",
    
    # Pronouns 
    "i": "zima",
    "you": "reka",
    "he": "moro",
    "she": "tena",
    "we": "piku",
    "they": "yona",
    "this": "sora",
    "that": "kima",
    "who": "vero",
    "what": "noka",
    "where": "hiru",
    "when": "tema",
    "why": "yaso",
    "how": "fune",
}

# ============================================================
# 2. GRAMMAR RULES (INVENTED)
# ============================================================

GRAMMAR_RULES = {
    "plural": "ko",
    "past": "ta",
    "present": "ru",
    "future": "ma",
    "adjective": "ne",
    "adverb": "to",
}

# ============================================================
# 3. PHONETIC PATTERN GENERATOR
# ============================================================
class YumekoGenerator: 
    """ Generate new words based on YUMEKO phonetic patterns """

    CONSONANTS = ['k', 's', 't', 'n', 'h', 'm', 'y', 'r', 'w', 
                  'p', 'z', 'ch', 'f']
    VOWELS = ['a', 'i', 'u', 'e', 'o']
    
    @staticmethod
    def generate_noun():
        """Generate japanese-style noun"""
        c1= random.choice(YumekoGenerator.CONSONANTS)
        v1= random.choice(YumekoGenerator.VOWELS)
        c2= random.choice(YumekoGenerator.CONSONANTS)
        v2= random.choice(YumekoGenerator.VOWELS)
        ending = random.choice(['a', 'o', 'ka', 'no', 'ma'])
        return f"{c1}{v1}{c2}{v2}{ending}"
    
    @staticmethod
    def generate_verb():
        """Generate japanese-style verb ending with -ri"""
        c1= random.choice(YumekoGenerator.CONSONANTS)
        v1= random.choice(YumekoGenerator.VOWELS)
        c2= random.choice(YumekoGenerator.CONSONANTS)
        v2= random.choice(YumekoGenerator.VOWELS)
        return f"{c1}{v1}{c2}{v2}ri"
    
    @staticmethod
    def generate_adjective():
        """Generate japanese-style adjective ending with -ne"""
        c1= random.choice(YumekoGenerator.CONSONANTS)
        v1= random.choice(YumekoGenerator.VOWELS)
        c2= random.choice(YumekoGenerator.CONSONANTS)
        v2= random.choice(YumekoGenerator.VOWELS)
        return f"{c1}{v1}{c2}{v2}ne"
    
# ============================================================
# 4. ADVANCED TRANSLATOR
# ============================================================

class YumekoTranslator:
    """Bidirectional English ↔ Yumiko translator with grammar"""

    def __init__(self):
        self.en_to_yu = YUMEKO_DICT
        self.yu_to_en = {v: k for k, v in YUMEKO_DICT.items()}

    def translate_to_yumeko(self, text):
        """English → Yumiko with grammar rules"""
        words = text.lower().split()
        translated = []

        for i, word in enumerate(words):
            if word.endswith('s') and word[:-1] in self.en_to_yu:
                base= self.en_to_yu[word[:-1]]
                translated.append(base + 'ko')
            elif word.endswith('ed') and word[:-2] in self.en_to_yu:
                base = self.en_to_yu[word[:-2]]
                if base.endswith('ri'):
                    translated.append(base[:-2] + 'ta')
            elif word in self.en_to_yu:
                translated.append(self.en_to_yu[word])
            else:
                translated.append(f"[{word}]")
                
        return ' '.join(translated)


    def translate_to_english(self, text):
        """Yumiko → English"""
        words = text.lower().split()
        translated = []

        for word in words:
            if word.endswith('ko') and word[:-2] in self.yu_to_en:
                translated.append(self.yu_to_en[word[:-2]] + 's')
            elif word.endswith('ta') and word[:-2] + 'ri' in self.yu_to_en:
                translated.append(self.yu_to_en[word[:-2] + 'ri'] + 'ed')
            elif word.endswith('ru') and word[:-2] + 'ri' in self.yu_to_en:
                translated.append(self.yu_to_en[word[:-2] + 'ri'] + 's')
            elif word in self.yu_to_en:
                translated.append(self.yu_to_en[word])
            else:
                translated.append(f"[{word}]")
                
        return ' '.join(translated)


    def analyze_grammar(self, yumeko_text): 
        """Analyze grammar of a Yumiko sentence"""
        words = yumeko_text.split()
        analysis = []

        for word in words:
            if word in self.yu_to_en:
                base= self.yu_to_en[word]
                if word.endswith ('a') or word.endswith('o'):
                    analysis.append(f"{word} (noun: {base})")
                elif word.endswith('ri'):
                    analysis.append(f"{word} (verb: {base})")
                elif word.endswith('ne'):
                    analysis.append(f"{word} (adjective: {base})")
                else:
                    analysis.append(f"{word} (pronoun: {base})")
            elif word.endswith('ko'):
                analysis.append(f"{word} (plural noun)")
            elif word.endswith('ta'):
                analysis.append(f"{word} (verb past tense)")
            elif word.endswith('ru'):
                analysis.append(f"{word} (verb present tense)")
            else:
                analysis.append(f"{word} (unknown)")
        
        return '\n'.join(analysis)
    
    # ============================================================
    # 5. INTERACTIVE DEMO
    # ============================================================

def main():
    translator= YumekoTranslator()
    generator = YumekoGenerator()

    print("="*60)
    print("🌸 YUMEKO LANGUAGE - Constructed Language Demo 🌸")
    print("="*60)
    print("\nFeatures:")
    print("  1. English → Yumeko translation")
    print("  2. Yumeko → English translation")
    print("  3. Grammar analysis")
    print("  4. Random word generator")
    print("\nType 'quit' to exit\n")

    while True:
       print("\n + "+"-"*60)
       choice = input("Choose mode (1/2/3/4) or 'quit': ").strip().lower()

       if choice == 'quit':
              print("\n Goodbye! 🌸")
              break
       if choice == '1':
           text = input("\nEnter English text: ")
           result = translator.translate_to_yumeko(text)
           print(f"Yumeko: {result}")

       elif choice == '2':
           text = input("\nEnter Yumeko text: ")
           result = translator.translate_to_english(text)
           print(f"English: {result}")

       elif choice == '3':
           text = input("\nEnter Yumeko text to analyze: ")
           analysis = translator.analyze_grammar(text)
           print(f"Grammar Analysis:\n{analysis}")  
 
       elif choice == '4':
            print("\nGenerated words:")
            print(f"  Noun: {generator.generate_noun()}")
            print(f"  Verb: {generator.generate_verb()}")
            print(f"  Adjective: {generator.generate_adjective()}")
        
       else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()