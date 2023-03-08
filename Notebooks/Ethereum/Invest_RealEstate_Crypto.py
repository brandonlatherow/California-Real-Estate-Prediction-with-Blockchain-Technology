
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
from crypto_wallet import generate_account, get_balance, send_transaction

# Updated the port number to 8545 from 7545 in order to ensure the connection to Ganache for transactions
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:8545"))

################################################################################
#Real Estate Investment Options

# Database of KryptoJobs2Go candidates including their name, digital address, rating and hourly cost per Ether.
property_database = {
    "Property 1": [
        "Cali 1",
        "0x507BFb01f2F2e73f428C197bF3059AaC8ef73caf",
        "1000",
        0.50,
        "Images/california_beach2.jpeg",
    ],
    "Property 2": [
        "Cali 2",
        "0x0cfCfac45FEcEcbCAF8Fb78D257041Cbb7F6Ca41",
        "1500",
        1.00,
        "Images/california_beach3.jpeg",
    ],
    "Property 3": [
        "Cali 3",
        "0x58AcEf7b776A19Eb5536f5c7D189c73bbaF6d313",
        "2000",
        1.50,
        "Images/california_beach4.jpeg",
    ]
}

# A list of the Properties
property = ["Cali 1", "Cali 2", "Cali 3"]

def get_property():
    """Display the database of Property Investment information."""
    db_list = list(property_database.values())

    for number in range(len(property)):
        st.image(db_list[number][3], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("Property Square ft: ", db_list[number][2])
        st.write("Investment Starting Value: ", db_list[number][3], "eth")
        st.text(" \n")


################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# Invest in California Real Estate")
st.markdown("## Using Ethereum, Decide How Much You Will Invest")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

##########################################

#  Call the `generate_account` function and save it as the variable `account`
account = generate_account()

# ##########################################

# # Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

# ##########################################

# # Call `get_balance` function and pass it your account address
# # Write the returned ether balance to the sidebar
st.sidebar.write(get_balance(w3,account.address))

##########################################

# # Create a select box to chose a Property to Invest
property = st.sidebar.selectbox("Select a Property", property)

# Create a input field to record the square feet you want to invest
#hours = st.sidebar.number_input("Square Foot Investment")

st.sidebar.markdown("## Property Name, Square Foot, and Ethereum Address")

# Identify the Property
Cali = property_database[property][0]

# Write the Property name to the sidebar
st.sidebar.write(property)

# Identify the Property Square Foot
sq_ft = property_database[property][3]

# Write the Square Foot to the sidebar
st.sidebar.write(sq_ft)

# Identify the Property Ethereum Address
property_address = property_database[property][1]

# Write the Property's Ethereum Address to the sidebar
st.sidebar.write(property_address)

# Write the Property's name to the sidebar

st.sidebar.markdown("## Total Wage in Ether")

################################################################################

# Calculate total `Investment` for the property
# rate from the candidate database (`candidate_database[person][3]`) by the
# value of the `hours` variable
#investment = hours * hourly_rate

# # Write the `investment` calculation to the Streamlit sidebar
#st.sidebar.write(investment)

##########################################

if st.sidebar.button("Send Transaction"):

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(send_transaction(w3, account, property_address, wage))

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes Properties to the Streamlit page
get_property()

################################################################################
