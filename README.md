# Zootopia - My Animal Search Tool 🐾

Hello! This is a Python project I built to explore the animal kingdom. Instead of just showing one result, this tool acts like a search engine for animals.

## What does this program do?

When you start the program by running `animals_web_generator.py`, it asks you to enter an animal name in English. 

The special thing about this tool is that it finds **all animals** related to your search term. For example, if you search for **"Fox"**, you won't just get one result. You will get a list of about 20 different animals, such as:
*   Arctic Fox
*   American Foxhound
*   Darwin's Fox
*   Kit Fox ... and many more!

The program fetches all these results from the **Ninja API** and creates a beautiful **HTML website** where all these animals are listed clearly with their specific details.

## Features & Details

For every animal found, the website displays:
*   **Name:** The specific breed or species name.
*   **Diet:** What they usually eat.
*   **Location:** Where in the world they can be found.
*   **Characteristics:** Unique features, skin type, lifespan, and more.

## How to use it

1.  **Run the script:** Start `animals_web_generator.py`.
2.  **Search:** Enter a name (e.g., "Fox" or "Cat") in the console.
3.  **View:** Open the generated HTML file in your browser to see your full report.

## Tech I used

*   **Python:** For the logic and handling the data.
*   **Requests Library:** To communicate with the Ninja API.
*   **HTML:** To build the visual report for the user.
*   **Dotenv:** To keep my private API Key safe.


