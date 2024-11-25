def average_word_length(sentence):
    
    cleaned_sentence = ''.join(char if char.isalnum() or char.isspace() else '' for char in sentence)
    
    words = cleaned_sentence.split()
    
    total_characters = sum(len(word) for word in words)
   
    avg_length = total_characters / len(words)
    return avg_length

def main():
    sentence1 = "Hi all, my name is Tom...I am originally from Australia."
    average_length = average_word_length(sentence1)
    print(f"The average word length is: {average_length:.2f}")

    
if __name__== "__main__":
    main()
    
    