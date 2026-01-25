from analyzer import TargetAnalyzer
import pandas as pd
import os

def main():
    input_file = 'research_tool/target_urls.txt'
    output_file = 'research_tool/leads.csv'
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    with open(input_file, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]

    if not urls:
        print("No URLs found in input file.")
        return

    analyzer = TargetAnalyzer()
    df = analyzer.process_list(urls)
    
    print("\n--- Analysis Result ---")
    print(df[['title', 'score', 'strategy']])
    
    df.to_csv(output_file, index=False)
    print(f"\nSaved detailed results to {output_file}")

if __name__ == "__main__":
    main()
