from transformers import pipeline

# Initialize summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_crime_report(crime_report):
    """
    Summarize the given crime report using BART.
    """
    summary = summarizer(crime_report, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Example usage
crime_report = """
1. FIR Number:
FIR-2024-BLR-0456

2. Date and Time of the Incident:
2024-10-01, 22:15

3. Crime Category:
Robbery

4. Location of Crime:

Address: 15th Main, 4th Block, Koramangala, Bengaluru, Karnataka, 560034
Latitude: 12.934533
Longitude: 77.610116
5. District and Police Station:

District: Bengaluru City
Police Station: Koramangala Police Station
6. Victim Details:

Name: Anirudh Sharma
Age: 34
Gender: Male
Contact Information: anirudh.sharma@example.com
7. Offender Details (if available):

Name: Unknown
Age: Approx. 25-30
Physical Description: Two male suspects, wearing black hoodies and masks, approx. 5'10" tall, medium build.
8. Crime Severity / Threat Level:
High

9. Witness Information:

Name: Rohit Kumar
Contact Information: rohit.kumar@example.com
Statement: "I was walking nearby and saw two men on a motorcycle stop the victim. They seemed aggressive, and I heard one of them shout at the victim to hand over his belongings. I noted that the motorcycle had no visible number plate."
10. Evidence Collected:

Image of Suspects: Uploaded CCTV footage image (suspects_cctv.jpg)
Description: "Still image from CCTV showing suspects fleeing the scene."
11. Status of Investigation:
Under Investigation
"""
summary = summarize_crime_report(crime_report)
print("Crime Report Summary:\n", summary)
