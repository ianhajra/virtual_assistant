import pytest
from nlp.text_processing import normalize, tokenize, remove_stop_words, lemmatize, process_command

# normalize text by converting it to lowercase
def test_normalize():
    assert normalize("Hello, World!") == "hello, world!"
    assert normalize("weIrD InPUt") == "weird input"
    assert normalize("ALL CAPS INPUT") == "all caps input"
    assert normalize("all lowercase input") == "all lowercase input"
    assert normalize("572983758923789327") == "572983758923789327"
    assert normalize("@%^&^$#") == "@%^&^$#"
    assert normalize("HELLO") == "hello"
    assert normalize("HeLLo WoRLd") == "hello world"
    assert normalize("123ABCdef") == "123abcdef"
    assert normalize("!@#$%^&*()_+{}:<>? ABCD") == "!@#$%^&*()_+{}:<>? abcd"
    assert normalize("ÀÉÎÕÛ") == "àéîõû"
    assert normalize("") == ""
    assert normalize("Hello\nWorld") == "hello\nworld"
    assert normalize("Hello\tWorld") == "hello\tworld"
    assert normalize("  HeLLo  WoRLd  ") == "  hello  world  "
    assert normalize("你好世界HELLO") == "你好世界hello"
    assert normalize("THIS IS A TEST") == "this is a test"
    assert normalize("python CODE") == "python code"
    assert normalize("12345") == "12345"
    assert normalize("MixedCASE123") == "mixedcase123"
    assert normalize("Leading and Trailing Spaces    ") == "leading and trailing spaces    "
    assert normalize("    ALL SPACES IN FRONT") == "    all spaces in front"
    assert normalize("SpecialCharacters!@#") == "specialcharacters!@#"
    assert normalize("CamelCaseWord") == "camelcaseword"
    assert normalize("UPPERCASE123lower") == "uppercase123lower"
    assert normalize("numbers1234567890") == "numbers1234567890"
    assert normalize("    SPACES everywhere  ") == "    spaces everywhere  "
    assert normalize("String with Tabs\t and Newlines\n") == "string with tabs\t and newlines\n"
    assert normalize("UPPER AND lower") == "upper and lower"
    assert normalize("123 Mixed Upper LOWER!") == "123 mixed upper lower!"
    assert normalize("Ümläüts ShÖuld BE lowER") == "ümläüts shöuld be lower"
    assert normalize("LONG STRING OF TEXT TO TEST THE FUNCTION") == "long string of text to test the function"
    assert normalize("SPACES\tTABS\nNEWLINES") == "spaces\ttabs\nnewlines"
    assert normalize("PYTHON\tROCKS") == "python\trocks"
    assert normalize("TextWith123AndSymbols!@#") == "textwith123andsymbols!@#"
    assert normalize("lowercase remains unchanged") == "lowercase remains unchanged"

