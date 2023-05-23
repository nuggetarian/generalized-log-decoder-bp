import time
import transformers
from time import perf_counter
from transformers import AutoTokenizer, TFAutoModelForQuestionAnswering, pipeline
import torch
import tensorflow as tf

class NeuralNetwork:
    # def getCurrentGpu():
    #     print('Currently used device id: {}'.format(torch.cuda.current_device()))
    #     print('Currently used device name: {}'.format(torch.cuda.get_device_name(torch.cuda.current_device())))

    # def setCudaDevice(gpuid):
    #     try:
    #         torch.cuda.set_device(gpuid)
    #         device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    #         n_gpu = torch.cuda.device_count()

    #     except RuntimeError as e:
    #         raise SystemError('Is not able to set a GPU device')
    
    test_model = TFAutoModelForQuestionAnswering.from_pretrained("modules\\model")
    test_tokenizer = AutoTokenizer.from_pretrained("modules\\model")
    question_answerer = pipeline("question-answering", model=test_model, tokenizer=test_tokenizer, device=0, device_map="auto")

   
    # setCudaDevice(0)  
    torch.device("cuda" if torch.cuda.is_available() else "cpu")   
    def predict(self, log):
        question = [#"When did the event happen?", 
                "What is the level of log?", 
                #"What is the eventid?",
                #"Which event channel is the source?",
                #"What is the name of the host origin?",
                #"What is the host's domain name?",
                #"Which user is the origin of the event?",
                #"What is the identification number of the origin user?",
                #"Which user is the target of the event?",
                #"What is the identification number of the target user?",
                #"Which process is involved?",
                #"What is PID of responsible process?",
                #"Which logon type was used?",
                #"What is the message of the event?",
                #'Which operation or task was provided?',
                #'Which process is a provider of event information?',
                #"Which command was used?","What is domain suffix?",
                #"What is IP address of DNS server?",
                #"Which IP address is origin of the DNS event?"
            ]
        
        counter=1

        for q in question:
            start = perf_counter()
            result = self.question_answerer(question=q, context=log)
            end = perf_counter()
            time = format(round((end - start)*1000))
            print(str(counter) + '. Question: ' + q + '\nAnswer: ' + result['answer'] + '\nScore: ' + str(result['score']) + '\nExecution time [ms]: ' + str(time) + '\n')
            counter+=1
    
    
    
    
    
