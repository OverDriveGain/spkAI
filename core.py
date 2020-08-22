import torch
from transformers import BertForQuestionAnswering, BertTokenizer

model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

answerText = ''
# Take string as file content
def setAnswersFile(file):
    global answerText
    answerText = file
    return True


def answerQuestion(question):
    if(answerText == ''):
        print("Answers file not presented")
        return False
    inputIds = tokenizer.encode(question, answerText)
    tokens = tokenizer.convert_ids_to_tokens(inputIds)
    sepIndex = inputIds.index(tokenizer.sep_token_id)
    numSegA = sepIndex + 1
    numSegB = len(inputIds) - numSegA
    segmentIds = [0]*numSegA + [1]*numSegB
    assert len(segmentIds) == len(inputIds)
    # Run our example through the model.
    startScore, endScore = model(torch.tensor([inputIds]), # The tokens representing our input text.
                                 token_type_ids=torch.tensor([segmentIds])) # The segment IDs to differentiate question from answer_text
    answerStart = torch.argmax(startScore)
    answerEnd = torch.argmax(endScore)
    # Combine the tokens in the answer and print it out.
    answer = ' '.join(tokens[answerStart:answerEnd+1])

    print('Answer: "' + answer + '"')
    return True