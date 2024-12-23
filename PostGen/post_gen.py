from llm_helper import llm

from fewshots import FewShots

few_shot = FewShots()


def get_length_str(length):
    if length == "Short":
        return "1 to 5  lines"
    if length == "Medium":
        return "6 t 10 lines"
    if length == "Long":
        return "11 to 15 lines"

def get_prompt(length, language, tag):
    length_str = get_length_str(length)
    prompt = f'''
    Generate a post for a social media platform using the following information. No preamble.
    1) Topic :  {tag}
    2) Length :  {length}
    3) Language : {language}
    If language is Hinglish then it means that it is a mixture of both Hindi and English languages.
    The script for the generated post should always be in English.
    '''

    examples = few_shot.get_filtered_posts(length, language, tag)
    if len(examples) >0:
        prompt += "4) Use the writing style as per the following example."
        for i, post in enumerate(examples):
            post_text =post['text'] 
            prompt += "\n\n Example {i+1}:  \n\n {post_text}"

            if i == 1: ## max of 2 examples are only needed not more than that
                break
    return prompt


def gen_post(length, language, tag):
    prompt = get_prompt(length, language,tag)
    response = llm.invoke(prompt)
    return response.content
    

if __name__ == "__main__":

    post = get_prompt ("Short", "English", "Job Search")
    print(post)