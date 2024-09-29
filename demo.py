from ai import *
import csv

#def ask_sys(info, instructions)
#Example usage: 
# ask_sys("A frog on a log.", "Write a story about this")


def translate_to_english(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        csv_reader = csv.reader(infile)
        csv_writer = csv.writer(outfile)
        
        for row in csv_reader:
            if row:  # Check if the row is not empty
                original_text = row[0]
                translated_text = ask_sys(original_text, "Translate this statement into English. Only give the translated statement, say nothing else")
                csv_writer.writerow([translated_text])

# Call the function
translate_to_english('data.csv', 'translated_data.csv')






#second is to create topic summaries and then you can make an advocate for that. So you would run through it once to pick out all the topics, then a second time to make summary of each topic?
#basically it should go through in bunches of 15 at a time and make a list of all the topics and specific ideas covered in those 15. It will then take those results and combine each two of them together. It will do it again until htere is just one topic summary.

def generate_topic_summaries(input_file, output_csv):
    # Read all non-empty rows from the CSV file
    with open(input_file, 'r', encoding='utf-8') as infile:
        csv_reader = csv.reader(infile)
        all_texts = [row[0] for row in csv_reader if row]

    # Generate initial summaries for each batch of 15 statements
    summaries = []
    for i in range(0, len(all_texts), 15):
        batch = all_texts[i:i+15]
        batch_text = "\n".join(batch)
        batch_summary = ask_sys(batch_text, "List all topics covered in these statements in a bulleted list.")
        summaries.append(batch_summary)
        print(f"Generated summary for batch {i//15 + 1}/{len(all_texts)//15 + 1}")

    # Prepare CSV to store all iterations of summaries
    all_iterations = [summaries]

    # Combine summaries iteratively until only one remains
    iteration = 1
    while len(summaries) > 1:
        print(f"\nIteration {iteration} - Combining {len(summaries)} summaries")
        new_summaries = []
        for i in range(0, len(summaries), 2):
            if i + 1 < len(summaries):
                # Combine pair of summaries
                combined_text = summaries[i] + "\n\n" + summaries[i+1]
                combined_summary = ask_sys(combined_text, "Given this, create a single bulleted list of all topics with no duplicates. Just give this, nothing else")
            else:
                # If odd number of summaries, keep the last one as is
                combined_summary = summaries[i]
            new_summaries.append(combined_summary)
            print(f"Combined summaries {i+1} and {i+2 if i+1 < len(summaries) else '(none)'}")
        
        summaries = new_summaries
        all_iterations.append(summaries)
        iteration += 1

    # Write all iterations to CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        max_length = max(len(iteration) for iteration in all_iterations)
        for row in range(max_length):
            csv_row = []
            for iteration in all_iterations:
                csv_row.append(iteration[row] if row < len(iteration) else '')
            writer.writerow(csv_row)

    # Return the final, single summary
    return summaries[0], output_csv

# Usage example:
# final_summary, csv_file = generate_topic_summaries('translated_data.csv', 'summary_iterations.csv')
# print("Final Topic Summary:")
# print(final_summary)
# print(f"All summary iterations saved to {csv_file}")



#now for each topic collect a summary only regarding to it of people's worries. That way we could make a custom bot as a community advocate.

