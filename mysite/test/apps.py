from django.apps import AppConfig
import html
import pathlib
import os

class TestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test'




from transformers import BertTokenizerFast, GPT2LMHeadModel
import torch
class WebappConfig(AppConfig):
    def __init__(self):
        self.model = GPT2LMHeadModel.from_pretrained('C:\\Users\\이종헌\\Desktop\\Django\\projects\\mysite\\test\\model_save')
        self.tokenizer_gpt3 = BertTokenizerFast.from_pretrained("kykim/gpt3-kor-small_based_on_gpt2",
                                                           bos_token='<|startoftext|>',
                                                           eos_token='<|endoftext|>',
                                                           pad_token='<|pad|>')
        self.input_ids = self.tokenizer_gpt3.encode("text to tokenize")[1:]  # CLS token 제거

        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        self.model.eval()

    def coverletter_generator(self,text):
        prompt = f"<|startoftext|> {text}"
        generated = torch.tensor(self.tokenizer_gpt3.encode(prompt)[1:]).unsqueeze(0)
        generated = generated.to(self.device)

        sample_outputs = self.model.generate(
            generated,
            do_sample=True,
            top_k=50,
            max_length=500,
            top_p=0.95,
            num_return_sequences=3,
            repetition_penalty=1.1
        )
        new_array = {}
        for i, sample_output in enumerate(sample_outputs):
            result = "{}: {}\n\n".format(i, self.tokenizer_gpt3.decode(sample_output, skip_special_tokens=True))
            name = '생성문'+str(i+1)
            new_array[name] = result
            # print(result)
        return new_array
