from transformers import pipeline
from flask import Flask, request, jsonify, render_template

# Initialize question-answering pipeline using a generative model
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Predefined crime-specific contexts for better guidance
crime_contexts = {
    "burglary": """
    Burglary involves illegal entry into a property with the intent to commit theft. 
    To enhance your safety, consider the following:
    - **Secure all Entry Points**: Ensure all doors and windows are locked, and consider installing deadbolts. Reinforce weak spots, like sliding doors, with additional locks.
    - **Invest in Security Systems**: Use a comprehensive security system with cameras and alarms to deter intruders. Signage indicating a security system can also act as a deterrent.
    - **Neighborhood Awareness**: Get to know your neighbors and keep an eye on each other's properties. Forming a neighborhood watch can enhance safety and awareness of suspicious activities.
    """,
    "theft": """
    Theft is the unlawful taking of someone’s property. To safeguard against theft, keep the following tips in mind:
    - **Personal Vigilance**: Always keep an eye on your belongings, especially in crowded places. Hold bags and purses close to your body.
    - **Vehicle Security**: Never leave valuables in plain sight in your car. Use anti-theft devices and ensure all windows are secured.
    - **Awareness of Surroundings**: Stay alert in public spaces. If you notice suspicious behavior, report it to authorities immediately.
    """,
    "assault": """
    Assault can involve physical harm or the threat of harm. To protect yourself:
    - **Travel in Groups**: Avoid walking alone at night or in dimly lit areas. There is safety in numbers.
    - **Self-Defense Awareness**: Consider taking self-defense classes to empower yourself and learn how to respond in dangerous situations.
    - **Use Safety Apps**: Consider using safety apps on your phone that allow you to share your location with trusted contacts in case of an emergency.
    """,
    "cybercrime": """
    Cybercrime refers to crimes conducted via the internet, such as hacking or online fraud. To ensure your online safety:
    - **Strong Passwords**: Use unique, complex passwords for each of your online accounts and consider a password manager to keep track of them.
    - **Regular Software Updates**: Keep your operating system and software up to date to protect against vulnerabilities. Enable automatic updates where possible.
    - **Educate Yourself**: Stay informed about common cyber threats such as phishing scams and malware. Be cautious about clicking on links or downloading attachments from unknown sources.
    """,
    "public safety": """
    Public safety involves being aware of potential hazards in public areas. To enhance your safety in public:
    - **Stay Alert**: Be aware of your surroundings at all times, especially in crowded or unfamiliar places. Avoid distractions such as your phone when walking.
    - **Emergency Contacts**: Keep a list of emergency contacts on your phone and have a plan for what to do in case of an emergency.
    - **Follow Local Guidelines**: Stay updated on local safety regulations and emergency protocols, especially during large events or gatherings.
    """,
    "hurt": """
    Cases of hurt refer to physical injury inflicted on a person. To protect yourself from harm:
    - **Avoid Confrontations**: Stay calm and try to diffuse tense situations rather than escalating them. Walk away if you feel threatened.
    - **Self-Defense Tools**: Carry a personal alarm or pepper spray for protection. These can provide a crucial advantage in dangerous situations.
    - **Seek Help**: If you ever feel threatened, do not hesitate to ask for help from nearby individuals or authorities. 
    """,
    "kidnapping and abduction": """
    Kidnapping and abduction involve forcibly taking someone away. To prevent such incidents:
    - **Stay Aware**: Be cautious around strangers, especially if they ask for personal information or appear overly friendly. Trust your instincts.
    - **Use Safe Transportation**: If you are using rideshare apps, verify the driver's information and the vehicle's license plate before entering.
    - **Emergency Plans**: Have a plan for what to do in case of an emergency. Inform trusted friends or family about your whereabouts when going to unfamiliar places.
    """,
    "motor vehicle accidents": """
    Motor vehicle accidents can be prevented by:
    - **Seat Belts Are Mandatory**: Always wear your seat belt and ensure all passengers do the same. This simple action can save lives.
    - **Avoid Distractions**: Stay focused on the road. Avoid texting or engaging with your phone while driving.
    - **Vehicle Maintenance**: Regularly check your vehicle's brakes, tires, and lights to ensure they are in good working order.
    """,
    "molestation": """
    Molestation involves unwanted or inappropriate physical contact. To enhance your safety:
    - **Be Cautious**: Avoid secluded areas, especially if you feel uncomfortable. Stay where there are other people.
    - **Trust Your Instincts**: If someone makes you feel uneasy, distance yourself from that person and seek help.
    - **Communicate**: Inform trusted friends or family about uncomfortable encounters. Open dialogue about safety can empower you.
    """,
    "robbery": """
    Robbery involves the use of force to steal. To stay safe during such incidents:
    - **Keep Valuables Hidden**: Do not display expensive items in public. Keep your phone and wallet secure and out of sight.
    - **Stay Calm**: In the event of a robbery, comply with the demands of the robber to avoid escalation. Your safety is the priority.
    - **Report Immediately**: As soon as it is safe to do so, report the robbery to the authorities with as much detail as possible.
    """
}

def public_safety_chatbot(user_query):
    """
    Generate a response to public safety-related queries, ensuring that at least 3 safety points are provided.
    The model will give crime-specific answers based on the context provided for each crime type.
    """
    # Identify the crime type from the user query (simple keyword matching)
    if "burglary" in user_query.lower():
        context = crime_contexts["burglary"]
    elif "theft" in user_query.lower():
        context = crime_contexts["theft"]
    elif "assault" in user_query.lower():
        context = crime_contexts["assault"]
    elif "cybercrime" in user_query.lower():
        context = crime_contexts["cybercrime"]
    elif "public safety" in user_query.lower():
        context = crime_contexts["public safety"]
    elif "hurt" in user_query.lower():
        context = crime_contexts["hurt"]
    elif "kidnapping" in user_query.lower() or "abduction" in user_query.lower():
        context = crime_contexts["kidnapping and abduction"]
    elif "motor vehicle accident" in user_query.lower() or "accident" in user_query.lower():
        context = crime_contexts["motor vehicle accidents"]
    elif "molestation" in user_query.lower():
        context = crime_contexts["molestation"]
    elif "robbery" in user_query.lower():
        context = crime_contexts["robbery"]
    else:
        # If the crime type isn't found, use a default safety context
        context = """
        Staying safe is important in all situations. Here are some general safety tips:
        - **Stay alert and aware of your surroundings.**
        - **Avoid risky areas, especially at night, and travel in groups when possible.**
        - **Consider investing in personal security measures such as alarms, locks, and security systems.**
        """

    # Generate a clear and structured output without repeating the question
    response = f"To stay safe, consider the following tips:\n\n"

    # Append each safety tip to the response with line breaks for better formatting
    for line in context.strip().splitlines():
        response += f"{line.strip()}\n\n"  # Adding double line breaks for better spacing

    return response.strip()

# Flask web app setup
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_query = request.form.get('query')
    if not user_query:
        return jsonify({'error': 'No query provided'}), 400

    # Generate response from the chatbot
    answer = public_safety_chatbot(user_query)
    
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
