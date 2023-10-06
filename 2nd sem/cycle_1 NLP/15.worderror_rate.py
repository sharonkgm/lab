# Find The Word Error Rate (WER) of a Sentence

def word_error_rate(hypothesis, reference):
    hypothesis_words = hypothesis.lower().split()
    reference_words = reference.lower().split()

    common_words = set(hypothesis_words) & set(reference_words)
    
    wer = 1 - len(common_words) / len(reference_words)
    
    return wer

hypothesis = "Alice was beginning to get very tired of sitting by her sister on the bank."
reference = "Alice is beginning to get most tired of sitting by her sister in the bank."

wer = word_error_rate(hypothesis, reference)

print("Word Error Rate:", wer)
