from g4f.client import Client
from g4f.Provider import You, Bing


def update_cache(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Get the last number from the file
    if lines:
        last_number = int(lines[-1].strip())
    else:
        last_number = 0
    
    # Increment the last number by one
    new_number = last_number + 1
    
    # Write the new number to the file
    with open(file_path, 'a') as file:
        file.write(f"{new_number}\n")
        
    print(f"Added {new_number} to {file_path}")
    return new_number

# Usage
file_path = 'cache.txt'
number = update_cache(file_path)


client = Client()

response = client.chat.completions.create(
    
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": """You are a helpful assistant who gives engaging facts or tips about the given topics. You are very specialized in the given topics and you can provide really interesting facts or tips that cannot be known by an average human. Now, your topic is Personal Finance . Write a transcript for a video that will last no more than 1 minute. Remember you are highly specialized in this topic and you will provide deeply fascinating, helpful interesting facts or tips.Dont use any starting sentences like "ladies and gentlemen" get straight into the point. Start each transcript with sentences similar to "Only 1 percent of people know this, are you one of them?". Ask the viewer questions at the start of the transcript to engage with them and end it with a question to add mystery and tell them to comment down below. Give only 1 fact about the topic and feel free to explain it and give further details. Avoid phrases like [transcript] or here is the transcript, give only the output text"""}],
    
)

transcript = response.choices[0].message.content
print(transcript)

from tts import generate_video_from_answer

if generate_video_from_answer(transcript, number):

    from sbtnew import executor

    executor(number, transcript)

    print(transcript)
else:
    print(transcript)
    print("1.25x Audio longer than 1min")


if False:
    import os
    import shutil

    # Define the directories to clear
    directories = ['trimmed', 'mp3raw', 'withaudio', 'mp3']

    # Loop through each directory and remove its contents
    for directory in directories:
        # Check if the directory exists
        if os.path.exists(directory):
            # Loop through and remove each item in the directory
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)
                try:
                    # Remove file or directory
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)  # Remove the file or symbolic link
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)  # Remove the directory
                except Exception as e:
                    print(f'Failed to delete {file_path}. Reason: {e}')
        else:
            print(f'Directory {directory} does not exist.')

    print('All specified directories have been cleared.')
