
# The Insta Coach
Get instant selfie coaching from Kylie J.

Check my other projects, visit [Dries Depoorter](https://driesdepoorter.be).
I'm an artist combining art and technology. Follow me also on [Instagram](https://instagram.com/driesdepoorter) and [X](https://twitter.com/driesdepoorter).

This project combines 2 APIs: OpenAI GPT-4 vision preview and ElevenLabs.

This project requires the creation of a virtual environment to manage dependencies in isolation. Additionally, you need to provide API keys for OpenAI and ElevenLabs. These keys should be stored in a `.env` file at the root of the project for security reasons.

## Setting Up the Virtual Environment

To create a virtual environment, run the following command in the root directory of this project:

```bash
python3 -m venv venv
```

This command creates a new directory named `venv`, where the virtual environment will be stored. To activate the virtual environment, use the following command:

- On Windows:
```cmd
.\venv\Scripts\activate
```

- On macOS and Linux:
```bash
source venv/bin/activate
```

## Configuring the .env File

Create a `.env` file in the root directory of the project and fill in your OpenAI and ElevenLabs API keys as follows:

```env
ELEVENLABS_API_KEY=""
OPENAI_KEY=""
```

Replace `OPENAI_KEY` and `ELEVENLABS_API_KEY` with your actual API keys. This .env file will be ignored by Git if you've correctly set up your `.gitignore` file as advised.

## Final Steps

After setting up the virtual environment and configuring the `.env` file with your API keys, you're ready to proceed with the project setup and execution as per the project documentation.

Ensure you have pip installed and then run the following command to install all required packages:

```bash
pip3 install -r requirements.txt
```

Finally, you can run the project using:

```bash
python3 main.py
```