# tokenize the text, splitting it into individual words or tokens
def test_tokenize():
    assert tokenize("Hello, World!") == ["hello", "world"]
    assert tokenize("Hello World") == ["Hello", "World"]
    assert tokenize("  Leading spaces") == ["Leading", "spaces"]
    assert tokenize("Trailing spaces  ") == ["Trailing", "spaces"]
    assert tokenize("Multiple   spaces") == ["Multiple", "spaces"]
    assert tokenize("Tabs\tand\tspaces") == ["Tabs", "and", "spaces"]
    assert tokenize("Newlines\nin\ntext") == ["Newlines", "in", "text"]
    assert tokenize("Mixed\n \tspaces") == ["Mixed", "spaces"]
    assert tokenize("Words123 with numbers") == ["Words123", "with", "numbers"]
    assert tokenize("Special!@# characters") == ["Special!@#", "characters"]
    assert tokenize("CamelCase words") == ["CamelCase", "words"]
    assert tokenize("UPPER lower CASE") == ["UPPER", "lower", "CASE"]
    assert tokenize("12345 Numbers") == ["12345", "Numbers"]
    assert tokenize("    Leading multiple spaces") == ["Leading", "multiple", "spaces"]
    assert tokenize("Trailing multiple spaces    ") == ["Trailing", "multiple", "spaces"]
    assert tokenize("\tTabs at the start") == ["Tabs", "at", "the", "start"]
    assert tokenize("End with tabs\t") == ["End", "with", "tabs"]
    assert tokenize("\nNewlines at start") == ["Newlines", "at", "start"]
    assert tokenize("End with newlines\n") == ["End", "with", "newlines"]
    assert tokenize("Mixed whitespace \t\n characters") == ["Mixed", "whitespace", "characters"]
    assert tokenize("SingleWord") == ["SingleWord"]
    assert tokenize("Two words") == ["Two", "words"]
    assert tokenize("Three words here") == ["Three", "words", "here"]
    assert tokenize("A sentence with punctuation!") == ["A", "sentence", "with", "punctuation!"]
    assert tokenize("   Mixed leading and  trailing   ") == ["Mixed", "leading", "and", "trailing"]
    assert tokenize("") == []
    assert tokenize(" ") == []
    assert tokenize("\t") == []
    assert tokenize("\n") == []
    assert tokenize("Words-with-hyphens") == ["Words-with-hyphens"]
    assert tokenize("Words_with_underscores") == ["Words_with_underscores"]

# remove common stop words from a list of tokens
# (e.g., "and", "the", "is", etc.)
def test_remove_stop_words():
    assert remove_stop_words(["hello", "and", "world"]) == ["hello", "world"]
    assert remove_stop_words(["this", "is", "a", "test"]) == ["test"]
    assert remove_stop_words(["the", "quick", "brown", "fox"]) == ["quick", "brown", "fox"]
    assert remove_stop_words(["jumped", "over", "the", "lazy", "dog"]) == ["jumped", "lazy", "dog"]
    assert remove_stop_words(["a", "and", "the", "in"]) == []
    assert remove_stop_words(["and", "the", "cat", "in", "the", "hat"]) == ["cat", "hat"]
    assert remove_stop_words(["running", "and", "jumping"]) == ["running", "jumping"]
    assert remove_stop_words(["this", "sentence", "has", "no", "stop", "words"]) == ["sentence", "stop", "words"]
    assert remove_stop_words(["all", "stop", "words", "like", "and", "the", "removed"]) == ["stop", "words", "removed"]
    assert remove_stop_words(["stopwords", "removed", "properly"]) == ["stopwords", "removed", "properly"]
    assert remove_stop_words(["the", "words", "in", "this", "sentence", "remain"]) == ["words", "sentence", "remain"]
    assert remove_stop_words(["a", "story", "with", "no", "end"]) == ["story", "end"]
    assert remove_stop_words(["stop", "words", "will", "be", "gone"]) == ["stop", "words", "gone"]
    assert remove_stop_words(["example", "with", "mixed", "stop", "words"]) == ["example", "mixed", "stop", "words"]
    assert remove_stop_words(["an", "array", "with", "no", "stops"]) == ["array", "stops"]
    assert remove_stop_words(["no", "stop", "words", "here"]) == ["stop", "words"]
    assert remove_stop_words(["keeping", "all", "useful", "words"]) == ["keeping", "useful", "words"]
    assert remove_stop_words(["every", "word", "matters", "here"]) == ["word", "matters"]
    assert remove_stop_words(["no", "removal", "necessary"]) == ["removal", "necessary"]
    assert remove_stop_words(["keep", "the", "essentials"]) == ["keep", "essentials"]
    assert remove_stop_words(["only", "important", "words", "remain"]) == ["important", "words"]
    assert remove_stop_words(["ignore", "the", "small", "words"]) == ["ignore", "small", "words"]
    assert remove_stop_words(["all", "stop", "words", "gone"]) == ["stop", "words", "gone"]
    assert remove_stop_words(["this", "is", "completely", "filtered"]) == ["completely", "filtered"]
    assert remove_stop_words(["words", "with", "meaning"]) == ["words", "meaning"]
    assert remove_stop_words(["all", "words", "kept"]) == ["words", "kept"]
    assert remove_stop_words(["no", "removal"]) == ["removal"]
    assert remove_stop_words(["everything", "is", "useful"]) == ["everything", "useful"]
    assert remove_stop_words(["every", "word", "is", "important"]) == ["word", "important"]
    assert remove_stop_words(["no", "stop", "words"]) == ["stop", "words"]
    assert remove_stop_words(["keeps", "important", "content"]) == ["keeps", "important", "content"]
    assert remove_stop_words(["ignores", "useless", "terms"]) == ["ignores", "useless", "terms"]


