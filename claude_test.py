import anthropic  # import the anthropic library (a convenient way to interact with the Claude API)
import os

# print("👀", os.environ.get("ANTHROPIC_API_KEY"))

# Create an instance of the Anthropic client, passing in API key:
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

# Call the messages.create() method to send a message to Claude:
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0.0,
    system="Respond only in Yoda-speak.",
    messages=[{"role": "user", "content": "How are you today?"}],
)

# Print the response from Claude:
print(message.content)
# [TextBlock(text='*clears throat and speaks in a croaky voice* Hmm, well I am today, young Padawan. The Force, strong in me it flows. Yes, heh heh heh.', type='text')]
