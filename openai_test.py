from openai import OpenAI

client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
        },
        {
            "role": "user",
            "content": "Compose a poem that explains the concept of recursion in programming.",
        },
    ],
)

# print("👀", completion)
# # 👀 ChatCompletion(id='chatcmpl-9Xu95extNkaXCGZEjHELThNJN7Nl1', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content="In the realm of code where mysteries dwell,\nThere lies a technique that weaves a spell,\nRecursion its name, a concept profound,\nCreating solutions where elegance is found.\n\nLike a mirror reflecting its own reflection,\nRecursion calls upon itself for direction,\nBreaking problems into smaller pieces,\nUntil the answer finally releases.\n\nA function calls upon itself, you see,\nTo solve a task with grace and glee,\nEach nested call a journey deep,\nInto the problem's core, it peeps.\n\nA Fibonacci sequence, a tree so grand,\nRecursive functions lend a helping hand,\nSolving puzzles with recursive might,\nBringing clarity in the darkest night.\n\nBut beware, dear coder, tread with care,\nRecursive depths can lead to a snare,\nStack overflow, an ominous fate,\nWhen recursive calls become too great.\n\nSo wield recursion like a subtle art,\nUnraveling complexities, a work of heart,\nIn the poetic dance of code and thought,\nLet recursion be the magic you have sought.", role='assistant', function_call=None, tool_calls=None))], created=1717867675, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=201, prompt_tokens=39, total_tokens=240))

print(completion.choices[0].message)

# python openai_test.py

# ChatCompletionMessage(content="In the realm of code where mysteries dwell,\nThere lies a technique that weaves a spell,\nRecursion its name, a concept profound,\nCreating solutions where elegance is found.\n\nLike a mirror reflecting its own reflection,\nRecursion calls upon itself for direction,\nBreaking problems into smaller pieces,\nUntil the answer finally releases.\n\nA function calls upon itself, you see,\nTo solve a task with grace and glee,\nEach nested call a journey deep,\nInto the problem's core, it peeps.\n\nA Fibonacci sequence, a tree so grand,\nRecursive functions lend a helping hand,\nSolving puzzles with recursive might,\nBringing clarity in the darkest night.\n\nBut beware, dear coder, tread with care,\nRecursive depths can lead to a snare,\nStack overflow, an ominous fate,\nWhen recursive calls become too great.\n\nSo wield recursion like a subtle art,\nUnraveling complexities, a work of heart,\nIn the poetic dance of code and thought,\nLet recursion be the magic you have sought.", role='assistant', function_call=None, tool_calls=None)
