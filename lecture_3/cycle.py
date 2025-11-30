'''
name: str = "Ilya"


for i in range(10, 0, -1):

    print(

        f"Hello {name}! {i}"

    )
    
'''
print(

    list(range(0, 100))

)
print('~' * 21)

sentence: str = "Hello Bob! How are you?"

splitted_sentence: list[str] = sentence.split()  # type: ignore


for value in splitted_sentence:

    if len(value) == 3:

        print(f'We found {value=} with len={len(value)}')

