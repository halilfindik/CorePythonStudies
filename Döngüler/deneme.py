import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="create a java program to run a basic blackjack game\n\n/**\n * This is a basic blackjack game.\n */\npublic class Blackjack {\n \n    public static void main(String[] args) {\n         \n        //Declare and initialize variables\n        int value = 0;\n        int player = 0;\n        int dealer = 0;\n        String input = \"\";\n        String winner = \"\";\n        boolean gameOver = false;\n         \n        //Create a scanner object for keyboard input\n        Scanner keyboard = new Scanner(System.in);\n         \n        //Welcome the player\n        System.out.println(\"Welcome to Blackjack!\");\n         \n        //Get the player's name\n        System.out.print(\"What is your name? \");\n        input = keyboard.nextLine();\n         \n        //Create the player object and pass it the player's name\n        Player p = new Player(input);\n         \n        //Create the dealer object\n        Dealer d = new Dealer();\n         \n        //Shuffle the deck\n        d.shuffleDeck();\n         \n        // Deal the cards\n        System.out.println(\"Dealing cards...\");\n        p.",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)