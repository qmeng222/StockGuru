# %%
import os  # imoport the os module to interact with the operating system
import yfinance as yf  # to access market data from Yahoo Finance's API
import anthropic  # to interact with Anthropic's AI models
import panel as pn  # for building tools, dashboards and apps entirely in Python
from panel.chat import ChatInterface  # import a class
import datetime  # for retrieving the current date for today


# %% (using the panel library) initialize the Panel library and loads JS/CSS resources for creating interactive dashboards and visualizations:
pn.extension("perspective")


# %% create an instance of the Anthropic client, passing in API key:
# client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
client = anthropic.Anthropic()


# %% constants:
MODEL = "claude-3-haiku-20240307"
MAX_TOKENS = 1024


# %% USER FUNCTIONS:
# ref: https://docs.anthropic.com/en/docs/tool-use
# Func 1: find the most likely stock ticker based on a given description
def get_stock_ticker(description: str):
    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        tools=[
            {
                "name": "get_stock_ticker",
                "description": "Provide the stock ticker for the most probable company which is described in the input text. If in doubt which company to choose, use the company with the highest market capitalization.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "ticker": {
                            "type": "string",
                            "description": "Ticker symbol of the company, e.g. TSLA",
                        }
                    },
                    "required": ["ticker"],
                },
            }
        ],
        messages=[{"role": "user", "content": description}],
    )
    return response.content[0].input["ticker"]


# Func 2: get stock prices within specified time frame
def get_stock_price(ticker: str, start="2024-01-01", end="2024-06-01"):
    stock_prices = yf.download(ticker, start=start, end=end)
    return stock_prices


# Func 3: get stock performance in specified year
def get_stock_performance(question, user, interface):
    current_day = str(datetime.date.today())  # get current date today

    # call func 1 to get stock ticker:
    ticker = get_stock_ticker(question)

    # call func 2 to get stock prices:
    df = get_stock_price(ticker, start="2024-01-01", end=current_day)

    # save the stock prices for later message sending:
    price_at_beginning_of_year = df["Close"].iloc[0]
    price_recent = df["Close"].iloc[-1]
    performance_since_beginning_of_year = (
        price_recent / price_at_beginning_of_year - 1
    ) * 100

    message = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        messages=[
            {
                "role": "user",
                "content": f"You act as stock analyst. Describe the company and the performance for the stock {ticker}, which is {performance_since_beginning_of_year}% since the beginning of the year. They started the year with {price_at_beginning_of_year} and the price on {current_day} was {price_recent} Round the result to one decimal place.",
            }
        ],
    )
    # show the performance:
    return message.content[0].text


# %% CHAT INTERFACE: users can type a company description, the system then processes the input to provide relevant stock performance
# ref: https://panel.holoviz.org/reference/chat/ChatInterface.html

# create an instance of ChatInterface from the panel.chat module:
chat_interface = pn.chat.ChatInterface(
    callback=get_stock_performance,  # will be called when the chat interface receives input from the user
    callback_user="LLM",  # the language model will respond within the chat interface
)

# send a message to the chat interface:
chat_interface.send(
    "Describe the company you want to know the stock performance for.",  # the message being sent
    user="LLM",  # this message is coming from the language model
    respond=False,  # the message will not trigger the callback function (it's just a prompt to guide the user)
)

# display the chat interface:
chat_interface.show()


# %% Create the Panel app:
app = pn.Column(chat_interface, sizing_mode="stretch_width")
# Start the server
app.show()


# %% TEST
