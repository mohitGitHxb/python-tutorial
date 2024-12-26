import re
import string
import unidecode
import inflect
import textdistance
import Levenshtein
from fuzzywuzzy import fuzz
from slugify import slugify
import ftfy
import nltk

# Download NLTK resources (run once)
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

def comprehensive_string_manipulation_demo():
    # Original text for demonstration
    original_text = "Résumé for José - Advanced String Manipulation 123!"
    
    # 1. Regular Expressions (re)
    print("1. Regular Expressions:")
    numbers = re.findall(r'\d+', original_text)
    cleaned_text = re.sub(r'\d+', '', original_text)
    print("Numbers found:", numbers)
    print("Cleaned text:", cleaned_text)
    
    # 2. String Module Constants
    print("\n2. String Module:")
    print("ASCII Letters:", string.ascii_letters[:10])
    print("Digits:", string.digits)
    print("Punctuation:", string.punctuation[:5])
    
    # 3. Unicode Transliteration (unidecode)
    print("\n3. Unicode Transliteration:")
    ascii_text = unidecode.unidecode(original_text)
    print("Transliterated:", ascii_text)
    
    # 4. Inflect (Linguistic Manipulation)
    print("\n4. Linguistic Manipulation:")
    p = inflect.engine()
    print("Plural of 'child':", p.plural('child'))
    print("Ordinal of 3:", p.ordinal(3))
    
    # 5. Text Distance Calculation
    print("\n5. Text Distance:")
    print("Levenshtein Distance:", 
          textdistance.levenshtein.distance('hello', 'hallo'))
    print("Jaccard Similarity:", 
          textdistance.jaccard.similarity('hello', 'hallo'))
    
    # 6. Levenshtein Quick Calculations
    print("\n6. Levenshtein Calculations:")
    print("Distance:", Levenshtein.distance('hello', 'hallo'))
    print("Similarity Ratio:", Levenshtein.ratio('hello', 'hallo'))
    
    # 7. Fuzzy String Matching
    print("\n7. Fuzzy String Matching:")
    print("Fuzzy Ratio:", fuzz.ratio('hello world', 'hello wold'))
    print("Partial Ratio:", fuzz.partial_ratio('hello world', 'world'))
    
    # 8. Slugify (URL-friendly Conversion)
    print("\n8. URL-friendly Conversion:")
    url_friendly = slugify(original_text)
    print("Slugified:", url_friendly)
    
    # 9. Unicode Fixing
    print("\n9. Unicode Fixing:")
    broken_text = "MÃ¼ller"
    fixed_text = ftfy.fix_text(broken_text)
    print("Fixed Unicode:", fixed_text)
    
    # 10. NLTK Natural Language Processing
    print("\n10. Natural Language Processing:")
    tokens = nltk.word_tokenize(original_text)
    pos_tags = nltk.pos_tag(tokens)
    print("Tokens:", tokens)
    print("POS Tags:", pos_tags)
    
    # Bonus: Comprehensive Text Processing Function
    def advanced_text_processor(text):
        # Transliterate and clean
        ascii_text = unidecode.unidecode(text)
        cleaned_text = re.sub(r'[^a-zA-Z\s]', '', ascii_text)
        normalized_text = cleaned_text.lower().strip()
        
        return {
            'original': text,
            'ascii': ascii_text,
            'cleaned': cleaned_text,
            'normalized': normalized_text,
            'token_count': len(normalized_text.split()),
            'is_similar': fuzz.ratio(text.lower(), normalized_text) > 90
        }
    
    # Demonstrate advanced processor
    print("\n11. Advanced Text Processor:")
    processed = advanced_text_processor(original_text)
    for key, value in processed.items():
        print(f"{key.capitalize()}: {value}")

# Run the demonstration
if __name__ == "__main__":
    comprehensive_string_manipulation_demo()