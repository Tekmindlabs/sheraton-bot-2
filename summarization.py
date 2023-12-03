import cohere
import streamlit as st
import os
import requests
import webbrowser
from bs4 import BeautifulSoup

#co = cohere.Client(os.environ["COHERE_API_KEY"]) 
def formattingForSummarizer(text):
    # ... existing code ...

def summarizer(text):
    CleanText = formattingForSummarizer(str(text))
    summarizer_prompt = "You are a customer service representative at MyVitaminStore.pk, summarize the product details for a customer inquiry:"

    response = co.summarize( 
          text=CleanText,
          length='long',
          format='bullets',
          model='summarize-xlarge',
          additional_command=summarizer_prompt,
          temperature=0.3,
        ) 
    print(response.summary)
    return response.summary

# ... rest of the code remains unchanged ...

def generateKBase(largeData):

    rqdFormat =  [
        {
        "title": " ",
        "snippet": " "
        },
    ]
    FormatPrompt = "You should extract the given details text: " + largeData +" into this  \n: "+ " "+ str(rqdFormat) + "\n JSON FORMAT and populate the corresponding values from text : The snippet can contain the large amount of tokens.Don't shortent the content" 
    response = co.generate(
        # text,
        model='command-nightly',
        prompt=FormatPrompt,
        temperature=0.3,
        return_likelihoods =  None,
        # finish_reason= COMPLETE,
        # token_likelihoods= None,
    )
    print(response.generations[0].text)
    # sendAPIReg(response.generations[0].text)




def main():
    text = """The customer wants to book a 1-bedroom suite for 2 days
The check-in date is from 13th September
The suite costs ₹12600 and comes with a king bed, executive lounge access, a shower/tub combination, and amenities like high-speed internet and 2 TVs.
Nothing was mentioned about extras."""

    # generateKBase(data)
    # generateDetails(text)

# Add the summary
if __name__ == "__main__":
    main()

