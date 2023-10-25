import os
import subprocess 

translator_command = (
    'python -m manga_translator -v --mode batch --translator-chain '
    '"google:CHS;google:ENG" -i "{input_folder}" -o "{output_folder}" --font-size '
    '35 --manga2eng --save-text-file "{output_folder}" --font-path "{font_path}" '
    '--save-quality 100 -f jpg'
)

def process_folder(numbers,base_folder,outputs_folder,font_paths):
    input_folders = base_folder.format(numbers)
    output_folders = outputs_folder.format(numbers)
    print(input_folders,"input_folder")
    print(output_folders,"output_folder_path")
    command = translator_command.format(
        input_folder=input_folders, output_folder=output_folders, font_path=font_paths
    )

    try:
        if(subprocess.run(command, shell=True, check=True)):
           numbers +=1
           print(f"Translation completed for folder: {input_folders}") 
            
    except subprocess.CalledProcessError as e:
        print(f"Error executing the script for folder {input_folders}: {e}")
    return numbers + 1

def main():
    start_number = int(input("Enter the starting number (e.g. 141): "))
    end_number = int(input("Enter the ending number: "))
    font_path = r"path\to\font"
    for numbers in range(start_number, end_number+1):
        base_folder = f'path\to\folder\images_{numbers}'
        output_folder = f'path\to\folder\images_{numbers}'
        process_folder(numbers, base_folder, output_folder, font_path)
if __name__ == "__main__":
    main()