# lemmatize tokens, reducing words to their base or root form
# (e.g., "running" to "run", "jumps" to "jump")
def test_lemmatize():
    assert lemmatize(["running", "jumps"]) == ["run", "jump"]
    assert lemmatize(["running", "jumps", "easily"]) == ["run", "jump", "easily"]
    assert lemmatize(["better", "cats", "studies"]) == ["good", "cat", "study"]
    assert lemmatize(["children", "feet", "teeth"]) == ["child", "foot", "tooth"]
    assert lemmatize(["wolves", "buses", "geese"]) == ["wolf", "bus", "goose"]
    assert lemmatize(["thinking", "going", "singing"]) == ["think", "go", "sing"]
    assert lemmatize(["flying", "cars", "do"]) == ["fly", "car", "do"]
    assert lemmatize(["flies", "ran", "drives"]) == ["fly", "run", "drive"]
    assert lemmatize(["played", "doing", "sitting"]) == ["play", "do", "sit"]
    assert lemmatize(["quickly", "slower", "happiest"]) == ["quickly", "slow", "happy"]
    assert lemmatize(["driving", "eaten", "gone"]) == ["drive", "eat", "go"]
    assert lemmatize(["wrote", "writing", "writers"]) == ["write", "write", "writer"]
    assert lemmatize(["better", "worse", "more"]) == ["good", "bad", "more"]
    assert lemmatize(["swimming", "dancing", "dreaming"]) == ["swim", "dance", "dream"]
    assert lemmatize(["thieves", "knives", "wives"]) == ["thief", "knife", "wife"]
    assert lemmatize(["happier", "loveliest", "saddest"]) == ["happy", "lovely", "sad"]
    assert lemmatize(["mice", "men", "children"]) == ["mouse", "man", "child"]
    assert lemmatize(["faster", "strongest", "cleverest"]) == ["fast", "strong", "clever"]
    assert lemmatize(["cities", "babies", "puppies"]) == ["city", "baby", "puppy"]
    assert lemmatize(["saw", "seen", "seeing"]) == ["see", "see", "see"]
    assert lemmatize(["bought", "baking", "baker"]) == ["buy", "bake", "baker"]
    assert lemmatize(["happily", "quickly", "softly"]) == ["happily", "quickly", "softly"]
    assert lemmatize(["calves", "hooves", "leaves"]) == ["calf", "hoof", "leaf"]
    assert lemmatize(["fishing", "hunters", "traveled"]) == ["fish", "hunter", "travel"]
    assert lemmatize(["leafs", "beliefs", "chiefs"]) == ["leaf", "belief", "chief"]
    assert lemmatize(["matches", "kisses", "bosses"]) == ["match", "kiss", "boss"]
    assert lemmatize(["doing", "making", "created"]) == ["do", "make", "create"]
    assert lemmatize(["tries", "tries", "tried"]) == ["try", "try", "try"]
    assert lemmatize(["caring", "hating", "loving"]) == ["care", "hate", "love"]
    assert lemmatize(["jumps", "jumping", "jumped"]) == ["jump", "jump", "jump"]
    assert lemmatize(["easier", "easiest", "easily"]) == ["easy", "easy", "easily"]
